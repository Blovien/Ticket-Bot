import discord
from discord.ext import commands
from utils.messages import message


class Info:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def info(self, ctx):

        """
        info about the bot
        :param ctx:
        :return:
        """
        """
        Info embed
        """

        info_embed = discord.Embed(title='Info', description=message['info'], color=discord.Color.gold())
        info_embed.set_footer(text="Ticket bot")
        await self.bot.say(embed=info_embed)

    @commands.command(pass_context=True)
    async def help(self):
        """
        info about the bot
        :param ctx:
        :return:
        """
        """
        Info embed
        """
        help_embed = discord.Embed(title='Help', description=message['help'], color=discord.Color.gold())
        help_embed.set_footer(text="Ticket bot")
        await self.bot.say(embed=help_embed)


def setup(bot):
    bot.add_cog(Info(bot))
