import discord
from discord.ext import commands

intents=discord.Intents.default()
intents.message_content=True
bot=commands.Bot(command_prefix='/',intents=intents)


#success log message
@bot.event
async def on_ready():
    print("Logged on as", bot.user)

# messages replies
@bot.event
async def on_message(message):
    if message.author==bot.user:
        return
    
    if message.content.lower()=="slm":
        await message.channel.send("sup")

    if "dance" in message.content.lower():
        await message.channel.send('https://tenor.com/bUrwp.gif')

    if "peace" in message.content.lower():
        await message.channel.send('https://tenor.com/bjRCF.gif')
        
    await bot.process_commands(message)



@bot.command()
async def hello(ctx):
    await ctx.send('https://tenor.com/bUrwp.gif')

@bot.command()
async def pingd(ctx):
    await ctx.send(bot.latency*1000)


# Admin commands

#clear cmd
@bot.command()
@commands.has_permissions(administrator=True)
async def clear(ctx , amount:int=None):
    if(not amount):
        await ctx.send("3emer l'amount libaghi tmse7 ")
        return
    elif(amount>10):
        await ctx.send("Max 10 characters ")
        return
    # +1 delete the cmd itself     
    await ctx.channel.purge(limit=amount+1)     





bot.run('Put your token here')



