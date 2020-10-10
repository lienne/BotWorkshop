import discord
from discord.ext import commands
import asyncio


class Clear(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_guild_permissions(manage_messages=True)
    async def clear(self, ctx, amount=0):
        """
        Clears specified number of messages.
        In order for this to work, the bot must have manage messages permissions.
        To use this command you must have manage messages permissions.
        """
        await ctx.channel.purge(limit=amount + 1)
        await ctx.send(f'Deleted {amount} messages.')
        await asyncio.sleep(1)
        await ctx.channel.purge(limit=1)


def setup(bot):
    bot.add_cog(Clear(bot))
