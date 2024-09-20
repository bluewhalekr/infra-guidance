# train
# python train_qcnet.py --root /noah/dataset/infra-guidance/SUMO/A1 --ckpt_path /noah/ckpt/finetuning/infra_guidance/A1 --train_batch_size 1 --val_batch_size 1 --test_batch_size 1 --num_workers 2 --devices 1 --dataset argoverse_v2 --num_historical_steps 10 --num_future_steps 30 --num_recurrent_steps 3 --pl2pl_radius 150 --pl2a_radius 50 --a2a_radius 50 --num_t2m_steps 30 --pl2m_radius 150 --a2m_radius 150

# val
# python val.py --model QCNet --root /noah/dataset/infra-guidance/SUMO/A1 --ckpt_path /noah/ckpt/finetuning/infra_guidance/A1/epoch=0-val_minFDE=6.82.ckpt

# inference
python inference.py --model QCNet --root /noah/dataset/infra-guidance/SUMO/A1 --batch_size 1 --ckpt_path /noah/ckpt/finetuning/infra_guidance/A1/epoch\=0-val_minFDE\=6.82.ckpt