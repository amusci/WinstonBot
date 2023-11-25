import discord
import responses
import keys1
from discord.ext import commands, tasks

# Create default intents
intents = discord.Intents.all()

# Create a bot instance with specified command prefix and intents
bot = commands.Bot(command_prefix='!', intents=intents)


async def sendMessage(message, user, private):
    try:
        response = responses.responseHandler(user)
        await message.author.send(response) if private else await message.channel.send(response)
    except Exception as e:
        print(e)


def run():
    @bot.event
    async def on():
        print(f'The bot is now on.')

    @bot.event
    async def on_message(message):
        # Ignore messages from the bot itself
        if message.author == bot.user:
            return

        username = str(message.author)
        message = str(message.content)
        print(f"{message} was from {username} ")
        # Will only retrieve message if Pinged

    bot.run(keys1.DISCORD_TOKEN)
