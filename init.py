import asyncio
import random
from colorama import Back, Fore, Style
import sys
import os
import discord
from discord.ext.commands import Bot
from discord.ext import commands
import help_info
import auth

#Auth is set up like so:
#auth_token = 'DISCORD TOKEN'
#conn = "mongodb+srv://MONGODBUSER:PASSWORD@YOURCLUSTER.mongodb.net"



client = discord.Client()
bot = commands.Bot(command_prefix='>')
extensions = ['encoding_decoding', 'cipher', 'ctfs', 'utility']
bot.remove_command('help')
blacklisted = []
cool_names = ['_Wh1t3r0se_#7515', 'BlackCoffee#2718', 'a.lil.sus#7939'] 
# This is intended to be able to be circumvented.
# If you do something like report a bug on  GITHUB.

@bot.event
async def on_ready():
    print(('<' + bot.user.name) + ' Online>')
    print(f"discord.py {discord.__version__}\n")
    await bot.change_presence(activity=discord.Game(name='>help'))

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Invalid command passed.  Use >help")
    else:
        await ctx.send(f"There was an error, sorry!\nIf you think this should be fixed, report it with >report \"what happened\"")
    
    print(Style.BRIGHT + Fore.RED + f"Error occured with: {ctx.command}\n{error}\n")
    print(Style.RESET_ALL)


# Sends the github link.
@bot.command()
async def source(ctx):
    await ctx.send(help_info.src)

@bot.command()
async def help(ctx, page=None):
    
    if page == 'ctftime':
        emb = discord.Embed(description=help_info.ctftime_help, colour=4387968)
        emb.set_author(name='CTFTime Help')
    elif page == 'utility':
        emb = discord.Embed(description=help_info.utility_help, colour=4387968)
        emb.set_author(name='Utilities Help')
    
    else:
        emb = discord.Embed(description=help_info.help_page, colour=4387968)
        emb.set_author(name='Werewolf.exe')
    
    await ctx.channel.send(embed=emb)

@bot.command()
async def amicool(ctx):
    authors_name = str(ctx.author)
    if any((name in authors_name for name in cool_names)):
        await ctx.send('You are very cool')
    else:
        await ctx.send('lolno')
        await ctx.send('Psst, kid.  Want to be cool?  Find an issue and report it or request a feature you think would be cool.')

if __name__ == '__main__':
    sys.path.insert(1, os.getcwd() + '/cogs/')
    for extension in extensions:
        bot.load_extension(extension)
    bot.run(auth.auth_token)
