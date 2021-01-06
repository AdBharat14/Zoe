import discord
from discord.ext import commands
import asyncio

class Help(commands.Cog, name='help'):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def help(self, ctx, str=None):
        if str == 'hi':
            embed = discord.Embed(
                title='hi',
                description = 'type ``./hi`` in the text to get the bot response',
                color = discord.Color.purple()
            )
            await ctx.send(embed = embed)
        elif str == 'howareyou':
            embed = discord.Embed(
                title='howareyou',
                description = 'type ``./howareyou`` in the text to get the bot response',
                color = discord.Color.purple()
            )
            await ctx.send(embed = embed)
        elif str == 'invite':
            embed = discord.Embed(
                title='invite',
                description = 'type ``./invite`` to get a link to invite a bot and a link to join support server',
                color = discord.Color.purple()
            )
            await ctx.send(embed = embed)
        elif str == 'clear':
            embed = discord.Embed(
                title='clear',
                description = 'type ``./clear no_of_messages`` in the text to delete that number of messages(must have manage message permission)',
                color = discord.Color.purple()
            )
            await ctx.send(embed = embed)
        elif str == 'tell':
            embed = discord.Embed(
                title='tell',
                description = 'type ``./tell message`` to create an undeveloped embed',
                color = discord.Color.purple()
            )
            await ctx.send(embed = embed)
        elif str == 'embed':
            embed = discord.Embed(
                title='embed',
                description = 'type ``./embed text`` to get an embedded text',
                color = discord.Color.purple()
            )
            await ctx.send(embed = embed)
        elif str == 'kick':
            embed = discord.Embed(
                title='kick',
                description = 'type ``./kick username reason`` in the text to get the bot response',
                color = discord.Color.purple()
            )
            await ctx.send(embed = embed)
        elif str == 'ban':
            embed = discord.Embed(
                title='ban',
                description = 'type ``./ban username reason`` in the text to get the bot response',
                color = discord.Color.purple()
            )
            await ctx.send(embed = embed)
        elif str == 'unban':
            embed = discord.Embed(
                title='unban',
                description = 'type ``unban username with tag`` in the text to get the bot response',
                color = discord.Color.purple()
            )
            await ctx.send(embed = embed)
        else:
            embed = discord.Embed(
                title=None,
                description = '**Welcome to help**',
                color = discord.Color.purple()
            )
            embed.set_author(name = ctx.guild.me.display_name, icon_url = ctx.guild.me.avatar_url)
            embed.add_field(name = 'Basic', value = 'hi, howareyou, invite', inline = False)
            embed.add_field(name = 'Manage message', value = 'clear, tell, embed', inline = False)
            embed.add_field(name = 'Moderation', value = 'kick, ban, unban', inline = False)
            embed.set_footer(text = './help ``command`` for more info on command')
            await ctx.send(embed = embed)

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
    bot.add_cog(Help(bot))
    print('help cog is loaded')