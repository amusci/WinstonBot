import discord
import os
import asyncio
import keys1
import random
from discord.ext import commands, tasks
from itertools import cycle

# Create a bot instance with specified command prefix and intents
bot = commands.Bot(command_prefix='-', intents=discord.Intents.all())

bot_status = cycle(['HIGH TEMPO DUELS', 'JOIN HTD NOW', 'HTD SEASON 3', 'hort...I SAID HORT'])


@tasks.loop(seconds=45)
async def change_status():
    await bot.change_presence(activity=discord.Game(next(bot_status)))


@bot.event
async def on_ready():
    print(f'Success: The bot is now on.')
    change_status.start()



'''
bot.command(aliases = ["foo","bar","fizz","buzz",]) 
this is a way to have multiple names for your command 
'''

@bot.command()
async def ping(ctx):
    bot_latency = round(bot.latency * 1000)

    await ctx.send(f'Pong!  \nResponse time {bot_latency} ms.')


@bot.command()
async def hort(ctx):
    result = 'HEADS' if random.randint(0, 10) > 5 else 'TAILS'
    await ctx.send(result)


bot.run(keys1.DISCORD_TOKEN)