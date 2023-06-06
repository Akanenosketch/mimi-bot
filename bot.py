import discord
import os # default module
from dotenv import load_dotenv
import random # for rnd based commands

def run_discord_bot():

  load_dotenv() # load all the variables from the env file
  bot = discord.Bot()

  @bot.event
  async def on_ready():
      print(f"{bot.user} is ready and online!")

  @bot.slash_command(name = "ping", description = "Shows the bot's ping!")
  async def ping(ctx):
      rnd = random.randrange(3)
      match rnd:
        case 0:
          await ctx.respond(f"Pong! ({bot.latency*1000} ms)")
        case 1:
          await ctx.respond(f"Pong! ||~~Mafia time?~~|| ({bot.latency*1000} ms)")
        case 2:
          await ctx.respond(f"Ping pong! Get a life! ({bot.latency*1000} ms)")

  @bot.slash_command(name = "pull_8ball", description= "We all know too well what does this do")
  async def pull_8ball(ctx, question: discord.Option(str)):
    rnd = random.randrange(16)
    embed = discord.Embed(
      title="8ball",
      color=discord.Colour.teal(), # Pycord provides a class with default colors you can choose from
    )
    embed.add_field(name="Question: ", value= question, inline= True)
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
        value = "Stop using 8ball for your bullshity, don't you have a life?"
    embed.add_field(name= "Answer: ", value= value, inline=True)
    embed.set_thumbnail(url= "https://e7.pngegg.com/pngimages/438/588/png-clipart-eight-ball-8ball-mjg-magic-8-ball-eightball-store-logo-rapper-skull-sports-pool.png")
    await ctx.respond(embed=embed)

  bot.run(os.getenv('TOKEN')) # run the bot with the token


    



