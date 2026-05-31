# {{PROJECT_NAME}}

Panda3D project.

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run

```bash
./run.sh
```

## Structure

- `src/` — application code
  - `main.py` — entry point, ShowBase subclass
  - `scenes/` — scene/state management (FSM)
  - `input/` — centralized input handling
  - `utils/` — logging and helpers
- `assets/` — models, textures, sounds, fonts, shaders
- `config/config.prc` — Panda3D config (window, audio, model paths)
- `tests/` — pytest tests
