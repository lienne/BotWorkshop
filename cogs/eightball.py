import discord
from discord.ext import commands
import random


class EightBall(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['8ball'])
    # * is a wildcard: allows multiple arguments to be passed in
    async def eightball(self, ctx, *, question=None):
        if ctx.author == bot.user:
            return

        if question == None:
            await ctx.send('You have to ask a question!')

        else:

            responses = [
                'It is certain.',
                'It is decidedly so.',
                'Without a doubt.',
                'Yes - definitely.',
                'You may rely on it',
                'As I see it, yes.',
                'Most likely.',
                'Outlook good.',
                'Yes.',
                'Signs point to yes.',
                'Reply hazy, try again.',
                'Ask again later.',
                'Better not tell now.',
                'Cannot predict now.',
                'Concentrate and ask again.',
                'Don\'t count on it.',
                'My reply is no.',
                'My sources say no.',
                'Outlook not so good.',
                'Very doubtful.',
                'No.'
            ]

            response = random.choice(responses)
            await ctx.send(response)


def setup(bot):
    bot.add_cog(EightBall(bot))
