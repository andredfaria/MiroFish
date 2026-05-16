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
    import logging
    logging.basicConfig(level=logging.WARNING)
    log = logging.getLogger('mirofish.wsgi')
    log.warning("Configuração incompleta — a aplicação pode não funcionar corretamente:")
    for err in errors:
        log.warning("  - %s", err)
    log.warning("Defina as variáveis de ambiente no EasyPanel e reinicie o container.")

app = create_app()
