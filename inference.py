from typing import Optional, Union

import numpy as np
import torch
import torch.nn as nn
from torch_geometric.data import Dataset
from torch_geometric.loader import DataLoader
from tqdm import tqdm
import json
import time

from argparse import ArgumentParser
import pytorch_lightning as pl
from datasets import ArgoverseV2Dataset
from predictors import QCNet
from datetime import datetime
import random

import warnings

warnings.filterwarnings("ignore")


def inference_benchmark(
    model: nn.Module,
    dataset: Dataset,
    device: Optional[Union[torch.device, str]],
    warmup_steps: int = 10,
    batch_size: int = 1,
    shuffle: bool = False,
    num_workers: int = 0,
    pin_memory: bool = True,
    persistent_workers: bool = True,
) -> None:
    model.to(device)
    model.eval()
    dataloader = DataLoader(
        dataset,
        batch_size=batch_size,
        shuffle=shuffle,
        num_workers=num_workers,
        pin_memory=pin_memory,
        persistent_workers=persistent_workers and num_workers > 0,
    )
    start, end = torch.cuda.Event(enable_timing=True), torch.cuda.Event(
        enable_timing=True
    )

    times = []
    total_inference_time = 0
    total_samples = 0

    with torch.no_grad():
        save_total = []
        for i, batch in enumerate(
            tqdm(dataloader)
        ):  ### 2502 - 분석용 전체 배치로 추론 수정
            save_json = {
                "refine_result": [],
                "propose_result": [],
                "input_trej": None,
                "gt_trej": None,
            }
            batch = batch.to(device)
            if i == 0:
                for _ in range(warmup_steps):
                    result = model(batch)
            
            inference_start_time = time.time()
            start.record()
            result = model(batch)

            ### get original prediction
            num_obj, _, _, _ = result["loc_refine_pos"].shape
            set_time = dict()
            prop_time = dict()

            ### SET list DUE TO ways1 PROTOCOL
            ###
            for i in range(30):
                set_time[str((i + 1) / 10)] = []  # key = offset
                prop_time[str((i + 1) / 10)] = []  # key = offset

            for obj_idx in range(num_obj):  # 객체 이미 지정되어있음
                tensor_pi = result["pi"][obj_idx]
                get_highest_idx = tensor_pi.argmax()

                raw_result = result["loc_refine_pos"][
                    obj_idx : obj_idx + 1, get_highest_idx, :, :
                ]
                # propose result 포함
                raw_propose_result = result["loc_propose_pos"][
                    obj_idx : obj_idx + 1, get_highest_idx, :, :
                ]
                convert_result = invert_transform_result(
                    batch, obj_idx, raw_result, 10, 30
                )
                ####
                convert_propose_result = invert_transform_result(
                    batch, obj_idx, raw_propose_result, 10, 30
                )

                pred_instance = batch["agent"]["id"][0][obj_idx]
                position_xs = convert_result[:, :, 0].cpu().numpy()[0].tolist()
                position_ys = convert_result[:, :, 1].cpu().numpy()[0].tolist()

                for i in range(30):
                    set_time[str((i + 1) / 10)].append(
                        {
                            "ObjectID": pred_instance,
                            "DistanceX": position_xs[i],
                            "DistanceY": position_ys[i],
                        }
                    )

                position_xs_pro = (
                    convert_propose_result[:, :, 0].cpu().numpy()[0].tolist()
                )
                position_ys_pro = (
                    convert_propose_result[:, :, 1].cpu().numpy()[0].tolist()
                )
                for i in range(30):
                    prop_time[str((i + 1) / 10)].append(
                        {
                            "ObjectID": pred_instance,
                            "DistanceX": position_xs_pro[i],
                            "DistanceY": position_ys_pro[i],
                        }
                    )

            end.record()
            torch.cuda.synchronize()
            times.append(start.elapsed_time(end))
            
            inference_time = time.time() - inference_start_time
            total_inference_time += inference_time
            total_samples += batch_size

            save_json["refine_result"].append(set_time)
            save_json["propose_result"].append(prop_time)
            save_json["input_trej"] = (
                batch["agent"]["position"][:, :10].cpu().numpy().tolist()
            )
            save_json["gt_trej"] = (
                batch["agent"]["position"][:, 10:].cpu().numpy().tolist()
            )
            save_total.append(save_json)
    mean_time = np.mean(times)
    std_time = np.std(times)
    avg_inference_time = total_inference_time / total_samples
    print("Average inference time (ms): {:.3f} +- {:.3f}".format(mean_time, std_time))
    print(f"Average inference time per sample: {avg_inference_time:.4f} seconds")
    return save_total


def invert_transform_result(
    ref_data, pick_id, pred_data, num_historical_steps, num_future_steps
):
    origin = ref_data["agent"]["position"][
        pick_id : pick_id + 1, num_historical_steps - 1
    ]
    theta = ref_data["agent"]["heading"][
        pick_id : pick_id + 1, num_historical_steps - 1
    ]
    cos, sin = theta.cos(), theta.sin()

    rot_mat_inv = theta.new_zeros(1, 2, 2)  # preidct one by one
    rot_mat_inv[:, 0, 0] = cos
    rot_mat_inv[:, 0, 1] = sin
    rot_mat_inv[:, 1, 0] = -sin
    rot_mat_inv[:, 1, 1] = cos

    check_result = torch.bmm(pred_data, rot_mat_inv) + origin[:, :2].unsqueeze(1)

    return check_result


if __name__ == "__main__":
    # seed
    seed = 2023
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed(seed)
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False

    pl.seed_everything(seed, workers=True)

    parser = ArgumentParser()
    parser.add_argument("--model", type=str, required=True)
    parser.add_argument("--root", type=str, required=True)
    parser.add_argument("--batch_size", type=int, default=32)
    parser.add_argument("--num_workers", type=int, default=8)
    parser.add_argument("--pin_memory", type=bool, default=True)
    parser.add_argument("--persistent_workers", type=bool, default=True)
    parser.add_argument("--devices", type=int, default=1)
    parser.add_argument("--ckpt_path", type=str, required=True)
    args = parser.parse_args()

    model = {
        "QCNet": QCNet,
    }[
        args.model
    ].load_from_checkpoint(checkpoint_path=args.ckpt_path)

    test_dataset = {
        "argoverse_v2": ArgoverseV2Dataset,
    }[
        model.dataset
    ](root=args.root, split="val")

    object_result = inference_benchmark(model, test_dataset, device="cuda:0")

    print("Saving ... ")
    final_result = {"PredictDataList": object_result}

    # Get dataset name from root path
    dataset_name = args.root.split('/')[-1]
    current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = f"inference_result/{dataset_name}_inference_{current_time}.json"

    # 결과를 JSON 형식으로 저장
    with open(file_name, "w") as file:
        json.dump(final_result, file, indent=4)
    print("Inference done.")
