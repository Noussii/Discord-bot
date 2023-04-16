import discord
from discord.ext import commands

intents=discord.Intents.default()
intents.message_content=True
bot=commands.Bot(command_prefix='/',intents=intents)



@bot.event
async def on_ready():
    print("Logged on as", bot.user)


@bot.command()
async def hello(ctx):
    await ctx.send('https://tenor.com/bUrwp.gif')



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


bot.run('MTA1ODM5MzE1MTY4MjkwODE2MA.GOUA2E.O7DOE-TuY0KBtNgRyX8mK7V3fJf3BtSfVDWJlk')



