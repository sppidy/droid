from telethon import events

@ultroid.on(events.NewMessage(pattern="^.ping", outgoing=True))
async def _(ult):
    await ult.edit("Pong")
