import asyncio,discord
from discord.ext import commands
from ticketBot.utils import config_setup,messages

ticket_bot = commands.Bot(command_prefix=config_setup.prefix)

extensions = ['commands.new_command', 'commands.info_command', 'commands.close_command', 'commands.add_command']

ticket_bot.get_all_channels()


@ticket_bot.event
async def on_ready():
    print('Ticket bot loaded')
    print('Name : {}'.format(ticket_bot.user.name))
    print('ID : {}'.format(ticket_bot.user.id))
    print('–––––––––\n')
    ticket_bot.loop.create_task(change_playing())


async def change_playing():
    while True:
        await ticket_bot.change_presence(game=discord.Game(name=messages.message['status_1']))
        await asyncio.sleep(10)
        await ticket_bot.change_presence(game=discord.Game(name=messages.message['status_2']))
        await asyncio.sleep(10)
        await ticket_bot.change_presence(game=discord.Game(name=messages.message['status_3']))
        await asyncio.sleep(10)

if __name__ == '__main__':
    ticket_bot.remove_command('help')
    for extension in extensions:
                try:
                    ticket_bot.load_extension(extension)
                except Exception as ex:
                    print("{} cannot be loaded : {}".format(extension.title(), ex))
    ticket_bot.run(config_setup.token)
