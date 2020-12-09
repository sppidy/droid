import glob
from pathlib import Path
from ultroid import ultroid
from ultroid.utils import load_plugins
import logging

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

path = "ultroid/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        load_plugins(plugin_name.replace(".py", ""))
    
print("Successfully deployed Ultroid!")

if __name__ == "__main__":
    ultroid.run_until_disconnected()
