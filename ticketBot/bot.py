from ticketBot.utils import config_setup
from discord.ext import commands

ticket_bot = commands.Bot(command_prefix=config_setup.prefix)


@ticket_bot.event
async def on_ready():
    print('Ticket bot loaded')
    print('Name : {}'.format(ticket_bot.user.name))
    print('ID : {}'.format(ticket_bot.user.id))
    print('–––––––––\n')

ticket_bot.run(config_setup.token)
