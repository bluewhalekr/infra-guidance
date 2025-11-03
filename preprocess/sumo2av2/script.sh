# train / validation
# python 00_merge_sumo.py --root_dir /noah/dataset/infra-guidance/SUMO/sumo_origin --use_case "A1" "B1" "C1" "D3" "D4" --mode
# python 01_agent_SUMOtoAV2.py --src_dir /noah/dataset/infra-guidance/SUMO/sumo_origin --dst_dir /noah/dataset/infra-guidance/SUMO/sumo_process --use_case "A1" "B1" "C1" "D3" "D4" --mode
# python 02_json_copy.py --src_dir /noah/dataset/infra-guidance/SUMO/sumo_origin --dst_dir /noah/dataset/infra-guidance/SUMO/sumo_process --use_case "A1" "B1" "C1" "D3" "D4" --mode
# python 03_merge.py --root_dir /noah/dataset/infra-guidance/SUMO/sumo_process --save_dir /noah/dataset/infra-guidance/SUMO/sumo_process/merge --use_case "A1" "B1" "C1" "D3" "D4" --mode

# python 00_merge_sumo.py --root_dir /noah/dataset/infra-guidance/SUMO/sumo_origin --use_case "A1" "B1" "C1" "D3" "D4" --mode
# python 01_agent_SUMOtoAV2.py --src_dir /noah/dataset/infra-guidance/SUMO/sumo_origin --dst_dir /noah/dataset/infra-guidance/SUMO/sumo_process_step_1 --use_case "A1" "B1" "C1" "D3" "D4" --mode --sample_step 1
# python 02_json_copy.py --src_dir /noah/dataset/infra-guidance/SUMO/sumo_origin --dst_dir /noah/dataset/infra-guidance/SUMO/sumo_process_step_1 --use_case "A1" "B1" "C1" "D3" "D4" --mode

# python 01_agent_SUMOtoAV2.py --src_dir /noah/dataset/infra-guidance/SUMO/sumo_origin --dst_dir /noah/dataset/infra-guidance/SUMO/sumo_process_step_5 --use_case "A1" "B1" "C1" "D3" "D4" --mode --sample_step 5
# python 02_json_copy.py --src_dir /noah/dataset/infra-guidance/SUMO/sumo_origin --dst_dir /noah/dataset/infra-guidance/SUMO/sumo_process_step_5 --use_case "A1" "B1" "C1" "D3" "D4" --mode

# python 01_agent_SUMOtoAV2.py --src_dir /noah/dataset/infra-guidance/SUMO/sumo_origin --dst_dir /noah/dataset/infra-guidance/SUMO/sumo_process_step_10 --use_case "A1" "B1" "C1" "D3" "D4" --mode --sample_step 10
# python 02_json_copy.py --src_dir /noah/dataset/infra-guidance/SUMO/sumo_origin --dst_dir /noah/dataset/infra-guidance/SUMO/sumo_process_step_10 --use_case "A1" "B1" "C1" "D3" "D4" --mode

# test
# python 00_merge_sumo.py --root_dir /noah/dataset/infra-guidance/SUMO/sumo_origin --use_case "A1" "B1" "D3"
# python 01_agent_SUMOtoAV2.py --src_dir /noah/dataset/infra-guidance/SUMO/sumo_origin --dst_dir /noah/dataset/infra-guidance/SUMO/sumo_process --use_case "A1" "B1" "D3"
# python 02_json_copy.py --src_dir /noah/dataset/infra-guidance/SUMO/sumo_origin --dst_dir /noah/dataset/infra-guidance/SUMO/sumo_process --use_case "A1" "B1" "D3"
# python 03_merge.py --root_dir /noah/dataset/infra-guidance/SUMO/sumo_process --save_dir /noah/dataset/infra-guidance/SUMO/sumo_process/merge --use_case ""A1" "B1" "D3"

# train/val
python 00_merge_sumo.py --root_dir /workspace/rosie/Dataset/IG --use_case "SS_origin1" --mode
python 01_agent_SUMOtoAV2.py --src_dir /workspace/rosie/Dataset/IG --dst_dir /workspace/rosie/Desktop/infra-guidance_process_noah/data_sumo --use_case "SS_origin1" --mode --sample_step 10 --input_frame 10
python 02_json_copy.py --src_dir /workspace/rosie/Dataset/IG --dst_dir /workspace/rosie/Desktop/infra-guidance_process_noah/data_sumo --use_case "SS_origin1" --mode

# test
# python 00_merge_sumo.py --root_dir /workspace/rosie/Dataset/IG --use_case "A1_tc" 
# python 01_agent_SUMOtoAV2.py --src_dir /workspace/rosie/Dataset/IG --dst_dir /workspace/rosie/Desktop/infra-guidance_process_noah/data_sumo --use_case "A1_tc" --sample_step 10 --input_frame 15
# python 02_json_copy.py --src_dir /workspace/rosie/Dataset/IG --dst_dir /workspace/rosie/Desktop/infra-guidance_process_noah/data_sumo --use_case "A1_tc" 
