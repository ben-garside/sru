from aiohttp import web
from sru.conf import settings
from sru.support.ssl_process import ssl_context
# from sru import routes
import logging
import sru_pkgmgr as pkgmgr


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
    load_modules_json(pkgmgr.ROOT, app)

    # end load
    if ssl_cert and ssl_key:
        if ssl_cert != "None" and ssl_key != "None":
            sslContext = ssl_context(ssl_cert=ssl_cert, ssl_key=ssl_key)
            web.run_app(app, ssl_context=settings.sslContext, port=port, host=host)
    else:
        web.run_app(app, port=port, host=host)
