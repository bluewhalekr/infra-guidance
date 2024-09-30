import os
import pandas as pd
import shutil
from tqdm import tqdm
from datetime import date

def process_files(folder_path, output_folder, input_frame, output_frame):
    # 파일 처리 함수 호출
    files = os.listdir(folder_path)
    for file_name in tqdm(files, desc="전체 폴더 진행 중"):
        if file_name.endswith('.csv'):
            tracks_file_path = os.path.join(folder_path, file_name)
            process_track_files(tracks_file_path, output_folder, input_frame, output_frame)

def process_track_files(tracks_file_path, output_folder, input_frame, output_frame):
    # 데이터 불러오기
    df = pd.read_csv(tracks_file_path)

    # 열 이름 대체 및 추가
    column_mapping = {
        'trackId': 'track_id',
        'frame': 'timestep',
        'xCenter': 'position_x',
        'yCenter': 'position_y',
        'heading': 'heading',
        'xVelocity': 'velocity_x',
        'yVelocity': 'velocity_y'
    }
    base_scenario_id_str = 10    
    scenario_id_int = int(base_scenario_id_str)  # 기존 숫자 부분을 정수로 변환
    df = df.rename(columns=column_mapping)

    additional_columns = ['observed', 'object_type', 'object_category', 'scenario_id', 'start_timestamp', 'end_timestamp',
                          'num_timestamps', 'focal_track_id', 'city']
    for col in additional_columns:
        df[col] = ""
    df['object_category'] = 0
    df['focal_track_id'] = 0  # 임시
    df['num_timestamps'] = output_frame + input_frame
    df['scenario_id'] = scenario_id_int
    df['start_timestamp'] = 0
    df['end_timestamp'] = 0
    df['city'] = 'kcity'
    df['object_type'] = 'VEHICLE'
    df = df[['recordingId','observed', 'track_id', 'object_type', 'object_category', 'timestep', 'position_x', 'position_y',
             'heading', 'velocity_x', 'velocity_y', 'scenario_id', 'start_timestamp', 'end_timestamp',
             'num_timestamps', 'focal_track_id', 'city']]

    frame_interval = output_frame + input_frame
    unique_recording_ids = list(set(df['recordingId']))
    for recording_id in unique_recording_ids:
        max_frame = df[df['recordingId']==recording_id]['timestep'].max()
        num_files = max_frame - frame_interval + 1

        for i in tqdm(range(0,num_files,frame_interval//2), desc="폴더 내 파일 생성 중"):
            new_scenario_id = f'{base_scenario_id_str}{i:05}'  # 새로운 시나리오 ID 생성

            start_frame = i
            end_frame = i + frame_interval
            df_group = df[(df['recordingId']==recording_id) & (df['timestep'] >= start_frame) & (df['timestep'] < end_frame)]

            if not df_group.empty:
                # timestep 값을 두 자리 숫자로 제한
                df_group['timestep'] = df_group['timestep'] - i
                df_group['observed'] = (df_group['timestep'] <= (input_frame - 1))
                df_group['scenario_id'] = int(new_scenario_id)

                # 새로운 데이터 필터링 단계 추가
                df_group = df_group.groupby('track_id').filter(lambda x: set(range(output_frame + input_frame)).issubset(x['timestep']))

                # velocity_x 및 velocity_y 열의 평균의 절댓값이 0.05보다 작은 행만 유지
                df_group = df_group[(df_group.groupby('track_id')['velocity_x'].transform('mean').abs() > 0) &
                                    (df_group.groupby('track_id')['velocity_y'].transform('mean').abs() > 0)]

                if not df_group.empty:
                    if not set(range(output_frame + input_frame)).issubset(df_group['timestep']):
                        df_group.loc[df_group.index, 'object_category'] = 0
                    else:
                        df_group.loc[df_group.index, 'object_category'] = 3

                    # 에러 처리
                    if ((df_group['timestep'] < 0) | (df_group['timestep'] > (output_frame + input_frame - 1))).any():
                        raise ValueError("Invalid timestep value found.")

                    # 새로운 파일 이름 및 폴더 경로 설정
                    new_file_name = f'scenario_{recording_id}_{new_scenario_id}.csv'
                    new_folder_path = os.path.join(output_folder, f'{recording_id}_{new_scenario_id}')

                    # 폴더 생성
                    if not os.path.exists(new_folder_path):
                        os.makedirs(new_folder_path)

                    # 파일 저장
                    new_file_path = os.path.join(new_folder_path, new_file_name)
                    df_group.to_csv(new_file_path, index=False)
                else:
                    print('error')
            else:
                print('error')

def generate_folder_path(base_folder, input_frame, output_frame):
    # 오늘의 날짜를 문자열로 변환
    today = date.today().strftime("%Y%m%d")
    
    # 파일 경로 생성
    folder_path = os.path.join(base_folder)
    
    return folder_path

def convert_csv_to_parquet(folder_path):
    # 폴더의 모든 하위 폴더를 순회
    for root, dirs, files in os.walk(folder_path):
        for dir_name in dirs:
            subfolder_path = os.path.join(root, dir_name)
            # 하위 폴더 내의 모든 파일을 순회
            for file_name in tqdm(os.listdir(subfolder_path), desc=f"Converting files in {subfolder_path}"):
                if file_name.endswith('.csv'):
                    csv_file_path = os.path.join(subfolder_path, file_name)
                    parquet_file_path = os.path.join(subfolder_path, file_name[:-4] + '.parquet')
                    df = pd.read_csv(csv_file_path)
                    df.to_parquet(parquet_file_path)
                    os.remove(csv_file_path)

# 설정값 정의
input_frame = 10
output_frame = 30  # hz
# use_case = ["A1", "B1", "C1", "D3", "D4"]
use_case = ["A1", "B1", "D3"]
src_path = '/noah/dataset/infra-guidance/SUMO/sumo_origin'
dst_path = '/noah/dataset/infra-guidance/SUMO/sumo_process'

for uc in use_case:
    # train_input_folder = os.path.join(src_path, uc, 'TRAIN')
    # val_input_folder = os.path.join(src_path, uc, 'VALI')
    test_input_folder = os.path.join(src_path, uc, 'TEST')
    
    # 출력 폴더 생성
    # train_output_folder = generate_folder_path(os.path.join(dst_path, '{}/train/raw'.format(uc)), input_frame, output_frame)
    # val_output_folder = generate_folder_path(os.path.join(dst_path, '{}/val/raw'.format(uc)), input_frame, output_frame)
    test_output_folder = generate_folder_path(os.path.join(dst_path, '{}/test/raw'.format(uc)), input_frame, output_frame)

    # 파일 처리 및 CSV -> Parquet 변환
    # process_files(train_input_folder, train_output_folder, input_frame, output_frame)
    # process_files(val_input_folder, val_output_folder, input_frame, output_frame)
    process_files(test_input_folder, test_output_folder, input_frame, output_frame)

    # convert_csv_to_parquet(train_output_folder)
    # convert_csv_to_parquet(val_output_folder)
    convert_csv_to_parquet(test_output_folder)
