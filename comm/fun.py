import discord
from discord.ext import commands
import asyncio
import random
from discord.utils import get

class Fun(commands.Cog, name = 'Fun'):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def about(self, ctx, *, s):
        l=s.split()
        if l[0]=='set':
            role = discord.utils.get(ctx.guild.roles, name='Moderator')
            if role in ctx.author.roles:
                with open('about.txt','a+') as f:
                    if self.check(l[1]):
                        self.dlt(l[1])
                    s1=' '.join(l[2:])
                    s1=l[1]+':'+s1+'\n'
                    f.write(s1)
            else:
                await ctx.send('Try again when you have perms')
        else:
            with open('about.txt','r') as f:
                for line in f:
                    l1=line.split(':')
                    if s==l1[0]:
                        s1=':'.join(l1[1:])
                        l2=s1.split(' ')
                        i = random.randint(0,len(l2)-1)
                        await ctx.send(l2[i])
                        break
                else:
                    await ctx.send('Data Not found')

    def check(self, s):
        with open('about.txt','r') as f:
            for line in f:
                l1=line.split(':')
                if s==l1[0]:
                    return True
        return False

    def dlt(self, s):
        lines = ''
        with open('about.txt','r') as f:
            lines=f.read()
        with open('about.txt','w') as f:
            for line in lines.splitlines():
                l1=line.split(':')
                if s!=l1[0]:
                    f.write(line+'\n')


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