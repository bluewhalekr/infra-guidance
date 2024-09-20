import os
import shutil

def copy_json_to_subfolders_with_new_name(source_file_path, dest_folder):
    # 대상 폴더의 모든 하위 폴더 목록을 가져오기
    subfolders = [os.path.join(dest_folder, name) for name in os.listdir(dest_folder) if os.path.isdir(os.path.join(dest_folder, name))]

    # 원본 JSON 파일을 각 하위 폴더로 복사하며 파일명 변경
    for folder in subfolders:
        folder_name = os.path.basename(folder)
        new_file_name = f"log_map_archive_{folder_name}.json"
        dest_file_path = os.path.join(folder, new_file_name)
        shutil.copyfile(source_file_path, dest_file_path)
        print(f"Copied {source_file_path} to {dest_file_path}")

use_case = ["A1", "B1", "C1", "D3", "D4"]
src_path = '/noah/dataset/infra-guidance/SUMO/sumo_origin'
dst_path = '/noah/dataset/infra-guidance/SUMO/sumo_process'

for uc in use_case:
    # 소스 파일 경로와 대상 폴더 지정
    source_file_path = os.path.join(src_path, '{}/{}_map.json'.format(uc,uc))

    # train 폴더에 대해 JSON 파일을 복사하며 새로운 이름으로 저장
    # train_dest_folder = f'./{use_case}_parquet/train/raw'
    train_dest_folder = os.path.join(dst_path,'{}/train/raw'.format(uc))
    copy_json_to_subfolders_with_new_name(source_file_path, train_dest_folder)

    # val 폴더에 대해 JSON 파일을 복사하며 새로운 이름으로 저장
    # val_dest_folder = f'./{use_case}_parquet/val/raw'
    val_dest_folder = os.path.join(dst_path,'{}/val/raw'.format(uc))
    copy_json_to_subfolders_with_new_name(source_file_path, val_dest_folder)
