import json
import pip_shim as pip
import importlib
import logging

log = logging.getLogger(__name__)

def load_modules_json(data, app):
    modules = json.loads(data)
    if "modules" in modules:
        for module in modules['modules']:
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
