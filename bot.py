import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import random
# for cogs
import builtins

load_dotenv()
TOKEN = os.getenv('TOKEN')

bot = commands.Bot(command_prefix='!')
builtins.bot = bot


@bot.event
async def on_ready():
    print(f'{bot.user.name} has joined the chat!')


@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')


@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')


@bot.command()
async def reload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
    bot.load_extension(f'cogs.{extension}')


# @bot.command()
# async def ping(ctx):
#     await ctx.send(f'Pong! {round(self.bot.latency * 1000)}ms')


# @bot.command(aliases=['8ball'])
# async def eightball(ctx, *, question=None):
#     if ctx.author == bot.user:
#         return

#     if question == None:
#         await ctx.send('You have to ask a question!')

#     else:

#         responses = [
#             'It is certain.',
#             'It is decidedly so.',
#             'Without a doubt.',
#             'Yes - definitely.',
#             'You may rely on it',
#             'As I see it, yes.',
#             'Most likely.',
#             'Outlook good.',
#             'Yes.',
#             'Signs point to yes.',
#             'Reply hazy, try again.',
#             'Ask again later.',
#             'Better not tell now.',
#             'Cannot predict now.',
#             'Concentrate and ask again.',
#             'Don\'t count on it.',
#             'My reply is no.',
#             'My sources say no.',
#             'Outlook not so good.',
#             'Very doubtful.',
#             'No.'
#         ]

#         response = random.choice(responses)
#         await ctx.send(response)

bot.run(TOKEN)
