import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

message = 'Test'
@client.event
async def on_ready():
    print('Wir sind eingeloggt als User {}'.format(client.user.name))
    client.loop.create_task(send(message))
    client.loop.create_task(status_task())


async def status_task():
    while True:
        await client.change_presence(activity=discord.Game('BeerPongBot'), status=discord.Status.online)


async def send(message):
    await client.get_channel(1018157039127642113).send(message)


client.run('MTAxODE1NzQwNzIyMzkzOTA3Mg.GqgUdX.pF21GqW3KIy11HYL55jfl0SOVWQoM55n2VFQDM')