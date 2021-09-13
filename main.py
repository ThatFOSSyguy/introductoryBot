import discord
import os
from pingingTheBot import keeping_alive # Pinging the bot

client = discord.Client()

@client.event
async def on_ready():
  print('I have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  intrMsg = """__""" # <--Enter the introduction there
  if message.content.startswith('!intro'): # You can change the message content to call the bot
    await message.channel.send(intrMsg)

keeping_alive()
client.run(os.getenv('Token')) # In the place of the token you should add your own bot's token. If you are using online text editors like Repl.it, you must set it as .env and it should be stored carefully.
