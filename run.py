# from sru.support.module_load import load_modules_json

import os, sys
path = os.path.dirname(__file__)
json_file = os.path.join(path, "modules.json")
# with open(json_file, 'r') as f:
#     json_content = f.read()
#     load_modules_json(json_content)
import sru.support.service

from sru.main import run

run(modules=json_file)