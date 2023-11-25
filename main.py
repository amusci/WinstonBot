import discord

DISCORD_TOKEN = 'ODI5NTQyNzY2OTcxMzIyNDI4.GHHjSi.--2fCbgNWpG4AHjJDNtSM8Pwa_MpIncHfnTY7s'

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run(DISCORD_TOKEN)
