import discord, random, json,requests,asyncio
from discord.ext import commands

     # create bot instance
bot = commands.Bot(command_prefix='!', description='porn discord Bot By Juji')
     # load file into json and data define
o = json.load(open('comments.json','r',encoding='utf-8-sig'))
data = [(m['username'],m['text']) for m in o]
	 # load commands txt 

     # login
@bot.event
async def on_ready():
    channel = discord.Object(id='insert channel here')
    print("Logged in Dis Bitch!:  name={}, id={}".format( bot.user.name, bot.user.id ))


@bot.command(pass_context=True)
async def porn(ctx):
    # Chooses a random quote
    text = random.choice(data)
    msg = "{}".format(text)
    await bot.say(msg)

async def my_background_task():
    await bot.wait_until_ready()
    channel = discord.Object(id='insert channel here')
    while not bot.is_closed:
        text = random.choice(data)
        msg = "Here is your Hourly Random Pornhub Comment: {}".format(text)
        await bot.send_message(channel, msg)
        await asyncio.sleep(3600) # task runs every 3600 seconds

@bot.command(pass_context=True)
async def pornx(ctx, n: int = 1):
    """Chooses a random quote."""
    msg = ["{}".format(text) for text in [random.choice(data) for _ in range(0,n)]]
    await bot.say('\n'.join(msg))

@bot.command(pass_context=True)
async def search(ctx, phrase : str):
    # Match data with a search-phrase
    results = []
    for datestamp, text in data:
        if phrase in text: results.append( "{} \n{}\n".format(datestamp, text))
        if len(results) > 8: break

    if len(results) > 0:
        msg = "\n\n {}".format( "\n".join(results) )
    else:
        msg = "`  {} porn Never Said That Before I Gayce`".format(phrase)
    await bot.say(msg)


@bot.command(pass_context=True)
async def commands(ctx):
    # Returns Commands
     with open('c:\commands.txt','r',encoding='utf-8-sig') as content_file:
          read = content_file.read()
     msg = "{}".format(read)
     await bot.say(msg)

bot.loop.create_task(my_background_task())

if __name__ == "__main__":
    try:
        bot.run('Insert token here')
    except:
        pass
