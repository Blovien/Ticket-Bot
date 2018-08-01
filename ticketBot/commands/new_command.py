import discord
from discord.ext import commands
from ticketBot.utils import config_setup, messages


class New:
    """
    Cog for "new" command
    """

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def new(self, ctx):
        """
        Create channel named : nickname-ticket(-001 ? maybe i'll add it)
        :param ctx:
        :return:
        """

        if ctx.message.channel.id == config_setup.ticket_channel:
            """
            Create "ticket created" embed
            """
            ticket_embed = discord.Embed(title='Ticked created',
                                         description=':white_check_mark:  You created a ticket now you can go to {}'.format(
                                             "#" + ctx.message.author.name + "-ticket"), color=discord.Color.green())
            ticket_embed.set_footer(text='Ticket bot')
            ticket_embed.set_thumbnail(url=ctx.message.author.avatar_url)
            await self.bot.say(embed=ticket_embed)
            await self.bot.create_channel(ctx.message.server, ctx.message.author.name + "-ticket")

            print("New ticket created by " + ctx.message.author.name)
        else:
            await self.bot.say(messages.message['not_in_channel'])


def setup(bot):
    bot.add_cog(New(bot))
