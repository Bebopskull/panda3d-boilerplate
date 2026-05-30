# panda3d-boilerplate

Cross-platform generator for new Panda3D projects.

## Requirements

- Python 3.8+ (anything that runs Panda3D will do)

## Usage

```bash
git clone https://github.com/Bebopskull/panda3d-boilerplate.git
cd panda3d-boilerplate
python create.py /path/to/my-game
```

Optionally pass a display name (defaults to the directory name):

```bash
python create.py /path/to/my-game "My Awesome Game"
```

Works on Linux, macOS, and Windows.

## What it creates

```
my-game/
├── src/
│   ├── main.py              # ShowBase entry point
│   ├── scenes/              # Scene/state system (base + menu example)
│   ├── input/               # Centralized input manager
│   └── utils/logger.py      # Stdout logging
├── assets/
│   ├── models/
│   ├── textures/
│   ├── sounds/
│   ├── fonts/
│   └── shaders/
├── config/config.prc        # Window, audio, model paths
├── tests/
├── requirements.txt         # panda3d
├── .gitignore
├── README.md
└── run.sh                   # Linux/macOS launcher
```

## Next steps after generation

```bash
cd /path/to/my-game
python3 -m venv .venv
source .venv/bin/activate         # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python src/main.py
```
