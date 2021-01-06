import discord
from discord.ext import commands
import asyncio
import random

class remtoosmall(Exception):
    def __str__(self):
        return 'I don\'t think i can countdown in negative'


class InvalExcp(Exception):
    def __str__(self):
        return 'I think you put up a wrong assist there'

class Gen(commands.Cog, name='General'):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hi(self, ctx):
        s = ['Hi there','Hi there','Hi there','Hi there', 'Hello', 'Hello', 'Hello', 'Hello', 'Get lost don\'t wanna talk', 'Get lost don\'t wanna talk', 'Get lost don\'t wanna talk', 'Get lost don\'t wanna talk', 'Go to hell', 'Go to hell', 'Go to hell', 'Go to hell']
        i = random.randint(0,15)
        await ctx.send(s[i])

    @commands.command()
    async def howareyou(self, ctx):
        await ctx.send('I am fine') 
        await ctx.send('What about you?')

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'ping:{round(self.bot.latency*1000)}ms')


    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def tell(self, ctx, *, msg):
        embed = discord.Embed(
            title="title",
            description=msg,
            color=discord.Color.red()
        )
        embed.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
        embed.add_field(name = 'field1', value='field value', inline = True)
        embed.add_field(name = 'field2', value='field value2', inline = True)
        embed.add_field(name = 'field3', value='field value3', inline = False)
        embed.set_footer(text='this is footer')
        embed.set_image(url = ctx.guild.icon_url)
        embed.set_thumbnail(url = ctx.guild.icon_url)
        await ctx.send(embed=embed)

    @tell.error
    async def tell_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('XXXNo argument specifiedXXX')
        if isinstance(error, commands.MissingPermissions):
            await ctx.send('XXXMissing permissionsXXX')


    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def embed(self, ctx, *, msg):
        await ctx.message.delete()
        await ctx.send(embed=self.say(msg, 'blue'))

    @embed.error
    async def embed_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('XXXNo argument specifiedXXX')
        if isinstance(error, commands.MissingPermissions):
            await ctx.send('XXXMissing permissionsXXX')


    @commands.command()
    async def invite(self, ctx):
        await ctx.send('`The feature is stil in development`')




    @commands.command()
    async def timer(self, ctx, s, *, msg='None'):
        try:
            t = float(s[:-1])
            if s[-1]=='h':
                t*=60*60
            elif s[-1]=='m':
                t*=60
            elif s[-1]=='s':
                t*=1
            else:
                raise InvalExcp
            if t<=0:
                raise remtoosmall
            message = await ctx.send(f'timer set for {t} seconds')
            while True:
                t=t-1
                if t<0:
                    await message.edit(content='timer has ended')
                    break
                await message.edit(content=f'time remaining:{t}')
                await asyncio.sleep(1)
            await ctx.send(f"{ctx.author.mention} you timer of {s} seconds has ended: **{msg}**")
        except InvalExcp:
            await ctx.send(str(InvalExcp))
        except remtoosmall:
            await ctx.send(str(remtoosmall))
        except:
            await ctx.send('The value is not an integer')
    
    @commands.command()
    async def spam(self, ctx, num :int, t:int, *,text):
        await ctx.channel.purge(limit=1)
        role = discord.utils.get(ctx.guild.roles, name='Moderator')
        print(str(ctx.author))
        if role in ctx.author.roles:
            while num>0:
                num -= 1
                await ctx.send(text)
                await asyncio.sleep(t)        

    def say(self, msg, color):
        if color=='red':
            cl = discord.Color.red()
        elif color=='blue':
            cl = discord.Color.blue()
        else:
            cl = discord.Color.green()
        embed = discord.Embed(
            description = msg,
            color = cl
        )
        return embed

def setup(bot):
    bot.add_cog(Gen(bot))
    print('General cog is loaded')