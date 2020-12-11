from telethon import events
from ultroid import ultroid

@ultroid.on(events.NewMessage(pattern="^.ping", outgoing=True))
async def _(ult):
    await ult.edit("Pong")
