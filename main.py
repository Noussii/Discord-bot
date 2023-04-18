import discord
from discord.ext import commands

intents=discord.Intents.default()
intents.message_content=True
bot=commands.Bot(command_prefix='/',intents=intents)


#sucess log message-terminal
@bot.event
async def on_ready():
    print("Logged on as", bot.user)

# messages replys
@bot.event
async def on_message(message):
    if message.author==bot.user:
        return
    
    if message.content.lower()=="slm":
        await message.channel.send("Wa alykum salam")

    if "zahya" in message.content.lower():
        await message.channel.send('https://tenor.com/bUrwp.gif')

    if "cv" in message.content.lower():
        await message.channel.send('bekher hmdlh')
        
    await bot.process_commands(message)



@bot.command()
async def hello(ctx):
    await ctx.send('https://tenor.com/bUrwp.gif')

@bot.command()
async def pingd(ctx):
    await ctx.send(bot.latency*1000)


# Admin commands
@bot.command()
@commands.has_permissions(administrator=True)
async def mse7(ctx , amount:int=None):
    if(not amount):
        await ctx.send("3emer l'amount libaghi tmse7 ")
        return
    elif(amount>10):
        await ctx.send("Max houwa 10 characters ")
        return
    # amount +1 to delete the /cmd itself  ex: /clear 5 => 5msgs+1cmd     
    await ctx.channel.purge(limit=amount+1)     





bot.run('MTA1ODM5MzE1MTY4MjkwODE2MA.GOUA2E.O7DOE-TuY0KBtNgRyX8mK7V3fJf3BtSfVDWJlk')



