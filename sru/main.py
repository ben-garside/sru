from aiohttp import web
from sru.conf import settings
from sru.support.ssl_process import ssl_context
# from sru import routes
import logging


logger = logging.getLogger(__name__)


# Istantiate application
app = web.Application()

# Load routes
from sru.support.module_load import load_modules_json
# from sru_pip import setup
# setup(app)
# from sru.helpers.load_modules import load_default_modules
# load_default_modules(app)
# routes.setup(app)

# Run application
def run(host=settings.host, port=settings.port, ssl_cert=None, ssl_key=None, modules=None):
    # load modules
    # import os
    # path = os.path.dirname(__file__)
    # json_file = os.path.join(path, "modules.json")
    with open(modules, 'r') as f:
        json_content = f.read()
        load_modules_json(json_content, app)

    # end load
    if ssl_cert and ssl_key:
        sslContext = ssl_context(ssl_cert=ssl_cert, ssl_key=ssl_key)
        web.run_app(app, ssl_context=settings.sslContext, port=port, host=host)
    else:
        web.run_app(app, port=port, host=host)
