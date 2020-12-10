# we save the vars here // remove this line later
import os

ENV = bool(os.environ.get("ENV", False))


class Var(object):
    APP_ID = int(os.environ.get("APP_ID", 9))
    # 9 is a placeholder
    API_HASH = os.environ.get("API_HASH", "eb06d4abfb49dc3eeb1aeb98ae0f581e")
    STRING_SESSION = os.environ.get("STRING_SESSION", None)
