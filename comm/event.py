import discord
from discord.ext import commands
import asyncio

class Welcome(commands.Cog,name='Welcome'):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("I am ready")

    @commands.Cog.listener()
    async def on_message(self, message):
        if self.bot.user.id != message.author.id:
            s = message.content
            s = s.lower()
            if 'happy new year' in s:
                mem_name, mem_discr = str(message.author).split('#')
                if mem_name!='ace' and mem_discr!='0314':
                    await message.channel.send(f'Wish you a happy new year\nMay this year bring joy and we hope you find a shiny darkrai and arceus\n-from Ace and Zoe')

    
    # @commands.Cog.listener()
    # async def on_member_join(self,member):
    #     channel = self.bot.get_channel(769817501781327882)
    #     channel2 = self.bot.get_channel(774922857825566720)
    #     channel3 = self.bot.get_channel(773980287801229352)
    #     ed = discord.Embed(description = f'Welcome {member.mention} to **Pokemon Grinding server**', color = discord.Color.green())
    #     ed.set_image(url=member.avatar_url)
    #     await channel.send(embed=ed)
    #     await channel.send(f'Be sure to read {channel2}\nGet self roles from {channel3}')

    # @commands.Cog.listener()
    # async def on_member_remove(self,member):
    #     channel = self.bot.get_channel(788407052098600960)
    #     await channel.send(f'user {member.mention} has left us \nWe hope you find golden arceus')

def setup(bot):
    bot.add_cog(Welcome(bot))
    print('Event cog loaded')