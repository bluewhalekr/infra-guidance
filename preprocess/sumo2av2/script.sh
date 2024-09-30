# train / validation
python 00_merge_sumo.py --root_dir /noah/dataset/infra-guidance/SUMO/sumo_origin --use_case "A1" "B1" "C1" "D3" "D4" --mode
python 01_agent_SUMOtoAV2.py --src_dir /noah/dataset/infra-guidance/SUMO/sumo_origin --dst_dir /noah/dataset/infra-guidance/SUMO/sumo_process --use_case "A1" "B1" "C1" "D3" "D4" --mode
python 02_json_copy.py --src_dir /noah/dataset/infra-guidance/SUMO/sumo_origin --dst_dir /noah/dataset/infra-guidance/SUMO/sumo_process --use_case "A1" "B1" "C1" "D3" "D4" --mode
python 03_merge.py --root_dir /noah/dataset/infra-guidance/SUMO/sumo_process --save_dir /noah/dataset/infra-guidance/SUMO/sumo_process/merge --use_case "A1" "B1" "C1" "D3" "D4" --mode

# test
python 00_merge_sumo.py --root_dir /noah/dataset/infra-guidance/SUMO/sumo_origin --use_case "A1" "B1" "D3"
python 01_agent_SUMOtoAV2.py --src_dir /noah/dataset/infra-guidance/SUMO/sumo_origin --dst_dir /noah/dataset/infra-guidance/SUMO/sumo_process --use_case "A1" "B1" "D3"
python 02_json_copy.py --src_dir /noah/dataset/infra-guidance/SUMO/sumo_origin --dst_dir /noah/dataset/infra-guidance/SUMO/sumo_process --use_case "A1" "B1" "D3"
python 03_merge.py --root_dir /noah/dataset/infra-guidance/SUMO/sumo_process --save_dir /noah/dataset/infra-guidance/SUMO/sumo_process/merge --use_case ""A1" "B1" "D3"
