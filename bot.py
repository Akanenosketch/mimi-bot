import discord
import os # default module
from dotenv import load_dotenv
import random # for rnd based commands
import responses #For non-application commands (responses)

##Block for sending messages if you have put a certain keyword
async def send_message(message, user_message, username, is_private):
  try:
    response = responses.handle_Response(user_message)
    await message.author.send(response) if is_private else await message.channel.send(response)
  except Exception as e:
    print(f"{user_message} - sent by {username}")

def run_discord_bot():
  load_dotenv() # load all the variables from the env file
  bot = discord.Bot(intents= discord.Intents.all())


  ##Bot events section
  @bot.event
  async def on_ready():
      print(f"{bot.user} is ready and online!")
  
  @bot.event
  async def on_message(message):
    try:
      if message.author == bot.user:   #Avoids loop on the bot
        return
      
      user_message = str(message.content)
      username = str(message.author)

      if user_message[0] =='?':
        user_message = user_message[1:]
        await send_message(message, user_message, username, is_private=True)
      else:
        await send_message(message,user_message, username, is_private=False)
    except IndexError as error: 
      print(message.attachments)
      print(error)
  
  #Log events
  @bot.event
  async def on_message_delete(message):
    async for entry in message.guild.audit_logs(limit=1,action=discord.AuditLogAction.message_delete): #admin needed lol
      deleter = entry.user
      entry_user = message.guild.get_member(message.author.id)
      if(entry_user.get_role(1116369818141073439) == None):
        deleter = message.author
    if message.author != bot.user:
      try:
        print(f"Message deleted: {message.content}- by {message.author.name} (deleted by {deleter.name})")
        channel = await message.guild.fetch_channel(1116369654366076989)

        embed = discord.Embed(
          title = "Deleted message",
          color= discord.Color.red(),
        )
        embed.add_field(name= "Author: ", value=message.author, inline=False)
        embed.add_field(name= "Channel: ", value= message.channel, inline= False)
        embed.add_field(name="Deleter: ", value= deleter.name, inline= False)
        if not message.content == "":
          embed.add_field(name = "Message content", value= message.content)
        else:
          for i in range(len(message.attachments)):
            embed.add_field(name=f"Message content n {i+1}" , value= message.attachments[i].proxy_url)
        embed.set_author(name= message.author.name, icon_url= message.author.avatar)
        await channel.send(embed=embed)
      except discord.errors.InvalidData or discord.HTTPException or discord.Forbidden as e:
        print(f"An exception has occurred: {e}")
    else:
      channel = await message.guild.fetch_channel(1116369654366076989)
      await channel.send(f"Really? Deleting logs? I call that a **low blow** <@{deleter.id}>")

  @bot.event
  async def on_message_edit(old_message, new_message):
    try:
      if not old_message.author.bot:
        channel= await new_message.guild.fetch_channel(1116369654366076989)
        embed = discord.Embed(
          title= "Message edited",
          color= discord.Color.dark_green()
        ) 
        embed.add_field(name="Author: ", value= new_message.author, inline=False)
        embed.add_field(name="Old message:", value=old_message.content, inline=False)
        embed.add_field(name="New message", value=new_message.content, inline=False)
        embed.set_author(name="Message edited", icon_url= new_message.author.avatar)
        await channel.send(embed=embed)
      else:
        print("boi, since when a bot does know how to edit?")
    except discord.errors.InvalidData as e:
      print(f"{e}, exception caused by{old_message.author}")

##Bot slash commands section
##Help command
  @bot.slash_command(name = "help", description = "Shows all the current available commands!")
  async def help(ctx):
    embed = discord.Embed(
      title= "Help page",
      description = "A list with all the corrent available commands!",
      color= discord.Color.embed_background()
    )
    embed.add_field(name= "ping", value= "Shows the current bot's latency", inline =False)
    embed.add_field(name= "pull_8ball", value= "Let's see what the 8ball says today...", inline =False)
    embed.add_field(name= "future", value= "Pulls a random predict on your future", inline =False)
    embed.add_field(name= "sleep", value= "Sleep? That's not in my dictionary (lol)", inline =False)
    embed.add_field(name= "avatar", value= "Stealing pfps? Gotcha", inline =False)
    await ctx.respond(embed= embed)
    
  @bot.slash_command(name="free_time", description= "Shows how much free time you have! (I am not responsible if it's accurate to your real free-time)")
  async def free_time(ctx):
    rnd= random.randrange(7)
    embed = discord.Embed(
      title= "How much free time you have?",
      color= discord.Color.teal()
    )
    if rnd==1:
      embed.add_field(name="Your amount of free time is...." , value= "`NullFreeTimeException` \nYou have no free time ||~~coffee coffee coffee coffe coffee~~||", inline=False)
      embed.set_image( url="https://cdn.discordapp.com/attachments/1117814758175953047/1117814822650789979/Investigacion_y_diseno_6.png")
    if rnd==0:
      embed.add_field(name="Your amount of free time is...." , value= "`NegativeFreeTimeException` \nYou're the definition of not having a fucking life", inline=False)
      embed.set_image(url="https://cdn.discordapp.com/attachments/1117814758175953047/1117814824852795432/Investigacion_y_diseno_7.png")
    if rnd==2:
      embed.add_field(name="Your amount of free time is....", value="You have really little free time.\nHey! Don't bother this person, they are a pretty busy one", inline=False)
      embed.set_image(url="https://cdn.discordapp.com/attachments/1117814758175953047/1117814823040864256/Investigacion_y_diseno_5.png")
    if rnd==3:
      embed.add_field(name="Your amount of free time is....", value= "You have a bit of free time...\nGo out and grab a coffee as a break!", inline=False)
      embed.set_image(url="https://media.discordapp.net/attachments/1117814758175953047/1117814823468679229/Investigacion_y_diseno_4.png")
    if rnd==4:
      embed.add_field(name="Your amount of free time is....", value= "Still busy but more free than I am", inline=False)
      embed.set_image(url="https://media.discordapp.net/attachments/1117814758175953047/1117814823753887754/Investigacion_y_diseno_3.png")
    if rnd==5:
      embed.add_field(name="Your amoutn of free time is....", value= "You have a lots of free time...\n**Gimme some of your free time**", inline=False)
      embed.set_image(url="https://media.discordapp.net/attachments/1117814758175953047/1117814824064274493/Investigacion_y_diseno_2.png")
    if rnd==6:
      embed.add_field(name="Your amount of free time is....", value="You have too much free time...im jelly\n||I NeEd YoUr FrEe TiMe FoR ReSeArCh PuRpOsEs ~~to fucking sleep~~||", inline=False)
      embed.set_image(url="https://media.discordapp.net/attachments/1117814758175953047/1117814824424980571/Investigacion_y_diseno.png")
    await ctx.defer()
    await ctx.respond(embed=embed)

  @bot.slash_command(name = "ping", description = "Shows the bot's ping!")
  async def ping(ctx):
      rnd = random.randrange(4)
      match rnd:
        case 0:
          await ctx.respond(f"Pong! ({bot.latency*1000} ms)")
        case 1:
          await ctx.respond(f"Pong! ||~~Mafia time?~~|| ({bot.latency*1000} ms)")
        case 2:
          await ctx.respond(f"Ping pong! Get a life! ({bot.latency*1000} ms)")
        case 3:
          await ctx.respond(f"Pingity pong! Fuck you my guy ({bot.latency*1000} ms)")

  @bot.slash_command(name = "pull_8ball", description= "We all know too well what does this do")
  async def pull_8ball(ctx, question: discord.Option(str, description= "What would you like to ask to the almighty 8ball?", required= True)):
    rnd = random.randrange(16)
    embed = discord.Embed(
      title="8ball",
      color=discord.Colour.teal(), # Pycord provides a class with default colors you can choose from
    )
    embed.add_field(name="Question: ", value= question, inline= False)
    value = ""
    match rnd:
      case 0:
        value = "I can't say no, but also can't say yes"    
      case 1:
        value = "I agree"
      case 2:
        value = "Ask soemone else, wil you?"
      case 3:
        value = "Not sure why are you asking that, but ok boomer"
      case 4:
        value = "Yes"
      case 5:
        value = "Not sure"
      case 6:
        value = "I don't know? fucking weirdo"
      case 7:
        value = "Just go ask your god, ok?"
      case 8:
        value = "???????"
      case 9:
        value = "My guy, please go take your meds"
      case 10:
        value = "Probably, can't confirm"
      case 11:
        value = "Call your nearest psych ward, after listening to that question I can tell you really need it"
      case 12:
        value = "Most likely yes"
      case 13:
        value = "HAHAHAHAHAHAHAHAHA\n\n\nnice try, but no"
      case 14:
        value = "*The person you're trying to contact with is unavailable, please try again later* ||~~the answer is no~~||"
      case 15:
        value = "Stop using 8ball for your bullshit, don't you have a life?"
    embed.add_field(name= "Answer: ", value= value, inline=False)
    embed.set_thumbnail(url= "https://e7.pngegg.com/pngimages/438/588/png-clipart-eight-ball-8ball-mjg-magic-8-ball-eightball-store-logo-rapper-skull-sports-pool.png")
    await ctx.respond(embed=embed)

  @bot.slash_command(name= "future", description= "Pulls a predict about your future!")
  async def future(ctx):
    ans = ""
    rnd = random.randrange(10)
    embed = discord.Embed(
      title="Prediction results: ",
      color=discord.Colour.random(), # Pycord provides a class with default colors you can choose from
    )
    match rnd:
      case 0:
        ans = "You have a 'future' I guess"
        embed.add_field(name = "The predict is....", value = ans, inline = True)
        embed.set_image(url = "https://media.tenor.com/0GOwPHgcUj0AAAAM/anime-shrug.gif")
      case 1:
        ans = "A bright future awaits for you"
        embed.add_field(name = "The predict is....", value = ans, inline = True)
        embed.set_image(url = "https://media.tenor.com/SEG_91V5vRcAAAAM/anime-toobright.gif")
      case 2:
        ans = "Your future seems good, don't sleep it up"
        embed.add_field(name = "The predict is....", value = ans, inline = True)
        embed.set_image(url = "https://media.tenor.com/N7FBq595kr0AAAAM/anime-cat.gif")
      case 3:
        ans = "You're useless my guy"
        embed.add_field(name = "The predict is....", value = ans, inline = True)
        embed.set_image(url = "https://media.tenor.com/wb9FZbLWsYIAAAAM/jujutsu-kaisen-useless-miwa-here.gif")
      case 4:
        ans = "You might need a sugar mommy/daddy to survive"
        embed.add_field(name = "The predict is....", value = ans, inline = True)
        embed.set_image(url = "https://media.tenor.com/t6nLZE74HTIAAAAM/brat-angry.gif")
      case 5:
        ans = "Before getting a future you need to obtain a life you neet"
        embed.add_field(name = "The predict is....", value = ans, inline = True)
        embed.set_image(url = "https://media.tenor.com/ekfsOJejpZwAAAAM/gabriel-dropout-gabriel.gif")
      case 6:
        ans = "Are you sure you don't want to jump out or something?"
        embed.add_field(name = "The predict is....", value = ans, inline = True)
        embed.set_image(url = "https://media.tenor.com/-OE02caO9pMAAAAM/depression-sad.gif")
      case 7:
        ans = "future = HTTPError 404\n`Future not found`"
        embed.add_field(name = "The predict is....", value = ans, inline = True)
        embed.set_image(url = "https://media.tenor.com/i_qVt3RBuZUAAAAM/tsukasa-plastic-memories.gif")
      case 8:
        ans = "Yea sure, Bill Gates wannabe. You're going to end up under a bridge if you don't lower your ego"
        embed.add_field(name = "The predict is....", value = ans, inline = True)
        embed.set_image(url = "https://media.tenor.com/BEWnQpv8-2MAAAAM/kikis-delivery-service-cars.gif")
      case 9:
        ans = "Decent"
        embed.add_field(name = "The predict is....", value = ans, inline = True)
        embed.set_image(url = "https://media.tenor.com/BIpQGtdD_wcAAAAM/misatobored-misato.gif")
    await ctx.respond(embed=embed)
    
  @bot.slash_command(name= "sleep", description="Sleep?")
  async def sleep(ctx):
    userID = ctx.author.id
    rnd = random.randrange(5)
    match rnd:
      case 0:
        await ctx.respond("What's sleep? Is that edible?")
      case 1:
        await ctx.respond("To learn more info about sleep I decided to look it up for you\nhttps://letmegooglethat.com/?q=what+is+sleep%3F")
      case 2:
        await ctx.respond(f"<@{userID}> we know you need to sleep you sleepyhead")
      case 3:
        await ctx.respond("https://tenor.com/bwxAk.gif")
      case 4:
        await ctx.respond("https://cdn.discordapp.com/attachments/1115024613668290560/1115024655493894194/20230604_124525.jpg")

  @bot.slash_command(name = "avatar", description= "Shows your, or an user's avatar!")
  async def avatar(ctx, user: discord.Option(discord.SlashCommandOptionType.mentionable, description = "If you put another user it will show their profile pic!", required = False )):
    username = None
    if user == None:
      image = ctx.author.avatar
      username = ctx.author.name
      user = ctx.author
    else:
      image = user.avatar
      username = user.name
    embed = discord.Embed(
      title=  username + "'s avatar",
      color= discord.Colour.random()
    )
    embed.set_image(url = image)
    await ctx.respond(embed = embed)
 

  bot.run(os.getenv('TOKEN')) # run the bot with the token
