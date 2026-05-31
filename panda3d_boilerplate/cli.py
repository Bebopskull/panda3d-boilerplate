#!/usr/bin/env python3
"""Scaffold a new Panda3D project from the templates/ directory."""

import argparse
import shutil
import sys
from pathlib import Path

PLACEHOLDER = "{{PROJECT_NAME}}"
SUBSTITUTE_EXTENSIONS = {".py", ".md", ".prc", ".sh", ".txt"}
DOTFILE_RENAMES = {"gitignore": ".gitignore", "gitkeep": ".gitkeep"}


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Create a new Panda3D project from this boilerplate.",
    )
    parser.add_argument(
        "target",
        type=Path,
        help="Path where the new project will be created (must not exist).",
    )
    parser.add_argument(
        "name",
        nargs="?",
        default=None,
        help="Display name for the project. Defaults to the target directory name.",
    )
    args = parser.parse_args()

    target: Path = args.target.expanduser().resolve()
    project_name: str = args.name or target.name

    if target.exists():
        print(f"Error: {target} already exists.", file=sys.stderr)
        return 1

    templates_dir = Path(__file__).resolve().parent / "templates"
    if not templates_dir.is_dir():
        print(f"Error: templates/ not found at {templates_dir}", file=sys.stderr)
        return 1

    print(f"Creating Panda3D project '{project_name}' at {target}...")
    shutil.copytree(templates_dir, target)

    for path in target.rglob("*"):
        if path.is_file() and path.suffix in SUBSTITUTE_EXTENSIONS:
            text = path.read_text(encoding="utf-8")
            if PLACEHOLDER in text:
                path.write_text(text.replace(PLACEHOLDER, project_name), encoding="utf-8")

    for path in list(target.rglob("*")):
        if path.is_file() and path.name in DOTFILE_RENAMES:
            path.rename(path.with_name(DOTFILE_RENAMES[path.name]))

    run_sh = target / "run.sh"
    if run_sh.exists():
        run_sh.chmod(0o755)

    print(
        f"\nDone. Next steps:\n\n"
        f"  cd {target}\n"
        f"  python3 -m venv .venv\n"
        f"  source .venv/bin/activate   # Windows: .venv\\Scripts\\activate\n"
        f"  pip install -r requirements.txt\n"
        f"  python src/main.py\n"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
