import collections
import string
import discord
from discord.ext import commands

class Ciphers(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def rot(self, ctx, message, pipe="none"):
        allrot = ''
        
        for i in range(0, 26):
            upper = collections.deque(string.ascii_uppercase)
            lower = collections.deque(string.ascii_lowercase)
            
            upper.rotate((- i))
            lower.rotate((- i))
            
            upper = ''.join(list(upper))
            lower = ''.join(list(lower))
            translated = message.translate(str.maketrans(string.ascii_uppercase, upper)).translate(str.maketrans(string.ascii_lowercase, lower))
            allrot += '{}: {}\n'.format(i, translated)
            decoded=f"{allrot}"
        if pipe != "none":
            more=pipe.split('|')
            decoded=pipline(encode_or_decode,decoded,more)
            await ctx.send(decoded)

    @commands.command()
    async def atbash(self, ctx, message,pipe="none"):
        normal = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        changed = 'zyxwvutsrqponmlkjihgfedcbaZYXWVUTSRQPONMLKJIHGFEDCBA'
        trans = str.maketrans(normal, changed)
        decoded = message.translate(trans)
        if pipe != "none":
                more=pipe.split('|')
                decoded=pipline(encode_or_decode,decoded,more)
        await ctx.send(decoded)

def setup(bot):
    bot.add_cog(Ciphers(bot))
