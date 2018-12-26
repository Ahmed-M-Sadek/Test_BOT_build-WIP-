import random

from discord import Game
from discord.ext.commands import Bot

BOT_PREFIX = "!="
TOKEN = 'NTI3NTI1Mjk1MTI1NjkyNDE4.DwVA6Q.DySY15hAaUks3_cnQ7zlgPkqtiM'

client = Bot(command_prefix=BOT_PREFIX)

@client.event
async def on_ready():
    await client.change_presence(game=Game(name="With puny humans"))
    print("Logged in as " + client.user.name)



@client.command(name='8b',description='Random response',brief='responses are random lel',pass_context=True)
async def eight_ball(context):
    possible_responses = [
        'You will live for another day',
        'a great future awaits you',
        'you are talking to a virtual non-existing bot',
        'no u',
        'ummmm how about no'
    ]
    await client.say(random.choice(possible_responses) + ',   ' + context.message.author.mention)
client.run(TOKEN)

