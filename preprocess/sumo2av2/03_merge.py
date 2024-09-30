import os
import shutil

root_dir = '/noah/dataset/infra-guidance/SUMO/sumo_process'
save_dir = os.path.join(root_dir,'merge')
use_case = ['A1', 'B1', 'D3']

for uc in use_case:
    use_case_folder=os.path.join(root_dir, uc)
    
    for split in os.listdir(use_case_folder):
        if 'raw' not in os.listdir(os.path.join(use_case_folder, split)):
            continue

        src_raw_folder_path = os.path.join(use_case_folder, split, 'raw')
        for raw_name in os.listdir(src_raw_folder_path):
            src_raw_file_path = os.path.join(src_raw_folder_path, raw_name)
            for name in os.listdir(src_raw_file_path):
                save_raw_folder_path = os.path.join(save_dir, split, 'raw', '{}_{}'.format(uc, raw_name))
                if not os.path.exists(save_raw_folder_path):
                    os.makedirs(save_raw_folder_path, exist_ok=True)
                shutil.copy(os.path.join(src_raw_file_path,name), os.path.join(save_raw_folder_path, name.replace(raw_name,'{}_{}'.format(uc, raw_name))))
