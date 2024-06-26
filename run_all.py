import os
import numpy as np

datasets = ["MOT17"]
dataset_types = ["val"]
occlusion_thresholds = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 1.0]

for dataset in datasets:
    for dataset_type in dataset_types:
        for th in occlusion_thresholds:
            # python strong_sort.py MOT17 val --BoT --ECC --NSA --EMA --MC --woC --display -pt 0.0
            if dataset == "dancetrack":
                os.system(f"python strong_sort.py {dataset} {dataset_type} --BoT --ECC --NSA --EMA --MC --woC --ot {th} --display")
            else:
                os.system(f"python strong_sort.py {dataset} {dataset_type} --BoT --ECC --NSA --EMA --MC --woC --ot {th} --offline --display")
