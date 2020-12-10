import sys
import logging
import importlib
from pathlib import Path

def load_plugins(plugin_name):
    from ultroid import ultroid
    path = Path(f"ultroid/plugins/{plugin_name}.py")
    name = "ultroid.plugins.{}".format(plugin_name)
    spec = importlib.util.spec_from_file_location(name, path)
    load = importlib.util.module_from_spec(spec)
    load.logger = logging.getLogger(plugin_name)
    spec.loader.exec_module(load)
    sys.modules["ultroid.plugins." + plugin_name] = load
    print("Ultroid has Imported " + plugin_name)
    mod.ultroid = ultroid
