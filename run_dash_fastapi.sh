#!/usr/bin/env bash
set -euo pipefail

python3 -m pip install -r requirements.txt
python3 -m uvicorn dash_fastapi_app:fastapi_app --reload
