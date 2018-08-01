from discord.ext import commands

from ticketBot.utils import config_setup

ticket_bot = commands.Bot(command_prefix=config_setup.prefix)

extensions = ['commands.new_command', 'commands.info_command']


@ticket_bot.event
async def on_ready():
    print('Ticket bot loaded')
    print('Name : {}'.format(ticket_bot.user.name))
    print('ID : {}'.format(ticket_bot.user.id))
    print('–––––––––\n')

if __name__ == '__main__':
    ticket_bot.remove_command('help')
    for extension in extensions:
                try:
                    ticket_bot.load_extension(extension)
                except Exception as ex:
                    print("{} cannot be loaded : {}".format(extension.title(), ex))
    ticket_bot.run(config_setup.token)
