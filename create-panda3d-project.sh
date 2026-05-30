#!/usr/bin/env bash
set -euo pipefail

if [ $# -lt 1 ]; then
    echo "Usage: $0 <project-path> [project-name]"
    echo "Example: $0 ~/projects/my-game"
    echo "         $0 ~/projects/my-game \"My Awesome Game\""
    exit 1
fi

TARGET="$1"
PROJECT_NAME="${2:-$(basename "$TARGET")}"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

if [ -e "$TARGET" ]; then
    echo "Error: $TARGET already exists"
    exit 1
fi

echo "Creating Panda3D project '$PROJECT_NAME' at $TARGET..."

mkdir -p "$TARGET"
cp -r "$SCRIPT_DIR/templates/." "$TARGET/"

find "$TARGET" -type f \( -name "*.py" -o -name "*.md" -o -name "*.prc" -o -name "*.sh" -o -name "*.txt" \) \
    -exec sed -i "s/{{PROJECT_NAME}}/$PROJECT_NAME/g" {} +

chmod +x "$TARGET/run.sh"

cat <<EOF

Done. Next steps:

  cd $TARGET
  python3 -m venv .venv
  source .venv/bin/activate
  pip install -r requirements.txt
  ./run.sh

EOF
