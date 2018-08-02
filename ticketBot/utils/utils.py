async def is_channel_already_exist(name:str, ctx):
    for channel in ctx.message.server.channels:
        if channel.name == name:
            return True
