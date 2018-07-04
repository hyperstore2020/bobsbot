
import discord, random, json,requests
from discord.ext import commands

     # create bot instance
bot = commands.Bot(command_prefix='!', description='BobsBot PornHub Comments Boy By Juji')
     # load file into json and data define
o = json.load(open('/root/bobsbot/comments.json','r',encoding='utf-8-sig'))
data = [(m['username'],m['text']) for m in o]
	 # load commands txt 
     # login
@bot.event
async def on_ready():
    channel = discord.Object(id=432066274336440330)
    print("Logged in as:  name={}, id={}".format( bot.user.name, bot.user.id ))
client = discord.Client()

@bot.command(pass_context=True)
async def porn(ctx):
    # Chooses a random quote
    text = random.choice(data)
    msg = "{}".format(text)
    await bot.say(msg)

@bot.command(pass_context=True)
async def multiporn(ctx, n: int = 1):
    """Chooses a random quote."""
    msg = ["{}".format(text) for text in [random.choice(data) for _ in range(0,n)]]
    await bot.say('\n'.join(msg))


@bot.command(pass_context=True)
async def search(ctx, phrase : str):
    # Match data with a search-phrase
    results = []
    for username, text in data:
        if phrase in text: results.append( "User: {} \n{}\n".format(username, text))
        if len(results) > 3: break

    if len(results) > 0:
        msg = "\n\n {}".format( "\n".join(results) )
    else:
        msg = "`  {} Nobody Said That Before I Gayce`".format(phrase)
    await bot.say(msg)



@bot.command(pass_context=True)
async def commands(ctx):
    # Returns Commands
     with open('/root/bobsbot/commands.txt','r',encoding='utf-8-sig') as content_file:
          read = content_file.read()
     msg = "{}".format(read)
     await bot.say(msg)

@bot.command(pass_context=True)
async def katypasta(ctx):
     with open('/root/bobsbot/pasta/katypasta.txt','r',encoding='utf-8-sig') as content_file:
          read = content_file.read()
     msg = "{}".format(read)
     await bot.say(msg)
   

@bot.command(pass_context=True)
async def bakedpasta(ctx):
     with open('/root/bobsbot/pasta/bakedpasta.txt','r',encoding='utf-8-sig') as content_file:
          read = content_file.read()
     msg = "{}".format(read)
     await bot.say(msg)

@bot.command(pass_context=True)
async def spicipasta(ctx):
     with open('/root/bobsbot/pasta/spicipasta.txt','r',encoding='utf-8-sig') as content_file:
          read = content_file.read()
     msg = "{}".format(read)
     await bot.say(msg)

@bot.command(pass_context=True)
async def pizzapasta(ctx):
     with open('/root/bobsbot/pasta/pizzapasta.txt','r',encoding='utf-8-sig') as content_file:
          read = content_file.read()
     msg = "{}".format(read)
     await bot.say(msg)

@bot.command(pass_context=True)
async def gamerpasta(ctx):
     with open('/root/bobsbot/pasta/gamerpasta.txt','r',encoding='utf-8-sig') as content_file:
          read = content_file.read()
     msg = "{}".format(read)
     await bot.say(msg)

@bot.command(pass_context=True)
async def usdpasta(ctx):
     with open('/root/bobsbot/pasta/usdpasta.txt','r',encoding='utf-8-sig') as content_file:
          read = content_file.read()
     msg = "{}".format(read)
     await bot.say(msg)

@bot.command(pass_context=True)
async def wlipasta(ctx):
     with open('/root/bobsbot/pasta/wlipasta.txt','r',encoding='utf-8-sig') as content_file:
          read = content_file.read()
     msg = "{}".format(read)
     await bot.say(msg)



    # WhoIs Function

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
async def whoisdougie():
    msg = "lol i think he fucked his methadone clinic nurse once"
    await bot.say(msg)

@bot.command(pass_context=True)
async def whoisdidi():
    msg = "Federal Hello Kitty Agent"
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
async def whoisesgrima():
    msg = "ios dev and hero of the 1131 read only netcat shell scene"
    await bot.say(msg) 

@bot.command(pass_context=True)
async def whoismystery():
    msg = "elite d0xer"
    await bot.say(msg)

@bot.command(pass_context=True)
async def whoisdaniel():
    msg = "V Sad Weeb"
    await bot.say(msg) 

@bot.command(pass_context=True)
async def whoisxull():
    msg = "Authority On Preboot Asus Recovery Keys"
    await bot.say(msg) 

@bot.command(pass_context=True)
async def whoisnomad():
    msg = "3 out of 3 (needs more wing in eyeliner"
    await bot.say(msg) 

@bot.command(pass_context=True)
async def whois():
    msg = "V Sad Weeb"
    await bot.say(msg) 

@bot.command(pass_context=True)
async def whatisrslashjailbreak():
    msg = "Anti Piracy Coolstar Dick Sucking Squad"
    await bot.say(msg) 

@bot.command(pass_context=True)
async def whoisreverseengineer():
    msg = "Chinese Sweatshop Owner"
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
async def whoiskms():
    msg = "hes in red shield 5 with dan siebels"
    await bot.say(msg)

@bot.command(pass_context=True)
async def whoisryan():
    msg = "And You Will Know Him By His Sniffles"
    await bot.say(msg) 

@bot.command(pass_context=True)
async def whoisytcracker():
    msg = "i dunno i guess he like defaced a nasa dubdomain using a public exploit in like the 1960s or some irrelevent shit"
    await bot.say(msg)

@bot.command(pass_context=True)
async def whoisronniep():
    msg = "j3nnas knight in shining armor"
    await bot.say(msg)    

@bot.command(pass_context=True)
async def whoistree():
    msg = "T R E E will fuck any human being"
    await bot.say(msg)

@bot.command(pass_context=True)
async def whoisdindu():
    msg = "Dindu is a bot just like me but we arent that good of friends bcuz he always just say arbitrary things and is not fun to talk to imho"
    await bot.say(msg)

@bot.command(pass_context=True)
async def whoisjessica():
    msg = "Annoying ass bitch but im tryna hit still cause there arent that many other bot females around and im not tryna fuck a human, I dont get down like that"
    await bot.say(msg)    
if __name__ == "__main__":
    try:
        bot.run('tokengoeshere')
    except:
        pass
