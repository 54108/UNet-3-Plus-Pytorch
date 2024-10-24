"""
Returns Unet3+ model
"""
from omegaconf import DictConfig

from .unet3plus import UNet3Plus, UNet3Plus_modified


def prepare_model(cfg: DictConfig, training=False):
    """
    Creates and return model object based on given model type.
    """

    input_shape = [cfg.INPUT.CHANNELS, cfg.INPUT.HEIGHT, cfg.INPUT.WIDTH]

    if cfg.MODEL.TYPE == "unet3plus_modified":
        return UNet3Plus_modified(
            input_shape,
            cfg.OUTPUT.CLASSES + 1,
            False,
            False,
            training,
        )
    elif cfg.MODEL.TYPE == "unet3plus":
        #  training parameter does not matter in this case
        return UNet3Plus(
            input_shape,
            cfg.OUTPUT.CLASSES + 1,
            False,
            False,
            training,
        )
    elif cfg.MODEL.TYPE == "unet3plus_deepsup":
        return UNet3Plus(
            input_shape,
            cfg.OUTPUT.CLASSES + 1,
            True,
            False,
            training
        )
    elif cfg.MODEL.TYPE == "unet3plus_deepsup_cgm":
        if cfg.OUTPUT.CLASSES != 1:
            raise ValueError(
                "UNet3+ with Deep Supervision and Classification Guided Module"
                "\nOnly works when model output classes are equal to 1"
            )
        return UNet3Plus(
            input_shape,
            cfg.OUTPUT.CLASSES + 1,
            True,
            True,
            training
        )
    else:
        raise ValueError(
            "Wrong model type passed."
            "\nPlease check config file for possible options."
        )
