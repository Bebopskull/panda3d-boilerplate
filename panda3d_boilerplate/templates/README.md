# {{PROJECT_NAME}}

Panda3D project.

## Prerequisites

Panda3D installed on your system. Install with `pip install --user panda3d` (or via your distro package, pyenv, or conda environment). Verify with:

```bash
python -c "import panda3d; print(panda3d.__version__)"
```

## Setup

The venv is created with `--system-site-packages` so it inherits the system-installed Panda3D — no re-download per project.

Linux / macOS:
```bash
python3 -m venv --system-site-packages .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Windows:
```cmd
python -m venv --system-site-packages .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## Run

Linux / macOS:
```bash
./run.sh
```

Windows:
```cmd
run.bat
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
