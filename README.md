# UNet 3+ Unofficial Pytorch Implementation

This code is Implementation of UNet 3+ in pytorch.

I refered to Tensorflow Implementation of UNet 3+ [github](https://github.com/hamidriasat/UNet-3-Plus).

## UNet 3+: A Full-Scale Connected UNet for Medical Image Segmentation [![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Fhamidriasat%2FUNet-3-Plus&count_bg=%2379C83D&title_bg=%23555555&icon=sega.svg&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://hits.seeyoufarm.com) <a href="/LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="license" /></a>

<!-- https://hits.seeyoufarm.com/ -->

[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/unet-3-a-full-scale-connected-unet-for/medical-image-segmentation-on-lits2017)](https://paperswithcode.com/sota/medical-image-segmentation-on-lits2017?p=unet-3-a-full-scale-connected-unet-for)

`Hit star ⭐ if you find my work useful.`

## Table of Contents

-   [UNet 3+](https://arxiv.org/abs/2004.08790) for Image Segmentation in Pytorch.
    -   [Table of Contents](#table-of-contents)
    -   [Installation](#installation)
    -   [Code Structure](#code-structure)
    -   [Config](#config)
    -   [Data Preparation](#data-preparation)
    -   [Models](#models)
    -   [Training & Evaluation](#training--evaluation)
    -   [Inference Demo](#inference-demo)

## Installation

**Requirements**

-   Python >= 3.10
-   [Pytorch](https://pytorch.org/get-started/locally/) >= 2.2.0
-   CUDA 12.0

This code base is tested against above-mentioned Python and Pytorch versions. But it's expected to work for latest
versions too.

-   Clone code

```
git clone https://github.com/hamidriasat/UNet-3-Plus.git UNet3P
cd UNet3P
```

-   Install other requirements.

```
pip install -r requirements.txt
```

## Code Structure

-   **checkpoint**: Model checkpoint and logs directory
-   **configs**: Configuration file
-   **data**: Dataset files (see [Data Preparation](#data-preparation)) for more details
-   **data_preparation**: For LiTS data preparation and data verification
-   **losses**: Implementations of UNet3+ hybrid loss function and dice coefficient
-   **models**: Unet3+ model files
-   **utils**: Generic utility functions
-   **data_generator.py**: Data generator for training, validation and testing
-   **evaluate.py**: Evaluation script to validate accuracy on trained model
-   **predict.py**: Prediction script used to visualize model output
-   **train.py**: Training script

## Config

Configurations are passed through `yaml` file. For more details on config file read [here](/configs/).

## Data Preparation

-   This code can be used to reproduce UNet3+ paper results
    on [LiTS - Liver Tumor Segmentation Challenge](https://competitions.codalab.org/competitions/15595).
-   You can also use it to train UNet3+ on custom dataset.

For dataset preparation read [here](/data_preparation/README.md).

## Models

This repo contains all three versions of UNet3+.

[//]: # "https://stackoverflow.com/questions/47344571/how-to-draw-checkbox-or-tick-mark-in-github-markdown-table"

| #   |                          Description                          |                  Model Name                   | Training Supported |
| :-- | :-----------------------------------------------------------: | :-------------------------------------------: | :----------------: |
| 1   |                       UNet3+ Base model                       |       [unet3plus](/models/unet3plus.py)       |      &check;       |
| 2   |                 UNet3+ with Deep Supervision                  |   [unet3plus_deepsup](/models/unet3plus.py)   |      &check;       |
| 3   | UNet3+ with Deep Supervision and Classification Guided Module | [unet3plus_deepsup_cgm](/models/unet3plus.py) |      &cross;       |

Here is a sample code for UNet 3+

```python
INPUT_SHAPE = [1, 320, 320]
OUTPUT_CHANNELS = 1

unet_3P = UNet3Plus(INPUT_SHAPE, OUTPUT_CHANNELS, deep_supervision=False, CGM=False)
unet_3P_deep_sup = UNet3Plus(INPUT_SHAPE, OUTPUT_CHANNELS, deep_supervision=True, CGM=False)
unet_3P_deep_sup_cgm = UNet3Plus(INPUT_SHAPE, OUTPUT_CHANNELS, deep_supervision=True, CGM=True)
```

[Here](/losses/unet_loss.py) you can find UNet3+ hybrid loss.

### Training

To train a model call `train.py` with required model type and configurations .

e.g. To train on base model run

```
python train.py MODEL.TYPE=unet3plus
```

### Inference Demo

For visualization two options are available

1. [Visualize from directory](#visualize-from-directory)
2. [Visualize from list](#visualize-from-list)

In both cases mask is optional

You can also override these settings through command line and call `predict.py`

1. **_Visualize from directory_**

In case of visualization from directory, it's going to make prediction and show all images from given directory.
Override the validation data paths and make sure the directory paths are relative to the project base/root path e.g.

```
python predict.py MODEL.TYPE=unet3plus ^
DATASET.VAL.IMAGES_PATH=/data/val/images/ ^
DATASET.VAL.MASK_PATH=/data/val/mask/
```

2. **_Visualize from list_**

In case of visualization from list, each list element should contain absolute path of image/mask. For absolute paths
training data naming convention does not matter you can pass whatever naming convention you have, just make sure images,
and it's corresponding mask are on same index.

e.g. To visualize model results on two images along with their corresponding mask, run

```
python predict.py MODEL.TYPE=unet3plus ^
DATASET.VAL.IMAGES_PATH=[^
H:\\Projects\\UNet3P\\data\\val\images\\image_0_48.png,^
H:\\Projects\\UNet3P\\data\\val\images\\image_0_21.png^
] DATASET.VAL.MASK_PATH=[^
H:\\Projects\\UNet3P\\data\\val\\mask\\mask_0_48.png,^
H:\\Projects\\UNet3P\\data\\val\\mask\\mask_0_21.png^
]
```

For your own data visualization set `SHOW_CENTER_CHANNEL_IMAGE=False`. This should set True for only UNet3+ LiTS data.

These commands are tested on Windows. For Linux replace `^` with \ and replace `H:\\Projects` with your own base path

> Note: Don't add space between list elements, it will create problem with Hydra.

In both cases if mask is not available just set the mask path to None

```
python predict.py DATASET.VAL.IMAGES_PATH=... DATASET.VAL.MASK_PATH=None
```

> This branch is in development mode. So changes are expected.

TODO List

-   [x] Complete README.md
-   [x] Add requirements file
-   [ ] Add Data augmentation
-   [x] Add multiprocessing in LiTS data preprocessing
-   [ ] Load data through NVIDIA DALI

We appreciate any feedback so reporting problems, and asking questions are welcomed here.

Licensed under [MIT License](LICENSE)

## Acknowledgement

-   [UNet 3+: A Full-Scale Connected UNet for Medical Image Segmentation](https://arxiv.org/abs/2004.08790)
