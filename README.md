# StrongSORT*
**StrongSORT\* Make StrongSORT Usable for Edge AI**

## Abstract

Since the position and the motion of the objects can change during long-term occlusions, ReID features remain a key component for the recent Multiple Object Tracking (MOT) methods. However, the computational cost of feature extraction via Convolutional Neural Networks (CNNs) results in extremely low Frame per Second (FPS) when they are executed on resource-constrained hardware. In this paper, we will introduce a method  that selects the detections that need feature extraction on-the-fly and extracts features from only those detections. We applied our method on StrongSORT to provide an example showcase and discussed the possibility of maintaining the advantages of feature extraction while increasing FPS.

## Data&Model Preparation

1. Download MOT17, MOT20 and DanceTrack and place them as follows: 

   ```
   path_to_dataset/MOTChallenge
   ├── MOT17
   	│   ├── test
   	│   └── train
   └── MOT20
       ├── test
       └── train
   └── dancetrack
       ├── test
       └── train
   ```
Note: Place DanceTrack Validation Set into dancetrack/train 

2. Download official weights and detections (if you wish to test offline) that are shared by authors of StrongSORT from: [data](https://drive.google.com/drive/folders/1Zk6TaSJPbpnqbz1w4kfhkKFCEzQbjfp_?usp=sharing) in Google disk (or [baidu disk](https://pan.baidu.com/s/1EtBbo-12xhjsqW5x-dYX8A?pwd=sort) with code "sort")

Then, download the detections + features for DanceTrack that are extracted by us following the instructions of the authors of StrongSORT from: [Google Drive](
https://drive.google.com/drive/folders/1k9mQWO3RJELN23Zs9jQmko5r8spt_zVP?usp=sharing) 

   ```
   precomputed
   ├── dancetrack_test_YOLOX+BoT  # detections + features
   ├── dancetrack_val_YOLOX+BoT  # detections + features
   ├── MOT17_test_YOLOX+BoT  # detections + features
   ├── MOT17_test_YOLOX+simpleCNN  # detections + features
   ├── MOT17_val_GT_for_TrackEval  # GT to eval the tracking results.
   ├── MOT17_val_YOLOX+BoT  # detections + features
   ├── MOT17_val_YOLOX+simpleCNN  # detections + features
   ├── MOT20_test_YOLOX+BoT  # detections + features
   ├── MOT20_test_YOLOX+simpleCNN  # detections + features
   ```

## Installation 

Follow the exact same installation steps as described in [StrongSORT](https://github.com/dyhBUPT/StrongSORT)

## Tracking


  ```shell
  python strong_sort.py {dataset} {dataset_type} --BoT --ECC --NSA --EMA --MC --woC --ot {th} --{offline} --{display}
  ```

  - th: threshold for Tespitlere Talepler algorithm as described in the paper.
  - offline: uses preextracted features when it is set.
  - display: creates a results folder and saves all annotated frames when it is set.
  - all other arguments are explained in [StrongSORT](https://github.com/dyhBUPT/StrongSORT)
