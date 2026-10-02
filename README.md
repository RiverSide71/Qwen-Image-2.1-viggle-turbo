---
license: other
license_name: qwen-research
license_link: LICENSE
base_model: Qwen/Qwen-Image-2.1
---

# Qwen-Image-2.1-viggle-turbo — v0.2.1

**Built with Qwen.** A few-step distilled version of [Qwen/Qwen-Image-2.1](https://huggingface.co/Qwen/Qwen-Image-2.1)
by Viggle. Text-to-image and instruction-driven editing with 1–3 reference images in **6 steps instead of 40**, with
**no classifier-free guidance**.

| file | |
|---|---|
|Qwen-Image-2.1-viggle-turbo-v0.2.1}-6step-int8_convrot.safetensors |
|ComfyUI custom nodes, text-to-image / edit workflows, example inputs |

## Install

```bash
git clone 


### Rules that matter

* **6 steps with `sigmas=[1.0, 0.9375, 0.875, 0.75, 0.5, 0.25]`, `true_cfg_scale=1.0`, no negative prompt.** These are raw nodes: the pipeline applies its resolution-dependent shift to them, so pass them as written at every size.

* **To change the step count, add or remove steps at the high-noise end only**, and keep `0.875, 0.75, 0.5, 0.25`: 5 steps `[1, 0.875, 0.75, 0.5, 0.25]`, 7 steps `[1, 0.9583, 0.9167, 0.875, 0.75, 0.5, 0.25]`. Moving the low-noise nodes makes images softer; plain `num_inference_steps` without `sigmas=` and CFG do not help.
* Reference order decides which image `image 1` / `image 2` in the prompt refers to. Without `height`/`width`, the output aspect ratio follows the **first**).
* Prompt rewriting with the official [PE-T2I](https://huggingface.co/Qwen/Qwen-Image-2.1-PE-T2I) /
  [PE-I2I](https://huggingface.co/Qwen/Qwen-Image-2.1-PE-I2I) rewriters helps composition and rendered text. Raw prompts work too.
* About 1 MP is the sweet spot; up to about 4 MP works. Keep width and height at multiples of 16.

Tested with ComfyUI 0.37.0 (frontend 1.53.6), which has native Qwen-Image-2.1 support. 

* `Qwen-Image-2.1-viggle-turbo-t2i.json`, `Qwen-Image-2.1-viggle-turbo-edit.json` — the workflows (drag into ComfyUI).
* `input/woman2.webp`, `input/cat.webp` — the edit workflow's example references (from the [black-forest-labs/flux-klein-9b-kv](https://huggingface.co/spaces/black-forest-labs/flux-klein-9b-kv) Space); copy them into `ComfyUI/input/`.

| ComfyUI folder | file | size |
|---|---|---|
| `diffusion_models/` | [`qwen_image_2.1_int8_convrot.safetensors`](https://huggingface.co/Comfy-Org/Qwen-Image-2.1) or `qwen_image_2.1_bf16.safetensors` | 7.3 / 14.2 GB |
| `text_encoders/` | [`qwen3vl_8b_int8_convrot.safetensors`](https://huggingface.co/Comfy-Org/Qwen-Image-2.1) or `qwen3vl_8b_bf16.safetensors` | 9.4 / 17.5 GB |
| `vae/` | [`qwen_image_2.1_vae_bf16.safetensors`](https://huggingface.co/Comfy-Org/Qwen-Image-2.1) | 0.7 GB |


* **Viggle Turbo Sigmas** — the 6-step schedule with the pipeline's resolution-dependent shift. Use it instead of a KSampler scheduler, with euler and `BasicGuider` (no CFG, no negative prompt).
* **Viggle Turbo LoRA (unmerged)** — applies the LoRA at runtime, as diffusers does. The stock LoRA loaders merge it into the weights, which drops about 30% of this adapter's update on bf16 and adds noise on int8. The unmerged node costs 10–25% more time per step. Keep its strength at 1.0.

Full names are `Qwen-Image-2.1-viggle-turbo-v0.2.1

## Known limitations

* **Complicated edits** (multi-reference composition, face swaps, identity-preserving edits, instructions with several constraints) can still fall short of the base model: duplicated or ghosted figures, identity drift.
* **Small or long rendered text** garbles more often than with the base model. 9 steps often helps, not always.
* Colours come out a few percent less saturated than the base model's.
* 2K output, RGBA output, mask-guided edits and edits with more than 3 references are checked only by eye on the Comparison tab examples. No standard benchmark is claimed.

## License

This model is a derivative work of Qwen-Image-2.1 and is distributed under the **Qwen RESEARCH LICENSE AGREEMENT**
([`LICENSE`](LICENSE)): **non-commercial use only** — research or evaluation purposes. Commercial use requires a separate licence from the licensor (`model-business@notice.qwencloud.com`). See [`NOTICE`](NOTICE) for the required
attribution.

Qwen is licensed under the Qwen RESEARCH LICENSE AGREEMENT, Copyright (c) 2026 Hangzhou Tongyi Laboratory Technology Co., Ltd. All Rights Reserved.

Relative to [`Qwen/Qwen-Image-2.1`](https://huggingface.co/Qwen/Qwen-Image-2.1) the Viggle/Qwen-Image-2.1-viggle-turbo repository **adds** LoRA adapters (v0.3, v0.2.1 and v0.2, at rank 256 and 128), single-file transformers (the base transformer with the v0.3 or 0.2.1 adapter merged in, quantized to int8, fp8 or GGUF), ComfyUI nodes, workflows and two example input photos, and a scheduler config with `shift_terminal` changed from `0.02` to `null`. 

This Github repository only reproduces the viggle_turbo.py, writes the __init__.py and organizes the workflows and input images for easy download by ComfyUI users.

Please download the Qwen-Image-2.1-viggle-turbo-v0.2.1-6step-int8_convrot.safetensors file from Viggle Huggingface at: https://huggingface.co/Viggle/Qwen-Image-2.1-viggle-turbo/blob/main/Qwen-Image-2.1-viggle-turbo-v0.2.1-6step-int8_convrot.safetensors

Please see [`NOTICE`](NOTICE)).

Distillation and release by **Viggle**. **Built with Qwen.**
