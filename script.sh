# train
# python train.py --root /noah/dataset/infra-guidance/SUMO/sumo_process/A1 --ckpt_path /noah/ckpt/finetuning/infra_guidance/A1 --train_batch_size 16 --val_batch_size 1 --test_batch_size 1 --num_workers 2 --devices 1 --dataset argoverse_v2 --num_historical_steps 10 --num_future_steps 30 --num_recurrent_steps 3 --pl2pl_radius 150 --pl2a_radius 50 --a2a_radius 50 --num_t2m_steps 30 --pl2m_radius 150 --a2m_radius 150
# python train.py --root /noah/dataset/infra-guidance/SUMO/sumo_process/B1 --ckpt_path /noah/ckpt/finetuning/infra_guidance/B1 --train_batch_size 16 --val_batch_size 1 --test_batch_size 1 --num_workers 2 --devices 1 --dataset argoverse_v2 --num_historical_steps 10 --num_future_steps 30 --num_recurrent_steps 3 --pl2pl_radius 150 --pl2a_radius 50 --a2a_radius 50 --num_t2m_steps 30 --pl2m_radius 150 --a2m_radius 150
# python train.py --root /noah/dataset/infra-guidance/SUMO/sumo_process/C1 --ckpt_path /noah/ckpt/finetuning/infra_guidance/C1 --train_batch_size 16 --val_batch_size 1 --test_batch_size 1 --num_workers 2 --devices 1 --dataset argoverse_v2 --num_historical_steps 10 --num_future_steps 30 --num_recurrent_steps 3 --pl2pl_radius 150 --pl2a_radius 50 --a2a_radius 50 --num_t2m_steps 30 --pl2m_radius 150 --a2m_radius 150
# python train.py --root /noah/dataset/infra-guidance/SUMO/sumo_process/D3 --ckpt_path /noah/ckpt/finetuning/infra_guidance/D3 --train_batch_size 16 --val_batch_size 1 --test_batch_size 1 --num_workers 2 --devices 1 --dataset argoverse_v2 --num_historical_steps 10 --num_future_steps 30 --num_recurrent_steps 3 --pl2pl_radius 150 --pl2a_radius 50 --a2a_radius 50 --num_t2m_steps 30 --pl2m_radius 150 --a2m_radius 150
# python train.py --root /noah/dataset/infra-guidance/SUMO/sumo_process/D4 --ckpt_path /noah/ckpt/finetuning/infra_guidance/D4 --train_batch_size 16 --val_batch_size 1 --test_batch_size 1 --num_workers 2 --devices 1 --dataset argoverse_v2 --num_historical_steps 10 --num_future_steps 30 --num_recurrent_steps 3 --pl2pl_radius 150 --pl2a_radius 50 --a2a_radius 50 --num_t2m_steps 30 --pl2m_radius 150 --a2m_radius 150
# python train.py --root /noah/dataset/infra-guidance/SUMO/sumo_process/merge --ckpt_path /noah/ckpt/finetuning/infra_guidance/merge --train_batch_size 16 --val_batch_size 1 --test_batch_size 1 --num_workers 2 --devices 1 --dataset argoverse_v2 --num_historical_steps 10 --num_future_steps 30 --num_recurrent_steps 3 --pl2pl_radius 150 --pl2a_radius 50 --a2a_radius 50 --num_t2m_steps 30 --pl2m_radius 150 --a2m_radius 150

# python train.py --root /noah/dataset/infra-guidance/SUMO/sumo_process_step_1/A1 --ckpt_path /noah/ckpt/finetuning/infra_guidance/A1_step1 --train_batch_size 16 --val_batch_size 1 --test_batch_size 1 --num_workers 2 --devices 1 --dataset argoverse_v2 --num_historical_steps 10 --num_future_steps 30 --num_recurrent_steps 3 --pl2pl_radius 150 --pl2a_radius 50 --a2a_radius 50 --num_t2m_steps 30 --pl2m_radius 150 --a2m_radius 150
# python train.py --root /noah/dataset/infra-guidance/SUMO/sumo_process_step_1/B1 --ckpt_path /noah/ckpt/finetuning/infra_guidance/B1_step1 --train_batch_size 16 --val_batch_size 1 --test_batch_size 1 --num_workers 2 --devices 1 --dataset argoverse_v2 --num_historical_steps 10 --num_future_steps 30 --num_recurrent_steps 3 --pl2pl_radius 150 --pl2a_radius 50 --a2a_radius 50 --num_t2m_steps 30 --pl2m_radius 150 --a2m_radius 150
# python train.py --root /noah/dataset/infra-guidance/SUMO/sumo_process_step_1/C1 --ckpt_path /noah/ckpt/finetuning/infra_guidance/C1_step1 --train_batch_size 16 --val_batch_size 1 --test_batch_size 1 --num_workers 2 --devices 1 --dataset argoverse_v2 --num_historical_steps 10 --num_future_steps 30 --num_recurrent_steps 3 --pl2pl_radius 150 --pl2a_radius 50 --a2a_radius 50 --num_t2m_steps 30 --pl2m_radius 150 --a2m_radius 150
# python train.py --root /noah/dataset/infra-guidance/SUMO/sumo_process_step_1/D3 --ckpt_path /noah/ckpt/finetuning/infra_guidance/D3_step1 --train_batch_size 16 --val_batch_size 1 --test_batch_size 1 --num_workers 2 --devices 1 --dataset argoverse_v2 --num_historical_steps 10 --num_future_steps 30 --num_recurrent_steps 3 --pl2pl_radius 150 --pl2a_radius 50 --a2a_radius 50 --num_t2m_steps 30 --pl2m_radius 150 --a2m_radius 150
# python train.py --root /noah/dataset/infra-guidance/SUMO/sumo_process_step_1/D4 --ckpt_path /noah/ckpt/finetuning/infra_guidance/D4_step1 --train_batch_size 16 --val_batch_size 1 --test_batch_size 1 --num_workers 2 --devices 1 --dataset argoverse_v2 --num_historical_steps 10 --num_future_steps 30 --num_recurrent_steps 3 --pl2pl_radius 150 --pl2a_radius 50 --a2a_radius 50 --num_t2m_steps 30 --pl2m_radius 150 --a2m_radius 150

# python train.py --root /noah/dataset/infra-guidance/SUMO/sumo_process_step_5/A1 --ckpt_path /noah/ckpt/finetuning/infra_guidance/A1_step5 --train_batch_size 16 --val_batch_size 1 --test_batch_size 1 --num_workers 2 --devices 1 --dataset argoverse_v2 --num_historical_steps 10 --num_future_steps 30 --num_recurrent_steps 3 --pl2pl_radius 150 --pl2a_radius 50 --a2a_radius 50 --num_t2m_steps 30 --pl2m_radius 150 --a2m_radius 150
# python train.py --root /noah/dataset/infra-guidance/SUMO/sumo_process_step_5/B1 --ckpt_path /noah/ckpt/finetuning/infra_guidance/B1_step5 --train_batch_size 16 --val_batch_size 1 --test_batch_size 1 --num_workers 2 --devices 1 --dataset argoverse_v2 --num_historical_steps 10 --num_future_steps 30 --num_recurrent_steps 3 --pl2pl_radius 150 --pl2a_radius 50 --a2a_radius 50 --num_t2m_steps 30 --pl2m_radius 150 --a2m_radius 150
# python train.py --root /noah/dataset/infra-guidance/SUMO/sumo_process_step_5/C1 --ckpt_path /noah/ckpt/finetuning/infra_guidance/C1_step5 --train_batch_size 16 --val_batch_size 1 --test_batch_size 1 --num_workers 2 --devices 1 --dataset argoverse_v2 --num_historical_steps 10 --num_future_steps 30 --num_recurrent_steps 3 --pl2pl_radius 150 --pl2a_radius 50 --a2a_radius 50 --num_t2m_steps 30 --pl2m_radius 150 --a2m_radius 150
# python train.py --root /noah/dataset/infra-guidance/SUMO/sumo_process_step_5/D3 --ckpt_path /noah/ckpt/finetuning/infra_guidance/D3_step5 --train_batch_size 16 --val_batch_size 1 --test_batch_size 1 --num_workers 2 --devices 1 --dataset argoverse_v2 --num_historical_steps 10 --num_future_steps 30 --num_recurrent_steps 3 --pl2pl_radius 150 --pl2a_radius 50 --a2a_radius 50 --num_t2m_steps 30 --pl2m_radius 150 --a2m_radius 150
# python train.py --root /noah/dataset/infra-guidance/SUMO/sumo_process_step_5/D4 --ckpt_path /noah/ckpt/finetuning/infra_guidance/D4_step5 --train_batch_size 16 --val_batch_size 1 --test_batch_size 1 --num_workers 2 --devices 1 --dataset argoverse_v2 --num_historical_steps 10 --num_future_steps 30 --num_recurrent_steps 3 --pl2pl_radius 150 --pl2a_radius 50 --a2a_radius 50 --num_t2m_steps 30 --pl2m_radius 150 --a2m_radius 150

# python train.py --root /noah/dataset/infra-guidance/SUMO/sumo_process_step_10/A1 --ckpt_path /noah/ckpt/finetuning/infra_guidance/A1_step10 --train_batch_size 16 --val_batch_size 1 --test_batch_size 1 --num_workers 2 --devices 1 --dataset argoverse_v2 --num_historical_steps 10 --num_future_steps 30 --num_recurrent_steps 3 --pl2pl_radius 150 --pl2a_radius 50 --a2a_radius 50 --num_t2m_steps 30 --pl2m_radius 150 --a2m_radius 150
# python train.py --root /noah/dataset/infra-guidance/SUMO/sumo_process_step_10/B1 --ckpt_path /noah/ckpt/finetuning/infra_guidance/B1_step10 --train_batch_size 16 --val_batch_size 1 --test_batch_size 1 --num_workers 2 --devices 1 --dataset argoverse_v2 --num_historical_steps 10 --num_future_steps 30 --num_recurrent_steps 3 --pl2pl_radius 150 --pl2a_radius 50 --a2a_radius 50 --num_t2m_steps 30 --pl2m_radius 150 --a2m_radius 150
# python train.py --root /noah/dataset/infra-guidance/SUMO/sumo_process_step_10/C1 --ckpt_path /noah/ckpt/finetuning/infra_guidance/C1_step10 --train_batch_size 16 --val_batch_size 1 --test_batch_size 1 --num_workers 2 --devices 1 --dataset argoverse_v2 --num_historical_steps 10 --num_future_steps 30 --num_recurrent_steps 3 --pl2pl_radius 150 --pl2a_radius 50 --a2a_radius 50 --num_t2m_steps 30 --pl2m_radius 150 --a2m_radius 150
# python train.py --root /noah/dataset/infra-guidance/SUMO/sumo_process_step_10/D3 --ckpt_path /noah/ckpt/finetuning/infra_guidance/D3_step10 --train_batch_size 16 --val_batch_size 1 --test_batch_size 1 --num_workers 2 --devices 1 --dataset argoverse_v2 --num_historical_steps 10 --num_future_steps 30 --num_recurrent_steps 3 --pl2pl_radius 150 --pl2a_radius 50 --a2a_radius 50 --num_t2m_steps 30 --pl2m_radius 150 --a2m_radius 150
# python train.py --root /noah/dataset/infra-guidance/SUMO/sumo_process_step_10/D4 --ckpt_path /noah/ckpt/finetuning/infra_guidance/D4_step10 --train_batch_size 16 --val_batch_size 1 --test_batch_size 1 --num_workers 2 --devices 1 --dataset argoverse_v2 --num_historical_steps 10 --num_future_steps 30 --num_recurrent_steps 3 --pl2pl_radius 150 --pl2a_radius 50 --a2a_radius 50 --num_t2m_steps 30 --pl2m_radius 150 --a2m_radius 150

# val
# Dataset_Model
python val.py --model QCNet --root /noah/dataset/infra-guidance/SUMO/sumo_process/A1 --ckpt_path /noah/ckpt/finetuning/infra_guidance/A1_step1/epoch=64-val_minFDE=0.90.ckpt
python val.py --model QCNet --root /noah/dataset/infra-guidance/SUMO/sumo_process/B1 --ckpt_path /noah/ckpt/finetuning/infra_guidance/A1_step1/epoch=64-val_minFDE=0.90.ckpt
python val.py --model QCNet --root /noah/dataset/infra-guidance/SUMO/sumo_process/D3 --ckpt_path /noah/ckpt/finetuning/infra_guidance/A1_step1/epoch=64-val_minFDE=0.90.ckpt
# python val.py --model QCNet --root /noah/dataset/infra-guidance/SUMO/sumo_process/merge --ckpt_path /noah/ckpt/finetuning/infra_guidance/A1_step1/epoch=64-val_minFDE=0.90.ckpt

python val.py --model QCNet --root /noah/dataset/infra-guidance/SUMO/sumo_process/A1 --ckpt_path /noah/ckpt/finetuning/infra_guidance/B1_step1/epoch=16-val_minFDE=0.53.ckpt
python val.py --model QCNet --root /noah/dataset/infra-guidance/SUMO/sumo_process/B1 --ckpt_path /noah/ckpt/finetuning/infra_guidance/B1_step1/epoch=16-val_minFDE=0.53.ckpt
python val.py --model QCNet --root /noah/dataset/infra-guidance/SUMO/sumo_process/D3 --ckpt_path /noah/ckpt/finetuning/infra_guidance/B1_step1/epoch=16-val_minFDE=0.53.ckpt
# python val.py --model QCNet --root /noah/dataset/infra-guidance/SUMO/sumo_process/merge --ckpt_path /noah/ckpt/finetuning/infra_guidance/B1_step1/epoch=16-val_minFDE=0.53.ckpt

python val.py --model QCNet --root /noah/dataset/infra-guidance/SUMO/sumo_process/A1 --ckpt_path /noah/ckpt/finetuning/infra_guidance/D3_step1/epoch=23-val_minFDE=0.60.ckpt
python val.py --model QCNet --root /noah/dataset/infra-guidance/SUMO/sumo_process/B1 --ckpt_path /noah/ckpt/finetuning/infra_guidance/D3_step1/epoch=23-val_minFDE=0.60.ckpt
python val.py --model QCNet --root /noah/dataset/infra-guidance/SUMO/sumo_process/D3 --ckpt_path /noah/ckpt/finetuning/infra_guidance/D3_step1/epoch=23-val_minFDE=0.60.ckpt
# python val.py --model QCNet --root /noah/dataset/infra-guidance/SUMO/sumo_process/merge --ckpt_path /noah/ckpt/finetuning/infra_guidance/D3_step1/epoch=23-val_minFDE=0.60.ckpt
#############################################################################################################################################################################################
python val.py --model QCNet --root /noah/dataset/infra-guidance/SUMO/sumo_process/A1 --ckpt_path /noah/ckpt/finetuning/infra_guidance/A1_step5/epoch=69-val_minFDE=1.27.ckpt
python val.py --model QCNet --root /noah/dataset/infra-guidance/SUMO/sumo_process/B1 --ckpt_path /noah/ckpt/finetuning/infra_guidance/A1_step5/epoch=69-val_minFDE=1.27.ckpt
python val.py --model QCNet --root /noah/dataset/infra-guidance/SUMO/sumo_process/D3 --ckpt_path /noah/ckpt/finetuning/infra_guidance/A1_step5/epoch=69-val_minFDE=1.27.ckpt
# python val.py --model QCNet --root /noah/dataset/infra-guidance/SUMO/sumo_process/merge --ckpt_path /noah/ckpt/finetuning/infra_guidance/A1_step1/epoch=64-val_minFDE=0.90.ckpt

python val.py --model QCNet --root /noah/dataset/infra-guidance/SUMO/sumo_process/A1 --ckpt_path /noah/ckpt/finetuning/infra_guidance/B1_step5/epoch=86-val_minFDE=0.86.ckpt
python val.py --model QCNet --root /noah/dataset/infra-guidance/SUMO/sumo_process/B1 --ckpt_path /noah/ckpt/finetuning/infra_guidance/B1_step5/epoch=86-val_minFDE=0.86.ckpt
python val.py --model QCNet --root /noah/dataset/infra-guidance/SUMO/sumo_process/D3 --ckpt_path /noah/ckpt/finetuning/infra_guidance/B1_step5/epoch=86-val_minFDE=0.86.ckpt
# python val.py --model QCNet --root /noah/dataset/infra-guidance/SUMO/sumo_process/merge --ckpt_path /noah/ckpt/finetuning/infra_guidance/B1_step1/epoch=16-val_minFDE=0.53.ckpt

python val.py --model QCNet --root /noah/dataset/infra-guidance/SUMO/sumo_process/A1 --ckpt_path /noah/ckpt/finetuning/infra_guidance/D3_step5/epoch=74-val_minFDE=0.65.ckpt
python val.py --model QCNet --root /noah/dataset/infra-guidance/SUMO/sumo_process/B1 --ckpt_path /noah/ckpt/finetuning/infra_guidance/D3_step5/epoch=74-val_minFDE=0.65.ckpt
python val.py --model QCNet --root /noah/dataset/infra-guidance/SUMO/sumo_process/D3 --ckpt_path /noah/ckpt/finetuning/infra_guidance/D3_step5/epoch=74-val_minFDE=0.65.ckpt
# python val.py --model QCNet --root /noah/dataset/infra-guidance/SUMO/sumo_process/merge --ckpt_path /noah/ckpt/finetuning/infra_guidance/D3_step1/epoch=23-val_minFDE=0.60.ckpt
#############################################################################################################################################################################################

python val.py --model QCNet --root /noah/dataset/infra-guidance/SUMO/sumo_process/A1 --ckpt_path /noah/ckpt/finetuning/infra_guidance/A1_step10/epoch=75-val_minFDE=1.38.ckpt
python val.py --model QCNet --root /noah/dataset/infra-guidance/SUMO/sumo_process/B1 --ckpt_path /noah/ckpt/finetuning/infra_guidance/A1_step10/epoch=75-val_minFDE=1.38.ckpt
python val.py --model QCNet --root /noah/dataset/infra-guidance/SUMO/sumo_process/D3 --ckpt_path /noah/ckpt/finetuning/infra_guidance/A1_step10/epoch=75-val_minFDE=1.38.ckpt
# python val.py --model QCNet --root /noah/dataset/infra-guidance/SUMO/sumo_process/merge --ckpt_path /noah/ckpt/finetuning/infra_guidance/A1_step1/epoch=64-val_minFDE=0.90.ckpt

python val.py --model QCNet --root /noah/dataset/infra-guidance/SUMO/sumo_process/A1 --ckpt_path /noah/ckpt/finetuning/infra_guidance/B1_step10/epoch=87-val_minFDE=0.54.ckpt
python val.py --model QCNet --root /noah/dataset/infra-guidance/SUMO/sumo_process/B1 --ckpt_path /noah/ckpt/finetuning/infra_guidance/B1_step10/epoch=87-val_minFDE=0.54.ckpt
python val.py --model QCNet --root /noah/dataset/infra-guidance/SUMO/sumo_process/D3 --ckpt_path /noah/ckpt/finetuning/infra_guidance/B1_step10/epoch=87-val_minFDE=0.54.ckpt
# python val.py --model QCNet --root /noah/dataset/infra-guidance/SUMO/sumo_process/merge --ckpt_path /noah/ckpt/finetuning/infra_guidance/B1_step1/epoch=16-val_minFDE=0.53.ckpt

python val.py --model QCNet --root /noah/dataset/infra-guidance/SUMO/sumo_process/A1 --ckpt_path /noah/ckpt/finetuning/infra_guidance/D3_step10/epoch=71-val_minFDE=0.85.ckpt
python val.py --model QCNet --root /noah/dataset/infra-guidance/SUMO/sumo_process/B1 --ckpt_path /noah/ckpt/finetuning/infra_guidance/D3_step10/epoch=71-val_minFDE=0.85.ckpt
python val.py --model QCNet --root /noah/dataset/infra-guidance/SUMO/sumo_process/D3 --ckpt_path /noah/ckpt/finetuning/infra_guidance/D3_step10/epoch=71-val_minFDE=0.85.ckpt
# python val.py --model QCNet --root /noah/dataset/infra-guidance/SUMO/sumo_process/merge --ckpt_path /noah/ckpt/finetuning/infra_guidance/D3_step1/epoch=23-val_minFDE=0.60.ckpt


# python val.py --model QCNet --root /noah/dataset/infra-guidance/SUMO/sumo_process/A1 --ckpt_path /noah/ckpt/finetuning/infra_guidance/merge/epoch=60-val_minFDE=0.76.ckpt
# python val.py --model QCNet --root /noah/dataset/infra-guidance/SUMO/sumo_process/B1 --ckpt_path /noah/ckpt/finetuning/infra_guidance/merge/epoch=60-val_minFDE=0.76.ckpt
# python val.py --model QCNet --root /noah/dataset/infra-guidance/SUMO/sumo_process/D3 --ckpt_path /noah/ckpt/finetuning/infra_guidance/merge/epoch=60-val_minFDE=0.76.ckpt
# python val.py --model QCNet --root /noah/dataset/infra-guidance/SUMO/sumo_process/merge --ckpt_path /noah/ckpt/finetuning/infra_guidance/merge/epoch=60-val_minFDE=0.76.ckpt

# test
# python test.py --model QCNet --root /noah/dataset/infra-guidance/SUMO/sumo_process/A1  --ckpt_path /noah/ckpt/finetuning/infra_guidance/A1_step1/epoch=64-val_minFDE=0.90.ckpt

# inference
# python inference.py --model QCNet --root /noah/dataset/infra-guidance/SUMO/A1 --batch_size 1 --ckpt_path /noah/ckpt/finetuning/infra_guidance/A1/epoch\=0-val_minFDE\=6.82.ckpt