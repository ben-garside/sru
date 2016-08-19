import json
import pip_shim as pip
import importlib
import logging
import os

log = logging.getLogger(__name__)

def load_modules_json(ROOT, app):
    modules = os.path.join(ROOT, "modules.json")
    default_modules = os.path.join(ROOT, "default_modules.json")
    mod_file = None
    if os.path.isfile(modules):
        mod_file = modules
    elif os.path.isfile(default_modules):
        mod_file = default_modules
    
    if mod_file:
        with open(mod_file, "r") as f:
            data = f.read()
            json_data = json.loads(data)
            if "modules" in json_data:
                for module in json_data['modules']:
                    module["safe_name"] = module["name"].replace("_", "-")

                    package = pip.get_by_name(module["name"])
                    if package:
                        mod = importlib.import_module(package["safe_name"])
                        setup = getattr(mod, "setup")
                        setup(app)
                        print("Loading: ", module['safe_name'], module['version'], module['link'])
                        # load the setup method
                    else:
                        result = pip.install(module["link"])
                        print("Unable to load: ", module['safe_name'], module['version'], module['link'])
                        # try install it
                        # then load setup method
