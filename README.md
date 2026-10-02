---
license: other
license_name: qwen-research
license_link: LICENSE
base_model: Qwen/Qwen-Image-2.1
---

# Qwen-Image-2.1-viggle-turbo — v0.2.1

**Built with Qwen.** A few-step distilled version of [Qwen/Qwen-Image-2.1](https://huggingface.co/Qwen/Qwen-Image-2.1) by Viggle. Text-to-image and instruction-driven editing with 1–3 reference images in **6 steps instead of 40**, with **no classifier-free guidance**.

| File | Description |
|---|---|
| `Qwen-Image-2.1-viggle-turbo-v0.2.1-6step-int8_convrot.safetensors` | Model weights file |
| `viggle_turbo.py` and `__init__.py` custom nodes, t2i / edit workflows, example inputs | Additional pipeline components |

## Install

```bash
git clone https://github.com/RiverSide71/Qwen-Image-2.1-viggle-turbo.git
```
Restart ComfyUI

### Rules that matter

* **6 steps with `sigmas=[1.0, 0.9375, 0.875, 0.75, 0.5, 0.25]`, `true_cfg_scale=1.0`, no negative prompt.** These are raw nodes: the pipeline applies its resolution-dependent shift to them, so pass them as written at every size.
* **To change the step count, add or remove steps at the high-noise end only**, and keep `0.875, 0.75, 0.5, 0.25`: 
  * 5 steps: `[1, 0.875, 0.75, 0.5, 0.25]`
  * 7 steps: `[1, 0.9583, 0.9167, 0.875, 0.75, 0.5, 0.25]`
  * *Note:* Moving the low-noise nodes makes images softer; plain `num_inference_steps` without `sigmas=` and CFG do not help.
* Reference order decides which image `image 1` / `image 2` in the prompt refers to. Without explicit `height`/`width` parameters, the output aspect ratio follows the **first** reference image.
* Prompt rewriting with the official [PE-T2I](https://huggingface.co/Qwen/Qwen-Image-2.1-PE-T2I) / [PE-I2I](https://huggingface.co/Qwen/Qwen-Image-2.1-PE-I2I) rewriters helps composition and rendered text. Raw prompts work too.
* About 1 MP is the sweet spot; up to about 4 MP works. Keep width and height at multiples of 16.

Tested with ComfyUI 0.37.0 (frontend 1.53.6), which has native Qwen-Image-2.1 support. 

### Included Resources
* `viggle_turbo.py`, `init__.py`
* `Qwen-Image-2.1-viggle-turbo-t2i.json`, `Qwen-Image-2.1-viggle-turbo-edit.json` - the workflows (drag into ComfyUI).
* `input/woman2.webp`, `input/cat.webp` - the edit workflow's example references (from `black-forest-labs/flux`).
