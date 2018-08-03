import discord
from discord.ext import commands
from utils import config_setup, messages, utils

class New:
    """
    Cog for "new" command
    """

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def new(self, ctx, *phrase):
        """
        Create channel named : nickname-ticket(-001 ? maybe i'll add it)
        :param ctx:
        :return:
        """

        author = ctx.message.author

        if ctx.message.channel.id == config_setup.ticket_channel:
            for channel in ctx.message.server.channels:
                if channel.name == '{}-ticket'.format(ctx.message.author.name).lower():
                    await self.bot.say("You have already created a ticket")
                    return None


            """
            Create "ticket created" embed
            """
            ticket_embed = discord.Embed(title='Ticked created',
                                         description=':white_check_mark:  You created a ticket now you can go to {}'.format(
                                             "#" + ctx.message.author.name + "-ticket"), color=discord.Color.green())
            ticket_embed.set_footer(text='Ticket bot', icon_url=self.bot.user.avatar_url)
            ticket_embed.set_thumbnail(url=ctx.message.author.avatar_url)
            await self.bot.say(embed=ticket_embed)

            out = ''
            if len(phrase) != 0:
                for word in phrase:
                    out += word
                    out += " "
            else:
                out = "No subject"

            dear_embed = discord.Embed(description="You created the ticket now you can talk with our support",
                                       color=discord.Color.green())
            dear_embed.add_field(name="Author", value=ctx.message.author.mention, inline=True)
            dear_embed.add_field(name="Subject", value=out, inline=True)
            dear_embed.set_thumbnail(url=ctx.message.author.avatar_url)
            dear_embed.set_footer(text="Ticket bot", icon_url=self.bot.user.avatar_url)

            everyone_perms = discord.PermissionOverwrite(read_messages=False)
            support_perms = discord.PermissionOverwrite(read_messages=True)
            my_perms = discord.PermissionOverwrite(read_messages=True)

            everyone = discord.ChannelPermissions(target=ctx.message.server.default_role, overwrite=everyone_perms)
            mine = discord.ChannelPermissions(target=ctx.message.author, overwrite=my_perms)
            bot = discord.ChannelPermissions(target=ctx.message.server.me, overwrite=my_perms)
            support = discord.ChannelPermissions(target=discord.utils.get(ctx.message.server.roles, name=config_setup.support_role), overwrite=support_perms)
            channel = await self.bot.create_channel(ctx.message.server, '{}-ticket'.format(ctx.message.author.name), everyone, mine, bot, support)

            await self.bot.send_message(channel, embed=dear_embed)

            print("New ticket created by " + ctx.message.author.name)
        else:
            await self.bot.say(messages.message['not_in_channel'])


def setup(bot):
    bot.add_cog(New(bot))
