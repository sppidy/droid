import glob
from pathlib import Path
from . import *
import logging

async def start(ult):
    await bot.start(ult)
    ultroid.me = await ultroid.get_me() 
    ultroid.uid = telethon.utils.get_peer_id(ultroid.me)

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)
                    
                    
ultroid.asst = None
print("Initialising...")
if BOT_TOKEN is not None:
    print("Setting up assistant...")
    ultroid.asst = TelegramClient("BOT_TOKEN",api_id=API_ID,api_hash=API_HASH).start(ult=BOT_TOKEN)
    print ("Assistant loaded.")
    print("Starting Ultroid UserBot!")
    ultroid.loop.run_until_complete(start(Var.BOT_USERNAME))
    print("Done, startup completed")
else:
    ultroid.start()

path = "ultroid/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        load_plugins(plugin_name.replace(".py", ""))
    
print("Ultroid has been deployed! Visit @TheUltroid for updates!!")
