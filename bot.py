import discord
import responses


async def send_message(message, user_message, username, is_private):
  try:
    response = responses.handle_Response(user_message, username)
    await message.author.send(response) if is_private else await message.channel.send(response)
  except Exception as e:
    print()

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
    if message.author == client.user:
      return
    
    username = str(message.author)
    user_message = str(message.content)
    ##old_message = 
    channel = str(message.channel)
    
    if user_message[0] =='?':
      user_message = user_message[1:]
      await send_message(message,user_message, username, is_private=True)
    else:
      await send_message(message,user_message, username, is_private=False)

  client.run(TOKEN)

    



