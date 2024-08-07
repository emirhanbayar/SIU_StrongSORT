# StrongSORT*
**StrongSORT\* Make StrongSORT Usable for Edge AI**

original implementation of [![IEEE Xplore](https://img.shields.io/badge/IEEE%20Xplore-10600800-00629B.svg)](https://ieeexplore.ieee.org/document/10600800)

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

## Analysis on Validation Sets

<p align="center">
  <img src="https://emirhanbayar.github.io/SIU_images/image1.png" width="44.5%" />
  <img src="https://emirhanbayar.github.io/SIU_images/image2.png" width="45%" />
</p>
<p align="center">
  <img src="https://emirhanbayar.github.io/SIU_images/image3.png" width="45%" />
  <img src="https://emirhanbayar.github.io/SIU_images/image4.png" width="45%" />
</p>

## Results on Test Sets

<p align="center">
  <img src="https://emirhanbayar.github.io/SIU_images/image5.png" width="90%" />
</p>
