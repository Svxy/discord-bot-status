@client.event

client = discord.Client()

async def on_ready():
    await client.change_presence(activity=discord.Streaming(
        name='$help', url='https://www.twitch.tv/Cutiey'))