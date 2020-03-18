import base64
import binascii
import collections
import string
import urllib.parse
from piping import *
import discord
import cipher
from discord.ext import commands
    
#TODO: Piping,RSA...
def pipline(encode_or_decode="decode",message=None,pipelist=None):
    for i in pipelist:
        if i == 'rot':
            decoded= rot_p(encode_or_decode, message)
        elif i == 'hex':
            decoded= hex_p(encode_or_decode, message)
        elif i == 'binary':
            decoded= bin_p(encode_or_decode, message)
        elif i == 'url':
            decoded= url_p(encode_or_decode, message)
        elif i == 'atbash':
            decoded= atbash_p(encode_or_decode, message)


class EncodingDecoding(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def b64(self, ctx, encode_or_decode, string,pipe="none"):
   
        byted_str = str.encode(string)
        
        if encode_or_decode == 'decode':
            decoded = base64.b64decode(byted_str).decode('utf-8')
            if pipe != "none":
                print(pipe)
                more=pipe.split('|')
                decoded=pipline(encode_or_decode,decoded,more)
            await ctx.send(decoded)
        
        if encode_or_decode == 'encode':
            encoded = base64.b64encode(byted_str).decode('utf-8').replace('\n', '')
            if pipe != "none":
                more=pipe.split('|')
                encoded=pipline(encode_or_decode,encoded,more)
            await ctx.send(encoded)

    @commands.command()
    async def binary(self, ctx, encode_or_decode, string,pipe="none"):
   
        if encode_or_decode == 'decode':
            string = string.replace(" ", "")
            data = int(string, 2)
            decoded = data.to_bytes((data.bit_length() + 7) // 8, 'big').decode()
            if pipe != "none":
                more=pipe.split('|')
                decoded=pipline(encode_or_decode,decoded,more)
            await ctx.send(decoded)
        
        if encode_or_decode == 'encode':
            encoded = bin(int.from_bytes(string.encode(), 'big')).replace('b', '')
            if pipe != "none":
                more=pipe.split('|')
                encoded=pipline(encode_or_decode,encoded,more)
            await ctx.send(encoded)

    @commands.command()
    async def hex(self, ctx, encode_or_decode, string,pipe="none"):
   
        if encode_or_decode == 'decode':
            string = string.replace(" ", "")
            decoded = binascii.unhexlify(string).decode('ascii')
            if pipe != "none":
                more=pipe.split('|')
                decoded=pipline(encode_or_decode,decoded,more)
            await ctx.send(decoded)
        
        if encode_or_decode == 'encode':
            byted = string.encode()
            encoded = binascii.hexlify(byted).decode('ascii')
            if pipe != "none":
                more=pipe.split('|')
                encoded=pipline(encode_or_decode,encoded,more)
            await ctx.send(encoded)

    @commands.command()
    async def url(self, ctx, encode_or_decode, message,pipe="none"):

        if encode_or_decode == 'decode':
            
            if '%20' in message:
                message = message.replace('%20', '(space)')
                decoded=urllib.parse.unquote(message)
                if pipe != "none":
                    more=pipe.split('|')
                    decoded=pipline(encode_or_decode,decoded,more)
                await ctx.send(decoded)
            else:
                decoded=urllib.parse.unquote(message)
                if pipe != "none":
                    more=pipe.split('|')
                    decoded=pipline(encode_or_decode,decoded,more)
                await ctx.send(decoded)
        
        if encode_or_decode == 'encode':
            encoded=urllib.parse.quote(message)
            if pipe != "none":
                more=pipe.split('|')
                encoded=pipline(encode_or_decode,encoded,more)
            await ctx.send(encoded)

def setup(bot):
    bot.add_cog(EncodingDecoding(bot))
