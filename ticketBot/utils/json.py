import json


async def write(channel):
    with open('.storage/tickets.json', 'w') as f:
            json.dump(channel, f)


async def read():
    with open('.storage/tickets.json', 'r') as f:
        channel = json.dump(f)

    return channel