# Creative Designs — OpenAI + Gradio

Generate campaign-ready visuals from text prompts using OpenAI and a Gradio web UI.  Very simple approach, working on a few enhancements but a great foundation to play with. 

---

## Features
- Text prompt → image workflow in a simple browser UI
- Style presets (cinematic, vector, watercolor, etc.)
- Multiple canvas sizes (square/portrait/landscape)
- Dockerized for consistent, reproducible runs

---

## Quick Start (Docker)

```bash
git clone https://github.com/l8knightz/creative-design.git
cd creative-design
```
## 1) Configure secrets (never commit your real key)
cp env.example .env
## then edit .env and set:
   OPENAI_API_KEY=sk-...
```
OPENAI_API_KEY=sk-...        # required
GRADIO_SERVER_NAME=0.0.0.0   # optional (default 0.0.0.0)
GRADIO_SERVER_PORT=7860      # optional (default 7860)
```

## 2) Build + run
```
docker compose build
docker compose up -d
```
## open http://localhost:7860

## Usage

* Enter Prompt
* pick a Style and Size
* optionally add a Negative prompt
* Click Submit

Generated image will appear to the right and also include a download link (&darr;)

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
├─ app.py                 # Gradio app 
├─ requirements.txt
├─ Dockerfile
├─ docker-compose.yml
├─ env.example
├─ .gitignore
└─ README.md
```

## Troubleshooting

403 on Photoreal: Your org must be verified for gpt-image-1.

401 Unauthorized: Check OPENAI_API_KEY in .env.

Port in use: Change GRADIO_SERVER_PORT and re-run.

Windows line endings: If Dockerfile parse errors occur, normalize line endings on Linux: sed -i 's/\r$//' Dockerfile.