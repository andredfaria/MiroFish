"""
MiroFish Backend - WSGI entrypoint for production (gunicorn)
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app import create_app
from app.config import Config

errors = Config.validate()
if errors:
    print("配置错误:")
    for err in errors:
        print(f"  - {err}")
    print("\n请检查 .env 文件中的配置")
    sys.exit(1)

app = create_app()
