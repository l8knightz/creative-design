# Creative Designs — OpenAI + Gradio

Generate campaign-ready visuals from text prompts using OpenAI and a Gradio web UI.  
Supports two engines:
1) **SVG via GPT-4o-mini** 
2) **Photoreal via gpt-image-1** (requires org verification)

---

## Features
- Text prompt → image workflow in a simple browser UI
- Style presets (cinematic, vector, watercolor, etc.)
- Multiple canvas sizes (square/portrait/landscape)
- SVG mode (fast, no image endpoint) and Photoreal mode (image endpoint)
- Dockerized for consistent, reproducible runs

---

## Quick Start (Docker)

```bash
git clone https://github.com/l8knightz/creative-design.git
cd creative-design
```
# 1) Configure secrets (never commit your real key)
cp env.example .env
# then edit .env and set:
#   OPENAI_API_KEY=sk-...

```
OPENAI_API_KEY=sk-...        # required
GRADIO_SERVER_NAME=0.0.0.0   # optional (default 0.0.0.0)
GRADIO_SERVER_PORT=7860      # optional (default 7860)
```

# 2) Build + run
docker compose build
docker compose up -d
# open http://localhost:7860


## Usage

Choose Generation engine:

SVG via GPT-4o-mini (no verification)
Photoreal via gpt-image-1 (requires verification)
Enter Prompt, pick a Style and Size, optionally add a Negative prompt.
Click Generate.

## Prompt tips

Cinematic poster:
Bold sci-fi poster: neon skyline, rain, reflective streets, dramatic portrait lighting
Style: cinematic • Negative: low-res, text artifacts

Minimal vector banner:
Minimalist vector banner, red/black palette, strong diagonal composition, high contrast, clean shapes
Style: vector • Negative: gradients, photo texture

## Project Structure:
```
creative-design
├─ app.py                 # Gradio app (SVG + Photoreal engines)
├─ requirements.txt
├─ Dockerfile
├─ docker-compose.yml
├─ env.example
├─ .gitignore
└─ README.md
```

## Troubleshooting

403 on Photoreal: Your org must be verified for gpt-image-1. Either verify or set ENABLE_PHOTOREAL=0.
401 Unauthorized: Check OPENAI_API_KEY in .env.
Port in use: Change GRADIO_SERVER_PORT and re-run.
Windows line endings: If Dockerfile parse errors occur, normalize line endings on Linux: sed -i 's/\r$//' Dockerfile.