# panda3d-boilerplate

Generator script for new Panda3D projects.

## Usage

```bash
./create-panda3d-project.sh /path/to/my-game
```

Optionally pass a custom project name (defaults to the directory name):

```bash
./create-panda3d-project.sh /path/to/my-game "My Awesome Game"
```

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
└── run.sh
```

## Next steps after generation

```bash
cd /path/to/my-game
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
./run.sh
```
