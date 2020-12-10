import os, sys
from telethon.sessions import StringSession
from telethon import TelegramClient
from var import Var
os.system("pip install --upgrade pip")

if Var.STRING_SESSION:
    ultroid = TelegramClient(StringSession(Var.STRING_SESSION), Var.APP_ID, Var.API_HASH)
else:
    quit(1)

ENV = os.environ.get("ENV", False)

from logging import basicConfig, getLogger, INFO, DEBUG
from distutils.util import strtobool as sb
import asyncio

from requests import get
if bool(ENV):
    CONSOLE_LOGGER_VERBOSE = sb(os.environ.get("CONSOLE_LOGGER_VERBOSE", "False"))

    if CONSOLE_LOGGER_VERBOSE:
        basicConfig(
            format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            level=DEBUG,
        )
    else:
        basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
                    level=INFO)
    LOGS = getLogger(__name__)
    CONFIG_CHECK = os.environ.get(
        "___________PLOX_______REMOVE_____THIS_____LINE__________", None)

    if CONFIG_CHECK:
        LOGS.info(
            "Please remove the line mentioned in the first hashtag from the config.env file"
        )
        quit(1)
else:
    PLACEHOLDER = None

#



# END OF VARS
