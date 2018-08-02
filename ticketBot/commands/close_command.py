import discord
from discord.ext import commands


class Close:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def close(self, ctx, *reason):
        """
        Close a ticket
        :param ctx:
        :param user_name:
        :param reason:
        :return:
        """
        if "-ticket" in ctx.message.channel.name:
            await self.bot.delete_channel(ctx.message.channel)

            out = ''
            if len(reason) != 0:
                for word in reason:
                    out += word
                    out += " "
            else:
                out = "No reason"

            close_embed = discord.Embed(title="The ticket as been closed", color=discord.Color.red())

            close_embed.add_field(name="Author", value=ctx.message.author, inline=True)
            close_embed.add_field(name="Reason", value=out)

            close_embed.set_footer(text="Ticket bot", icon_url=self.bot.user.avatar_url)

            await self.bot.send_message(ctx.message.author, embed=close_embed)
        else:
            await self.bot.say("You are not in a ticket channel")


def setup(bot):
    bot.add_cog(Close(bot))
