import discord
import responses
import keys1
import random
from discord.ext import commands, tasks

# Create a bot instance with specified command prefix and intents
bot = commands.Bot(command_prefix='-', intents=discord.Intents.all())


@bot.event
async def on_ready():
    print(f'Success: The bot is now on.')


'''commands'''


@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')


@bot.command()
async def hort(ctx):
    random_number = random.randint(0, 10)
    if random_number > 5:
        await ctx.send('HEADS')
    else:
        await ctx.send('TAILS')


bot.run(keys1.DISCORD_TOKEN)
