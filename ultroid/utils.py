import sys
import logging
import importlib
from pathlib import Path

def load_plugins(plugin_name):
    if plugin_name.startswith("__"):
        pass
    elif plugin_name.endswith("_"):
        import ultroid.utils
        import importlib
        path = Path(f"ultroid/plugins/{plugin_name}.py")
        name = "ultroid.plugins.{}".format(plugin_name)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        print("Ultroid has (re)Imported " + plugin_name)
    else:
        import ultroid.utils
        import importlib
        path = Path(f"ultroid/plugins/{plugin_name}.py")
        name = "ultroid.plugins.{}".format(plugin_name)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        mod.ultroid = ultroid
