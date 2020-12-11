from telethon import events

@ultroid.on(events.NewMessage(pattern="^.alive")
async def lol(event):
    await event.edit("`Ultroid is OnLine xD`\nVersion - __0.0.1__")
