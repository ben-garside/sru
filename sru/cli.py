from optparse import OptionParser
from aiohttp import web
from sru.main import run
from sru.conf import settings

parser = OptionParser()

parser.add_option("-H",  "--host", dest='host', help="server host", default=settings.host)
parser.add_option("-p",  "--port", dest='port', help="server port", default=settings.port)
parser.add_option("-c",  "--cert", dest='cert', help="SSL Certificate", default=None)
parser.add_option("-k",  "--key", dest='key', help="SSL Key", default=None)
parser.add_option("-m",  "--modules", dest='modules', help="modules to install", default=None)

(options, args) = parser.parse_args()

HOST = options.host
PORT = options.port
SSL_Cert = options.cert
SSL_Key = options.key
MODULES = options.modules


run(host=HOST, port=PORT, ssl_cert=SSL_Cert, ssl_key=SSL_Key, modules=MODULES)