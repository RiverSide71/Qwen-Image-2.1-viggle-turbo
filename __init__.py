from .viggle_turbo import ViggleTurboSigmas, ViggleTurboLora

NODE_CLASS_MAPPINGS = {
    "ViggleTurboSigmas": ViggleTurboSigmas,
    "ViggleTurboLora": ViggleTurboLora,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ViggleTurboSigmas": "Qwen-Image-2.1 Viggle Turbo Sigmas",
    "ViggleTurboLora": "Qwen-Image-2.1 Viggle Turbo LoRA (unmerged)",
}

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]