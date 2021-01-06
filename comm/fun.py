import discord
from discord.ext import commands
import asyncio
import random
from discord.utils import get

class Fun(commands.Cog, name = 'Fun'):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ace(self, ctx):
        s = ['pro', 'pro', 'blush', 'coder', 'My owner','My owner','My owner','coder','coder','coder']
        i = random.randint(0,8)
        await ctx.send(s[i])

    @commands.command()
    async def sonia(self, ctx):
        s = ['egg excl master', 'pro', 'pro', 'Bony','egg excl master','egg excl master','Bony','never ;r d!','never ;r d!']
        i = random.randint(0,8)
        await ctx.send(s[i])

    @commands.command()
    async def Justice(self, ctx):
        s = ['Lucky', 'Pro', 'Biggest simp :KeKw:', 'shiny ray and shiny arc','Biggest simp :KeKw:','Biggest simp :KeKw:','Lucky','Lucky','Pro','Pro','shiny ray and shiny arc']
        i = random.randint(0,10)
        await ctx.send(s[i])

    @commands.command()
    async def kei(self, ctx):
        s = ['sells everything', 'QT', 'QT', 'pro', 'pro', 'mikasa!','sells everything','sells everything','sells everything','QT','QT','QT','mikasa!','mikasa!']
        i = random.randint(0,13)
        await ctx.send(s[i])

    @commands.command()
    async def smile(self, ctx):
        s = ['lurk', 'lurk', 'frown', 'biggest noob', 'baka']
        i = random.randint(0,4)
        await ctx.send(s[i])

    @commands.command()
    async def nbroll(self, ctx, num=100):
        if num<0:
            await ctx.send('What do you even want me to roll with that')
        elif num<100000000000:
            i = random.randint(0,num)
            s = str(i)+'(0-'+str(num)+')'
            await ctx.send(s)
        else:
            await ctx.send('Number too large to process')

    @nbroll.error
    async def nbroll_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send(embed=self.say('What do you even want me to roll with that','red'))
    
    @commands.command()
    async def roll(self, ctx, num=100):
        if num<0:
            await ctx.send('What do you even wanna roll with that')
        elif num<=10000:
            role = discord.utils.get(ctx.guild.roles, name='Helper')
            r=0
            if role in ctx.author.roles:
                a = list(range(0,num))
                b = list(range(int(num/4),num))
                a = b+a
                if(num%2==1):
                    i=random.randint(0,len(a)-1)
                else:
                    i=random.randint(0,len(a)-1)
                r=a[i]
            else:
                a = list(range(0,num))
                b = list(range(0,int(num/4)))
                a = a+b
                i=random.randint(0,len(a)-1)
                r=a[i]
            await ctx.send(f'**{r}** (0-{num})')
        else:
            await ctx.send('Number too large to process')

    @commands.command()
    async def choose(self, ctx, *, s):
        l = s.split()
        n=len(l)
        i = random.randint(0,n-1)
        await ctx.send(l[i])

    @choose.error
    async def choose_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(embed=self.say('What do you even want me to choose from','red'))


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
    bot.add_cog(Fun(bot))
    print('Fun cog is loaded')