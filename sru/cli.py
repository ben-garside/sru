from optparse import OptionParser
from aiohttp import web
from sru.main import run
from sru.conf import settings

if __name__ == "__main__":
    parse = OptionParser()

    parse.add_option("-H",  "--host", dest='host', help="server host", default=settings.host)
    parse.add_option("-p",  "--port", dest='port', help="server port", default=settings.port)
    parse.add_option("-c",  "--cert", dest='cert', help="SSL Certificate", default=None)
    parse.add_option("-k",  "--key", dest='key', help="SSL Key", default=None)
    parse.add_option("-m",  "--modules", dest='modules', help="modules to install", default=None)

    (options, args) = parse.parse_args()

    HOST = options.host
    PORT = options.port
    SSL_Cert = options.cert
    SSL_Key = options.key
    MODULES = options.modules


    run(host=HOST, port=PORT, ssl_cert=SSL_Cert, ssl_key=SSL_Key, modules=MODULES)