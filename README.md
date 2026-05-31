# panda3d-boilerplate

Cross-platform generator for new Panda3D projects. Installs as a global `mkpanda` command.

## Install

Requires Python 3.8+ and [pipx](https://pipx.pypa.io/) (recommended) or pip.

```bash
pipx install mkpanda
```

Or directly from GitHub (for the latest unreleased changes on `main`):

```bash
pipx install git+https://github.com/Bebopskull/panda3d-boilerplate.git
```

## Use

```bash
mkpanda /path/to/my-game
```

Optional second argument sets the display name (defaults to the directory name):

```bash
mkpanda /path/to/my-game "My Awesome Game"
```

## Update

```bash
pipx upgrade mkpanda
```

Or to force-reinstall the latest from GitHub (bypasses PyPI cache):

```bash
pipx install --force git+https://github.com/Bebopskull/panda3d-boilerplate.git
```

## Releasing a new version (maintainers)

1. Bump `version` in `pyproject.toml` (SemVer: patch for fixes, minor for features, major for breaking changes).
2. Commit and push to `main`.
3. Build and upload:
   ```bash
   rm -rf dist/ build/
   pyproject-build
   twine upload dist/*
   ```
   (Requires `~/.pypirc` with a PyPI API token. See [pipx docs](https://pipx.pypa.io/) and the [PyPI token guide](https://pypi.org/help/#apitoken).)

## Uninstall

```bash
pipx uninstall mkpanda
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
└── run.sh                   # Linux/macOS launcher
```

## Next steps in the generated project

```bash
cd /path/to/my-game
python3 -m venv .venv
source .venv/bin/activate         # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python src/main.py
```

## Contributing

Open to PRs. The repo layout:

- `panda3d_boilerplate/cli.py` — the `mkpanda` entry point
- `panda3d_boilerplate/templates/` — files copied into new projects (with `{{PROJECT_NAME}}` substitution)
- `pyproject.toml` — packaging metadata; bump `version` for releases

To test changes locally:

```bash
git clone https://github.com/Bebopskull/panda3d-boilerplate.git
cd panda3d-boilerplate
pipx install --force .
mkpanda /tmp/test-project "Test"
```

## License

MIT
