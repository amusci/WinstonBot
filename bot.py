import discord
import responses
import keys1

DISCORD_TOKEN = 'ODI5NTQyNzY2OTcxMzIyNDI4.GHHjSi.--2fCbgNWpG4AHjJDNtSM8Pwa_MpIncHfnTY7s'


async def sendMessage(message, user, private):
    try:
        response = responses.responseHandler(user)
        await message.author.send(response) if private else await message.channel.send(response)
    except Exception as e:
        print(e)


def run():
    intents = discord.Intents.default()
    client = discord.Client(intents=intents)

    @client.event
    async def on():
        print(f'{client.user} is now on.')

    client.run(DISCORD_TOKEN)
