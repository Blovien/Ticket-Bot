import discord
from discord.ext import commands
from discord import Embed


class new:
    """
    Cog for "new" command
    """
    def __init__(self, ticket_bot):
        self.ticket_bot = ticket_bot

    @commands.command(pass_context=True)
    async def new(self, ctx):
        """
        Create channel named : nickname-ticket(-001 ? maybe i'll add it)
        :param ctx:
        :return:
        """
        embed = Embed(title='Ticket created', description='You created the ')


def setup(ticket_bot):
    ticket_bot.add_cog(new(ticket_bot))


