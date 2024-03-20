# TODO: IMPLEMENT NFMGUESSR
#       SKRIBBLE SCORING SYSTEM
#       RANDOMLY POST THE IMAGE, WHOEVER GUESSES IT CORRECTLY GETS FULL PTS, REST GET HALF
import asyncio
import json
import os
import re

import discord
import keys1
import random
import gspread
from discord.ext import commands, tasks
from itertools import cycle
from oauth2client.service_account import ServiceAccountCredentials

# Create a bot instance with specified command prefix and intents
bot = commands.Bot(command_prefix='-', intents=discord.Intents.all(), case_insensitive=True)

bot_status = cycle(['HIGH TEMPO DUELS', 'HTD IV IS NOW OPEN', 'HTD SEASON 4 HAS BEGUN', 'hort...I SAID HORT',
                    'CHECK -show_stages !!!'])

scopes = ['https://www.googleapis.com/auth/spreadsheets',
          'https://www.googleapis.com/auth/drive']

creds = ServiceAccountCredentials.from_json_keyfile_name(
    'D:\\coding\\WinstonBot\\gkey.json', scopes=scopes)

file = gspread.authorize(creds)
workbook = file.open("HTDIV")


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
async def trivia(ctx):
    try:
        # Open the file and read all lines into a list
        with open("trivia.txt") as open_file:
            lines = open_file.readlines()
            length = len(lines)
            random_question = lines[random.randint(0, length - 1)]
            words_list = random_question.split('?')
            await ctx.send(words_list[0] + '?')

            def check(m):
                return m.author.id == ctx.author.id

            user_response = await bot.wait_for('message', check=check)
            print('user response is:' + user_response.content.replace("\n", ""))
            print(words_list[-1])

            if user_response.content == words_list[-1].replace("\n", ""):
                await ctx.send('CORRECT')
            else:
                await ctx.send('https://youtu.be/-aAku5nXAEI')

    except Exception as e:
        print(f"Error: {e}")
        await ctx.send("Relax Pal.")


@bot.command()
async def wyr(ctx):
    try:
        # Open the file and read all lines into a list
        with open("wyr.txt") as open_file:
            lines = open_file.readlines()
            length = len(lines)
            await ctx.send(lines[random.randint(0, length - 1)])
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


@bot.command(aliases=["ss"])
async def show_stages(ctx):
    try:
        with open('stages.txt') as open_file:
            lines = open_file.read()

            embed = discord.Embed(title='STAGES FOR HTD SEASON IV', description=lines)
            await ctx.author.send(embed=embed)
    except Exception as e:
        print(f"Error: {e}")
        await ctx.send("Relax Pal.")


@bot.command(aliases=["sc"])
async def show_cars(ctx):
    try:
        with open('cars.txt') as open_file:
            lines = open_file.read()

            embed = discord.Embed(title='CARS FOR HTD SEASON IV', description=lines)
            await ctx.author.send(embed=embed)
    except Exception as e:
        print(f"Error: {e}")
        await ctx.send("Relax Pal.")


@bot.command(aliases=["pd1"])
async def players_d1(ctx):
    try:
        sheet_index = 0  # first sheet
        sheet = workbook.get_worksheet(sheet_index)
        values = sheet.range(f'B4:B9')
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


@bot.command(aliases=["pd2"])
async def players_d2(ctx):
    try:
        sheet_index = 1  # Index of the sheet
        sheet = workbook.get_worksheet(sheet_index)
        values = sheet.range(f'B4:B9')

        # Creating an embed
        embed = discord.Embed(title="Players in DIVISION II ", color=discord.Color.red())

        # Adding fields for each cell value
        for i, cell in enumerate(values, start=1):
            embed.add_field(name=f"Player {i}", value=cell.value, inline=False)

        # Sending the embed
        await ctx.send(embed=embed)

    except Exception as e:
        print(f"Error: {e}")
        await ctx.send("An error occurred while fetching data from the worksheet.")


@bot.command(aliases=["pd3"])
async def players_d3(ctx):
    try:
        sheet_index = 2  # Index of the sheet
        sheet = workbook.get_worksheet(sheet_index)
        values = sheet.range(f'B4:B9')

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


@bot.command(aliases=["pd4"])
async def players_d4(ctx):
    try:
        sheet_index = 3  # Index of the sheet
        sheet = workbook.get_worksheet(sheet_index)
        values = sheet.range(f'B4:B9')

        # Creating an embed
        embed = discord.Embed(title="Players in DIVISION IV", color=discord.Color.green())

        # Adding fields for each cell value
        for i, cell in enumerate(values, start=1):
            embed.add_field(name=f"Player {i}", value=cell.value, inline=False)

        # Sending the embed
        await ctx.send(embed=embed)

    except Exception as e:
        print(f"Error: {e}")
        await ctx.send("An error occurred while fetching data from the worksheet.")


@bot.command(aliases=["pd5"])
async def players_d5(ctx):
    try:
        sheet_index = 4  # Index of the sheet
        sheet = workbook.get_worksheet(sheet_index)
        values = sheet.range(f'B4:B9')

        # Creating an embed
        embed = discord.Embed(title="Players in DIVISION V", color=discord.Color.green())

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
        sheet_index = 5  # Index of the sheet
        sheet = workbook.get_worksheet(sheet_index)
        cols = sheet.get_all_values()
        players = []
        total = []
        sets = []
        for col in cols:
            value = col[0]  # Assuming you want to remove leading and trailing whitespaces
            if not value or value == 'D1':
                pass
            elif value == 'Players':
                break
            else:
                players.append(value + ' - ')

        for col in cols:
            value = col[1]  # Assuming you want to remove leading and trailing whitespaces
            if not value:
                pass
            elif value == 'Total Points':
                break
            else:
                total.append(value)

        for col in cols:
            value = col[2]  # Assuming you want to remove leading and trailing whitespaces
            if not value:
                pass
            elif value == 'Sets':
                break
            else:
                sets.append(' - ' + value + ' sets played')

        res = [i + j + k for i, j, k in zip(players, total, sets)]

        # Creating an embed
        embed = discord.Embed(title="Standings of Division I\n", color=discord.Color.red())

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
        sheet_index = 5  # Index of the sheet
        sheet = workbook.get_worksheet(sheet_index)
        cols = sheet.get_all_values()
        players = []
        total = []
        sets = []
        for col in cols:
            value = col[4]  # Assuming you want to remove leading and trailing whitespaces
            if not value or value == 'D2':
                pass
            elif value == 'Players':
                break
            else:
                players.append(value + ' - ')

        for col in cols:
            value = col[5]  # Assuming you want to remove leading and trailing whitespaces
            if not value:
                pass
            elif value == 'Total Points':
                break
            else:
                total.append(value)
        for col in cols:
            value = col[6]  # Assuming you want to remove leading and trailing whitespaces
            if not value:
                pass
            elif value == 'Sets':
                break
            else:
                sets.append(' - ' + value + ' sets played')

        res = [i + j + k for i, j, k in zip(players, total, sets)]

        # Creating an embed
        embed = discord.Embed(title="Standings of Division II\n", color=discord.Color.blue())

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
        sheet_index = 5  # Index of the sheet
        sheet = workbook.get_worksheet(sheet_index)
        cols = sheet.get_all_values()
        players = []
        total = []
        sets = []
        for col in cols:
            value = col[8]  # Assuming you want to remove leading and trailing whitespaces
            if not value or value == 'D3':
                pass
            elif value == 'Players':
                break
            else:
                players.append(value + ' - ')

        for col in cols:
            value = col[9]  # Assuming you want to remove leading and trailing whitespaces
            if not value:
                pass
            elif value == 'Total Points':
                break
            else:
                total.append(value)

        for col in cols:
            value = col[10]  # Assuming you want to remove leading and trailing whitespaces
            if not value:
                pass
            elif value == 'Sets':
                break
            else:
                sets.append(' - ' + value + ' sets played')

        res = [i + j + k for i, j, k in zip(players, total, sets)]

        # Creating an embed
        embed = discord.Embed(title="Standings of Division III\n", color=discord.Color.green())

        # Adding fields for each cell value
        for i, cell in enumerate(res, start=1):
            embed.add_field(name=f"Rank {i}", value=cell, inline=False)

        # Sending the embed
        await ctx.send(embed=embed)

    except Exception as e:
        print(f"Error: {e}")
        await ctx.send("An error occurred while fetching data from the worksheet.")


@bot.command(aliases=["sd4"])
async def standings_d4(ctx):
    try:
        sheet_index = 5  # Index of the sheet
        sheet = workbook.get_worksheet(sheet_index)
        cols = sheet.get_all_values()
        players = []
        total = []
        sets = []
        for col in cols:
            value = col[12]  # Assuming you want to remove leading and trailing whitespaces
            if not value or value == 'D4':
                pass
            elif value == 'Players':
                break
            else:
                players.append(value + ' - ')

        for col in cols:
            value = col[13]  # Assuming you want to remove leading and trailing whitespaces
            if not value:
                pass
            elif value == 'Total Points':
                break
            else:
                total.append(value)

        for col in cols:
            value = col[14]  # Assuming you want to remove leading and trailing whitespaces
            if not value:
                pass
            elif value == 'Sets':
                break
            else:
                sets.append(' - ' + value + ' sets played')

        res = [i + j + k for i, j, k in zip(players, total, sets)]

        # Creating an embed
        embed = discord.Embed(title="Standings of Division IV\n", color=discord.Color.gold())

        # Adding fields for each cell value
        for i, cell in enumerate(res, start=1):
            embed.add_field(name=f"Rank {i}", value=cell, inline=False)

        # Sending the embed
        await ctx.send(embed=embed)

    except Exception as e:
        print(f"Error: {e}")
        await ctx.send("An error occurred while fetching data from the worksheet.")


@bot.command(aliases=["sd5"])
async def standings_d5(ctx):
    try:
        sheet_index = 5  # Index of the sheet
        sheet = workbook.get_worksheet(sheet_index)
        cols = sheet.get_all_values()
        players = []
        total = []
        sets = []
        for col in cols:
            value = col[16]  # Assuming you want to remove leading and trailing whitespaces
            if not value or value == 'D5':
                pass
            elif value == 'Players':
                break
            else:
                players.append(value + ' - ')

        for col in cols:
            value = col[17]  # Assuming you want to remove leading and trailing whitespaces
            if not value:
                pass
            elif value == 'Total Points':
                break
            else:
                total.append(value)

        for col in cols:
            value = col[18]  # Assuming you want to remove leading and trailing whitespaces
            if not value:
                pass
            elif value == 'Sets':
                break
            else:
                sets.append(' - ' + value + ' sets played')

        res = [i + j + k for i, j, k in zip(players, total, sets)]

        # Creating an embed
        embed = discord.Embed(title="Standings of Division V\n", color=discord.Color.magenta())

        # Adding fields for each cell value
        for i, cell in enumerate(res, start=1):
            embed.add_field(name=f"Rank {i}", value=cell, inline=False)

        # Sending the embed
        await ctx.send(embed=embed)

    except Exception as e:
        print(f"Error: {e}")
        await ctx.send("An error occurred while fetching data from the worksheet.")


@bot.command()
async def TEMPNAME(ctx):
    try:
        folder_path = keys1.FILE_PATH
        folders = [f for f in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, f))]
        the_chosen_folder = random.choice(folders)
        files_in_folder = os.listdir(os.path.join(folder_path, the_chosen_folder))
        image_files = [f for f in files_in_folder if f.endswith(('.jpg', '.jpeg', '.png', '.gif'))]
        random_image = random.choice(image_files)
        embed = discord.Embed(title="NFMGUESSR", description="What is the name of this stage? :", color=0x00ff00)
        file_path = os.path.join(folder_path, the_chosen_folder, random_image)

        # Attach the image to the embed
        file = discord.File(file_path, filename=random_image)
        embed.set_image(url=f"attachment://{random_image}")

        # Send the embed with the attached image
        message = await ctx.send(embed=embed, file=file)
        print(random_image.split('.')[0])

        # Wait for a message from any user in the same channel
        def check(message):
            return message.channel == ctx.channel and message.author != bot.user

        while True:
            user_response = await bot.wait_for('message', check=check, timeout=60)  # Wait for 60 seconds

            # Check if the user's message matches the name of the image
            if user_response.content.lower() == random_image.split('.')[0].lower():
                await user_response.channel.send("yeah yeah yeah we paid")

                # Update user's score
                username = str(user_response.author)
                update_score(username, 100)
                break  # Exit the loop if the correct answer is provided

        # Send scores table as an embed
        scores = load_scores()
        scores_table = '\n'.join([f"{username}: {score}" for username, score in scores.items()])
        embed_scores = discord.Embed(title="NFMGUESSR SCORES", description=scores_table, color=0x00ff00)
        await ctx.send(embed=embed_scores)


    except asyncio.TimeoutError:
        await ctx.send("Time's up! Try again later.")
    except Exception as e:
        print(f"Error: {e}")
        await ctx.send("STOP PINGING PLEASE.")


def load_scores():
    scores = {}
    if os.path.exists(keys1.SCORES_FILE) and os.path.getsize(keys1.SCORES_FILE) > 0:
        with open(keys1.SCORES_FILE, 'r') as file:
            scores = json.load(file)
    return scores


def save_scores(scores):
    with open(keys1.SCORES_FILE, 'w') as file:
        json.dump(scores, file)


def update_score(username, points):
    scores = load_scores()
    scores[username] = scores.get(username, 0) + points
    save_scores(scores)


bot.run(keys1.DISCORD_TOKEN)
