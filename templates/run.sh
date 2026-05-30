#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
PYTHONPATH=src python3 src/main.py
