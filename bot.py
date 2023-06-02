import discord
import responses
import os


async def send_message(message, user_message, username, is_private):
  try:
    response = responses.handle_Response(user_message, username)
    if response != False:
      await message.author.send(response) if is_private else await message.channel.send(response)
    else:
      print(user_message + ' message by ' + username)
  except Exception as e:
    print(e, '- exception caused by: ', username)

def run_discord_bot():
  TOKEN = 'ODY0NTY1OTY2MTIwNjgxNTAz.GhrwMt.Th9HxRg_de168YelTbTQEH7RwWNZY7f6c9BJyY'
  intents = discord.Intents.default()
  intents.message_content = True
  client = discord.Client(intents=intents)

  @client.event
  async def on_ready():
    print(f'{client.user}is now running!')

  @client.event
  async def on_message(message):
    if message.author == client.user: ##avoids loop
      return
    ##test sniping command

    username = str(message.author)
    user_message = str(message.content)

    channel = str(message.channel)
    try:
      if user_message[0] =='?':
        user_message = user_message[1:]
        await send_message(message,user_message, username, is_private=True)
      else:
        await send_message(message,user_message, username, is_private=False)
    except IndexError as e:
      print(e)

  client.run(TOKEN)

    



