import discord
import keys1
import random
import gspread
from discord.ext import commands, tasks
from itertools import cycle
from oauth2client.service_account import ServiceAccountCredentials


# Create a bot instance with specified command prefix and intents
bot = commands.Bot(command_prefix='-', intents=discord.Intents.all())

bot_status = cycle(['HIGH TEMPO DUELS', 'JOIN HTD NOW', 'HTD SEASON 3', 'hort...I SAID HORT'])


scopes = ['https://www.googleapis.com/auth/spreadsheets',
          'https://www.googleapis.com/auth/drive']

creds = ServiceAccountCredentials.from_json_keyfile_name(
    'D:\\coding\\WinstonBot\\gkey.json', scopes=scopes)

file = gspread.authorize(creds)
workbook = file.open("HTD3")
sheet = workbook.sheet1




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
    # Takes -ping as an input and spits out the latency of the output
    bot_latency = round(bot.latency * 1000)

    await ctx.send(f'Pong!  \nResponse time {bot_latency} ms.')


@bot.command()
async def hort(ctx):
    # Takes -hort as an input and then spits out HEADS or TAILS
    result = 'HEADS' if random.randint(0, 10) > 5 else 'TAILS'
    await ctx.send(result)


@bot.command()
async def wyr(ctx):
    # Open the file and read all lines into a list
    with open("wyr.txt") as open_file:
        lines = open_file.readlines()
        await ctx.send(lines[random.randint(1, 30)])


@bot.command()
async def eightball(ctx):
    # Open the file and read all lines into a list
    with open("8.txt") as open_file:
        lines = open_file.readlines()
        await ctx.send(lines[random.randint(1, 30)])

@bot.command()
async def players(ctx):
    for cell in sheet.range('B4:B11'):
        await ctx.send(cell.value)


bot.run(keys1.DISCORD_TOKEN)
