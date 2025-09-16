import os
import io
import base64
from typing import Optional

import gradio as gr
from PIL import Image
from openai import OpenAI

client = OpenAI()

SIZE_MAP = {
    "Square (1024×1024)": "1024x1024",
    "Portrait (1024×1344)": "1024x1344",
    "Landscape (1344×1024)": "1344x1024",
}

STYLE_PRESETS = [
    "cinematic", "photorealistic", "vector", "flat illustration",
    "watercolor", "oil painting", "poster / banner", "pixel art",
]

def build_prompt(base_prompt: str, style: str, negative: Optional[str]) -> str:
    parts = [base_prompt.strip()]
    if style:
        parts.append(f"Style: {style}")
    if negative and negative.strip():
        parts.append(f"Negative prompt: {negative.strip()}")
    return "\n".join(parts)

def generate_image(
    base_prompt: str,
    style: str,
    size_label: str,
    negative_prompt: Optional[str],
):
    if not base_prompt or not base_prompt.strip():
        raise gr.Error("Please enter a prompt.")

    size = SIZE_MAP.get(size_label, "1024x1024")
    full_prompt = build_prompt(base_prompt, style, negative_prompt)

    try:
        resp = client.images.generate(
            model="gpt-image-1",
            prompt=full_prompt,
            size=size,
            # Note: Removed seeding, wasn't working no longer supported by the Images API
        )
    except Exception as e:
        raise gr.Error(f"Image generation failed: {e}")

    try:
        b64 = resp.data[0].b64_json
        img_bytes = base64.b64decode(b64)
        img = Image.open(io.BytesIO(img_bytes)).convert("RGBA")
    except Exception as e:
        raise gr.Error(f"Failed to decode image: {e}")

    return img

demo = gr.Interface(
    fn=generate_image,
    inputs=[
        gr.Textbox(
            label="Prompt",
            placeholder="e.g., Bold Netflix sci-fi poster: neon skyline, rain, reflective streets, dramatic lighting",
            lines=4,
        ),
        gr.Dropdown(choices=STYLE_PRESETS, value="cinematic", label="Style"),
        gr.Dropdown(choices=list(SIZE_MAP.keys()), value="Square (1024×1024)", label="Size"),
        gr.Textbox(label="Negative prompt (optional)", placeholder="e.g., low-res, text artifacts, extra fingers"),
    ],
    outputs=gr.Image(type="pil", label="Generated Image"),
    title="Creative Designs — OpenAI + Gradio",
    description="Enter a prompt and optionally set style/size and a negative prompt, then Generate.",
)

if __name__ == "__main__":
    demo.launch(
        server_name=os.getenv("GRADIO_SERVER_NAME", "0.0.0.0"),
        server_port=int(os.getenv("GRADIO_SERVER_PORT", "7860")),
        show_error=True,
    )
