import discord, random, json,requests
from discord.ext import commands



# create bot instance
bot = commands.Bot(command_prefix='!', description='BobsBot PornHub Comments Boy By Juji')

# load file into json and data define
o = json.load(open('http://modrepo.com/cgi-bin/comments.json','rb')) 
data = [(m['username'],m['text']) for m in o]



"""login"""
@bot.event
async def on_ready():
    channel = discord.Object(id=432066274336440330)
    print("Logged in as:  name={}, id={}".format( bot.user.name, bot.user.id ))
    
client = discord.Client()

@bot.command(pass_context=True)
async def porn(ctx):
    """Chooses a random quote."""
    text = random.choice(data)
    msg = "{}".format(text)
    await bot.say(msg)


@bot.command(pass_context=True)
async def search(ctx, phrase : str):
    """Match data with a search-phrase"""
    results = []
    for username, text in data:
        if phrase in text: results.append( "User: {} \n{}\n".format(username, text))
        if len(results) > 3: break

    if len(results) > 0:
        msg = "\n\n {}".format( "\n".join(results) )
    else:
        msg = "`  {} Nobody Said That Before I Gayce`".format(phrase)
    await bot.say(msg)


"""WhoIs Function"""
@bot.command(pass_context=True)
async def whoissyphor():
    msg = "Compulsive Hardchatter Who Is Probably Flying On Stims At Any Given Moment"
    await bot.say(msg)

@bot.command(pass_context=True)
async def whoiskaleena():
    msg = "  Moral Extremeist From Rural South"
    await bot.say(msg)

@bot.command(pass_context=True)
async def whoishydro():
    msg = "  *Helluv A Wilding n Shit* - xevan voice"
    await bot.say(msg)

@bot.command(pass_context=True)
async def whoislorea():
    msg = "  Some Basque Bitch"
    await bot.say(msg)

@bot.command(pass_context=True)
async def whoisdax():
    msg = "  GANG MF GANG"
    await bot.say(msg)

@bot.command(pass_context=True)
async def whoisenraged():
    msg = "  IF SHE BREATHE, SHE A THOT."
    await bot.say(msg)

@bot.command(pass_context=True)
async def whoisgrim():
    msg = "  Dat Boi"
    await bot.say(msg) 

@bot.command(pass_context=True)
async def whoismarza():
    msg = "  Prettiest Boy On Discord"
    await bot.say(msg) 

@bot.command(pass_context=True)
async def whoisjeth():
    msg = "  Juji's Jess"
    await bot.say(msg) 

@bot.command(pass_context=True)
async def whoisdj():
    msg = "  Sense/Sempai"
    await bot.say(msg) 

@bot.command(pass_context=True)
async def whoisolaf():
    msg = "  Not A Hacker"
    await bot.say(msg) 

@bot.command(pass_context=True)
async def whoisjulie():
    msg = "  Cardi B"
    await bot.say(msg) 

@bot.command(pass_context=True)
async def whoissheridan():
    msg = "  A Cute Triangle"
    await bot.say(msg) 

@bot.command(pass_context=True)
async def whoisrin():
    msg = "  Le Host Du Hardchat"
    await bot.say(msg) 

@bot.command(pass_context=True)
async def whoisjuji():
    msg = "  Soft Boy Kisser"
    await bot.say(msg) 

@bot.command(pass_context=True)
async def whoisgray():
    msg = "  The Crackhead"
    await bot.say(msg) 

@bot.command(pass_context=True)
async def whoisvirus():
    msg = "  The Hardchat Haccer"
    await bot.say(msg)

@bot.command(pass_context=True)
async def whoiseli(): 
    msg = "  Another Shrewd Jew"
    await bot.say(msg)
 
@bot.command(pass_context=True)
async def theroseparade():
    msg = "  !WhenIwas"
    await bot.say(msg)    

@bot.command(pass_context=True)
async def wheniwas():
    msg = "  !aYoungBoy"
    await bot.say(msg)    

@bot.command(pass_context=True)
async def ayoungboy():
    msg = "  !myFather"
    msg = "!myFather"
    await bot.say(msg)    

@bot.command(pass_context=True)
async def whoisjesss():
    msg = "  TWO S'S ON THAT SHIT NIGGA!!!!"
    await bot.say(msg)

@bot.command(pass_context=True)
async def whoiszoom():
    msg = "  XYRIX = CONFIRMED PEDO"
    await bot.say(msg) 

@bot.command(pass_context=True)
async def whoispad():
    msg = "  Dadillac Escobar"
    await bot.say(msg) 

@bot.command(pass_context=True)
async def whoisshell():
    msg = "  Tranny"
    await bot.say(msg) 

@bot.command(pass_context=True)
async def whoisbae():
    msg = "  She Thirsts For Lorea"
    await bot.say(msg)      

@bot.command(pass_context=True)
async def whoistrayc():
    msg = "  1/2 Of T6 <333"
    await bot.say(msg) 

@bot.command(pass_context=True)
async def whoisjames():
    msg = "  I DONT KNOW LOL"
    await bot.say(msg) 

@bot.command(pass_context=True)
async def whoisthisfag():
    msg = "  LOL I KNO HE A TRY HARD"
    await bot.say(msg)                           

@bot.command(pass_context=True)
async def whoisnt():
    msg = "  Pretentious Dude"
    await bot.say(msg) 

@bot.command(pass_context=True)
async def whoisyarp():
    msg = "  Tha Homie"
    await bot.say(msg) 

@bot.command(pass_context=True)
async def whoissd():
    msg = "  ME NIGGA!"
    await bot.say(msg) 

@bot.command(pass_context=True)
async def whoiskayla():
    msg = "  FWB Enthusiast"
    await bot.say(msg) 

@bot.command(pass_context=True)
async def whoiskayos():
    msg = "  sadboy"
    await bot.say(msg) 

@bot.command(pass_context=True)
async def whoisheather():
    msg = "  A Cuntree Gal"
    await bot.say(msg) 

@bot.command(pass_context=True)
async def whoislavos():
    msg = "  Hello Kitty Gvngsta"
    await bot.say(msg) 

@bot.command(pass_context=True)
async def whoiskrazy():
    msg = "  Hacker Of 1/2 Silicon Valley"
    await bot.say(msg) 

@bot.command(pass_context=True)
async def whoismai():
    msg = "  I have a crush on <@276900079431057408> dont tell theone"
    await bot.say(msg) 

@bot.command(pass_context=True)
async def rep():
    msg = "!rep <@231739573464465408>"
    await bot.say(msg) 

@bot.command(pass_context=True)
async def sdmarry():
    msg = ".marry <@231739573464465408>"
    await bot.say(msg) 

@bot.command(pass_context=True)
async def sdbangjuji():
    msg = ".bang <@231739573464465408>"
    await bot.say(msg) 

@bot.command(pass_context=True)
async def logininfo(phrase : str):
    msg = "Logged in as:  name= @{}, id=@{}".format( bot.user.name, bot.user.id )
    await bot.say(msg)

@bot.command(pass_context=True)
async def whoisjae():
    msg = "  Steezy Guy"
    await bot.say(msg) 

@bot.command(pass_context=True)
async def sdinfo():
    msg = ".info"
    await bot.say(msg) 

@bot.command(pass_context=True)
async def whoisgary():
    msg = "  illsec with coding knowledge"
    await bot.say(msg) 

@bot.command(pass_context=True)
async def whoisd0ct0r():
    msg = "v strong boi not even wheelchair man"
    await bot.say(msg) 

@bot.command(pass_context=True)
async def whoisjamal():
    msg = "dark dark prince like jafar from aladin"
    await bot.say(msg) 


@bot.command(pass_context=True)
async def whoiskrsa():
    msg = "Sociopath"
    await bot.say(msg) 




@bot.command(pass_context=True)
async def photo():

    response = requests.get("https://www.reddit.com/r/megaten.json", headers={"User-Agent": "linux:memebot:v1.0.0"})
    page = response.json()

    random.choice(page["data"]["children"])["data"]["url"]
    all_urls = [sub["data"]["url"] for sub in page["data"]["children"] if "imgur" in sub["data"]["url"]]
    all_urls
    return True

@bot.command(pass_context=True, no_pm=True)
async def cmere(self, ctx):
        """Summons the bot to join your voice channel."""
        summoned_channel = ctx.message.author.voice_channel
        if summoned_channel is None:
            await self.bot.say('WHO DAT IZ? UP IN THE VC? NOT YOU LOL IDIOT.')
            return False

        state = self.get_voice_state(ctx.message.server)
        if state.voice is None:
            state.voice = await self.bot.join_voice_channel(summoned_channel)
        else:
            await state.voice.move_to(summoned_channel)

        return True

if __name__ == "__main__":
    try:
        bot.run('NDM0MTUyNTkxMjg3NTE3MjE0.DbiDKQ.YN6HKWYq5-7FTSHDPJe7JTrFgwA')
    except:
        pass
