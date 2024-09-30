import os
from tqdm import tqdm
import pandas as pd
import random
import math

# use_case = ["A1", "B1", "C1", "D3", "D4"]
use_case = ["A1", "B1", "D3"]

for site in use_case:
    obj_dfs = [
                # pd.read_csv('/noah/dataset/infra-guidance/SUMO/sumo_origin/{}/{}_normal_object.csv'.format(site,site)),
                # pd.read_csv('/noah/dataset/infra-guidance/SUMO/sumo_origin/{}/{}_friction_object.csv'.format(site,site)),
                pd.read_csv('/noah/dataset/infra-guidance/SUMO/sumo_origin/{}/{}_tc_object.csv'.format(site,site))
            ]

    track_dfs = [
                    # pd.read_csv('/noah/dataset/infra-guidance/SUMO/sumo_origin/{}/{}_normal_track.csv'.format(site,site)),
                    # pd.read_csv('/noah/dataset/infra-guidance/SUMO/sumo_origin/{}/{}_friction_track.csv'.format(site,site)),
                    pd.read_csv('/noah/dataset/infra-guidance/SUMO/sumo_origin/{}/{}_tc_track.csv'.format(site,site)),
                ]

    combined = {
        'recordingId' : [],
        'trackId' : [],
        'frame' : [],
        'xCenter' : [],
        'yCenter' : [],
        'heading' : [],
        'xVelocity' : [],
        'yVelocity' : [],
        'xAcceleration' : [],
        'LongitudinalManeuver' : [],
        'LateralManeuver' : [],
        'trackLifetime' : [],
        'width' : [],
        'length' : [],
    }

    for idx_df, track_df in enumerate(track_dfs):
        for idx_row, row in tqdm(track_df.iterrows()):
            combined['recordingId'].append(int(idx_df+1))

            if not len(combined['trackId']) or combined['trackId'][-1] != row['ObjectID']:
                track_lift_time = 0
            else:
                track_lift_time = combined['trackLifetime'][-1] + 1

            combined['trackLifetime'].append(int(track_lift_time))

            combined['trackId'].append(int(row['ObjectID']))
            combined['frame'].append(int(row['FrameCounts']-1))
            combined['xCenter'].append(row['DistanceX'])
            combined['yCenter'].append(row['DistanceY'])

            heading = -(row['Heading']-90)
            speed = row['Speed']
            combined['heading'].append(heading)
            combined['xVelocity'].append(speed*math.cos(heading))
            combined['yVelocity'].append(speed*math.sin(heading))
            combined['xAcceleration'].append(row['Acceleration'])

            combined['LongitudinalManeuver'].append(row['LongitudinalManeuver'])
            combined['LateralManeuver'].append(row['LateralManeuver'])

            obj_df = obj_dfs[idx_df]
            obj_info = obj_df[obj_df['objectID']==row['ObjectID']]
            combined['width'] = obj_info['width_size'].values[0]
            combined['length'] = obj_info['length_size'].values[0]

    combined_df = pd.DataFrame(combined)

    test_path = '/noah/dataset/infra-guidance/SUMO/sumo_origin/{}/TEST'.format(site)
    os.makedirs(test_path,exist_ok=True)
    combined_df.to_csv(os.path.join(test_path, 'pp_{}__combined.csv'.format(site)), index=False)

    # unique_recording_ids = set(combined_df['recordingId'])
    # train_dfs = []
    # val_dfs = []
    # ratio = 0.9

    # for recording_id in unique_recording_ids:
    #     unique_combined_df = combined_df[combined_df['recordingId']==recording_id]
    #     object_ids = set(unique_combined_df['trackId'])    
    #     train_object_ids = random.sample(object_ids, int(len(object_ids)*ratio))

    #     train_df = unique_combined_df[unique_combined_df['trackId'].isin(train_object_ids)]
    #     val_df = unique_combined_df[~unique_combined_df['trackId'].isin(train_object_ids)]

    #     train_dfs.append(train_df)
    #     val_dfs.append(val_df)

    # train_dfs = pd.concat(train_dfs, ignore_index=True)
    # val_dfs = pd.concat(val_dfs, ignore_index=True)

    # train_path = '/noah/dataset/infra-guidance/SUMO/sumo_origin/{}/TRAIN'.format(site)
    # val_path = '/noah/dataset/infra-guidance/SUMO/sumo_origin/{}/VALI'.format(site)

    # os.makedirs(train_path,exist_ok=True)
    # os.makedirs(val_path,exist_ok=True)

    # train_dfs.to_csv(os.path.join(train_path, 'pp_{}__combined.csv'.format(site)), index=False)
    # val_dfs.to_csv(os.path.join(val_path, 'pp_{}__combined.csv'.format(site)), index=False)
