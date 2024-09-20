import os
import shutil

root_dir = '/noah/dataset/infra-guidance/SUMO/sumo_process'
save_dir = os.path.join(root_dir,'merge')
use_case = ['A1', 'B1', 'C1', 'D3', 'D4']

for uc in use_case:
    use_case_folder=os.path.join(root_dir, uc)
    
    for split in os.listdir(use_case_folder):
        if 'raw' not in os.listdir(os.path.join(use_case_folder, split)):
            continue
    
        for raw_name in os.listdir(os.path.join(use_case_folder, split, 'raw')):
            shutil.copytree(
                os.path.join(use_case_folder, split, 'raw', raw_name),
                os.path.join(save_dir, split, 'raw', '{}_{}'.format(uc, raw_name)))