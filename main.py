import discord
import os

client = discord.Client()

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
  if message.author == client.user:
    return 
  if message.content('tu madre'):
    await message.channel.send('La tuya por si acaso')


client.run(os.getenv('token'))