from typing import Optional, Union

import numpy as np
import torch
import torch.nn as nn
from torch_geometric.data import Dataset
from torch_geometric.loader import DataLoader
from tqdm import tqdm

from argparse import ArgumentParser
import pytorch_lightning as pl
from datasets import ArgoverseV2Dataset
from predictors import QCNet


def inference_benchmark(
        model: nn.Module,
        dataset: Dataset,
        device: Optional[Union[torch.device, str]],
        warmup_steps: int = 10,
        batch_size: int = 1,
        shuffle: bool = False,
        num_workers: int = 0,
        pin_memory: bool = True,
        persistent_workers: bool = True) -> None:
    model.to(device)
    model.eval()
    dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=shuffle, num_workers=num_workers,
                            pin_memory=pin_memory, persistent_workers=persistent_workers and num_workers > 0)
    start, end = torch.cuda.Event(enable_timing=True), torch.cuda.Event(enable_timing=True)

    times = []
    with torch.no_grad():
        for i, batch in enumerate(tqdm(dataloader)):
            batch = batch.to(device)
            if i == 0:
                for _ in range(warmup_steps):
                    model(batch)
            start.record()
            model(batch)
            end.record()
            torch.cuda.synchronize()
            times.append(start.elapsed_time(end))
            break
    mean_time = np.mean(times)
    std_time = np.std(times)
    print('Average inference time (ms): {:.3f} +- {:.3f}'.format(mean_time, std_time))

if __name__ == '__main__':
    pl.seed_everything(2023, workers=True)

    parser = ArgumentParser()
    parser.add_argument('--model', type=str, required=True)
    parser.add_argument('--root', type=str, required=True)
    parser.add_argument('--batch_size', type=int, default=32)
    parser.add_argument('--num_workers', type=int, default=8)
    parser.add_argument('--pin_memory', type=bool, default=True)
    parser.add_argument('--persistent_workers', type=bool, default=True)
    parser.add_argument('--devices', type=int, default=1)
    parser.add_argument('--ckpt_path', type=str, required=True)
    args = parser.parse_args()

    model = {
        'QCNet': QCNet,
    }[args.model].load_from_checkpoint(checkpoint_path=args.ckpt_path)

    test_dataset = {
        'argoverse_v2': ArgoverseV2Dataset,
    }[model.dataset](root=args.root, split='val')
    
    inference_benchmark(model, test_dataset, device='cuda:0')