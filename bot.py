import discord
import keys1
import random
import gspread
from discord.ext import commands, tasks
from itertools import cycle
from oauth2client.service_account import ServiceAccountCredentials

# Create a bot instance with specified command prefix and intents
bot = commands.Bot(command_prefix='-', intents=discord.Intents.all(), case_insensitive=True)

bot_status = cycle(['HIGH TEMPO DUELS', 'JOIN HTD NOW', 'HTD SEASON 3', 'hort...I SAID HORT'])

scopes = ['https://www.googleapis.com/auth/spreadsheets',
          'https://www.googleapis.com/auth/drive']

creds = ServiceAccountCredentials.from_json_keyfile_name(
    'D:\\coding\\WinstonBot\\gkey.json', scopes=scopes)

file = gspread.authorize(creds)
workbook = file.open("HTDIII")


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
    try:

        # Takes -ping as an input and spits out the latency of the output
        bot_latency = round(bot.latency * 1000)

        await ctx.send(f'Pong!  \nResponse time {bot_latency} ms.')

    except Exception as e:
        print(f"Error: {e}")
        await ctx.send("STOP PINGING PLEASE.")


@bot.command()
async def hort(ctx):
    try:

        # Takes -hort as an input and then spits out HEADS or TAILS
        result = 'HEADS' if random.randint(0, 10) > 5 else 'TAILS'
        await ctx.send(result)
    except Exception as e:
        print(f"Error: {e}")
        await ctx.send("? what do you want lol")


@bot.command()
async def wyr(ctx):
    try:
        # Open the file and read all lines into a list
        with open("wyr.txt") as open_file:
            lines = open_file.readlines()
            length = len(lines)
            # print(length)
            await ctx.send(lines[random.randint(1, length - 1)])
    except Exception as e:
        print(f"Error: {e}")
        await ctx.send("Relax Pal.")


@bot.command(aliases=["8ball", "8"])
async def eightball(ctx):
    try:
        # Open the file and read all lines into a list
        with open("8.txt") as open_file:
            lines = open_file.readlines()
            length = len(lines)
            await ctx.send(lines[random.randint(1, length)])
    except Exception as e:
        print(f"Error: {e}")
        await ctx.send("Relax Pal.")


@bot.command()
async def players_d1(ctx):
    try:
        sheet_index = 0  # first sheet
        sheet = workbook.get_worksheet(sheet_index)
        values = sheet.range(f'A1:A{len(sheet.col_values(1))}')
        # Creating an embed
        embed = discord.Embed(title="Players in DIVISION I", color=discord.Color.red())

        # fields for each cell
        for i, cell in enumerate(values, start=1):
            embed.add_field(name=f"Player {i}", value=cell.value, inline=False)

        # sending the embed
        await ctx.send(embed=embed)

    except Exception as e:
        print(f"Error: {e}")
        await ctx.send("An error occurred while fetching data from the worksheet.")


@bot.command()
async def players_d2(ctx):
    try:
        sheet_index = 1  # Index of the sheet
        sheet = workbook.get_worksheet(sheet_index)
        values = sheet.range(f'A1:A{len(sheet.col_values(1))}')

        # Creating an embed
        embed = discord.Embed(title="Players in DIVISION II", color=discord.Color.blue())

        # Adding fields for each cell value
        for i, cell in enumerate(values, start=1):
            embed.add_field(name=f"Player {i}", value=cell.value, inline=False)

        # Sending the embed
        await ctx.send(embed=embed)

    except Exception as e:
        print(f"Error: {e}")
        await ctx.send("An error occurred while fetching data from the worksheet.")


@bot.command()
async def players_d3(ctx):
    try:
        sheet_index = 2  # Index of the sheet
        sheet = workbook.get_worksheet(sheet_index)
        values = sheet.range(f'A1:A{len(sheet.col_values(1))}')

        # Creating an embed
        embed = discord.Embed(title="Players in DIVISION III", color=discord.Color.green())

        # Adding fields for each cell value
        for i, cell in enumerate(values, start=1):
            embed.add_field(name=f"Player {i}", value=cell.value, inline=False)

        # Sending the embed
        await ctx.send(embed=embed)

    except Exception as e:
        print(f"Error: {e}")
        await ctx.send("An error occurred while fetching data from the worksheet.")


@bot.command(aliases=["sd1"])
async def standings_d1(ctx):
    try:
        sheet_index = 3  # Index of the sheet
        sheet = workbook.get_worksheet(sheet_index)
        cols = sheet.get_all_values()
        players = []
        total = []
        sets = []
        for col in cols:
            value = col[9]  # Assuming you want to remove leading and trailing whitespaces
            if not value:
                pass
            elif value == 'Players':
                break
            else:
                players.append(value + ' - ')

        for col in cols:
            value = col[10]  # Assuming you want to remove leading and trailing whitespaces
            if not value:
                pass
            elif value == 'Total Points':
                break
            else:
                total.append(value)

        for col in cols:
            value = col[11]  # Assuming you want to remove leading and trailing whitespaces
            if not value:
                pass
            elif value == 'Sets':
                break
            else:
                sets.append(' - ' + value + ' sets played')

        res = [i + j + k for i, j, k in zip(players, total, sets)]


        # Creating an embed
        embed = discord.Embed(title="Standings of Division I", color=discord.Color.red())

        # Adding fields for each cell value
        for i, cell in enumerate(res, start=1):
            embed.add_field(name=f"Rank {i}", value=cell, inline=False)

        # Sending the embed
        await ctx.send(embed=embed)

    except Exception as e:
        print(f"Error: {e}")
        await ctx.send("An error occurred while fetching data from the worksheet.")


@bot.command(aliases=["sd2"])
async def standings_d2(ctx):
    try:
        sheet_index = 3  # Index of the sheet
        sheet = workbook.get_worksheet(sheet_index)
        cols = sheet.get_all_values()
        players = []
        total = []
        sets = []
        for col in cols:
            value = col[1]  # Assuming you want to remove leading and trailing whitespaces
            if not value:
                pass
            elif value == 'Players':
                break
            else:
                players.append(value + ' - ')

        for col in cols:
            value = col[2]  # Assuming you want to remove leading and trailing whitespaces
            if not value:
                pass
            elif value == 'Total Points':
                break
            else:
                total.append(value)
        for col in cols:
            value = col[3]  # Assuming you want to remove leading and trailing whitespaces
            if not value:
                pass
            elif value == 'Sets':
                break
            else:
                sets.append(' - ' + value + ' sets played')

        res = [i + j + k for i, j, k in zip(players, total, sets)]


        # Creating an embed
        embed = discord.Embed(title="Standings of Division II", color=discord.Color.blue())

        # Adding fields for each cell value
        for i, cell in enumerate(res, start=1):
            embed.add_field(name=f"Rank {i}", value=cell, inline=False)

        # Sending the embed
        await ctx.send(embed=embed)

    except Exception as e:
        print(f"Error: {e}")
        await ctx.send("An error occurred while fetching data from the worksheet.")


@bot.command(aliases=["sd3"])
async def standings_d3(ctx):
    try:
        sheet_index = 3  # Index of the sheet
        sheet = workbook.get_worksheet(sheet_index)
        cols = sheet.get_all_values()
        players = []
        total = []
        sets = []
        for col in cols:
            value = col[5]  # Assuming you want to remove leading and trailing whitespaces
            if not value:
                pass
            elif value == 'Players':
                break
            else:
                players.append(value + ' - ')

        for col in cols:
            value = col[6]  # Assuming you want to remove leading and trailing whitespaces
            if not value:
                pass
            elif value == 'Total Points':
                break
            else:
                total.append(value)

        for col in cols:
            value = col[7]  # Assuming you want to remove leading and trailing whitespaces
            if not value:
                pass
            elif value == 'Sets':
                break
            else:
                sets.append(' - ' + value + ' sets played')

        res = [i + j + k for i, j, k in zip(players, total, sets)]

        # Creating an embed
        embed = discord.Embed(title="Standings of Division III", color=discord.Color.green())

        # Adding fields for each cell value
        for i, cell in enumerate(res, start=1):
            embed.add_field(name=f"Rank {i}", value=cell, inline=False)

        # Sending the embed
        await ctx.send(embed=embed)

    except Exception as e:
        print(f"Error: {e}")
        await ctx.send("An error occurred while fetching data from the worksheet.")


bot.run(keys1.DISCORD_TOKEN)
