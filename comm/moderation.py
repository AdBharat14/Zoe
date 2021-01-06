import discord
from discord.ext import commands
import asyncio

class Mod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, msg : int):
        await ctx.channel.purge(limit = msg+1)

    @clear.error
    async def clear_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            msg = 'Number of message not specified'
        if isinstance(error, commands.MissingPermissions):
            msg = 'You don\'t have that permission lol'
        if isinstance(error, commands.BotMissingPermissions):
            msg = 'Bot is missing the the manage message permission' 
        await ctx.send(embed=self.say(msg, 'red'))


    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        try:
            await member.kick(reason=reason)
            await ctx.send(embed=self.say(f'{member.name} has been kicked for {reason}', 'red'))
        except discord.errors.Forbidden:
            await ctx.send(embed=self.say('XXXCan\'t kick that user he/she is more importantXXX', 'red'))
        except Exception as e:
            await ctx.send(embed=self.say(str(e),'red'))

    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(embed=self.say('Error:User not specified', 'red'))
        if isinstance(error, commands.MemberNotFound):
            await ctx.send(embed=self.say('Error:User not found', 'red'))
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(embed=self.say('Error:you don\'t have permissions', 'red'))
        if isinstance(error, commands.BotMissingPermissions):
            await ctx.send(embed=self.say('Error:Bot doesn\'t have kick permission','red'))

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        try:
            await member.ban(reason=reason)
            await ctx.send(sembed = self.say(f'{member.name} has been banned for {reason}', 'red'))
        except discord.errors.Forbidden:
            await ctx.send(embed=self.say('XXXCan\'t ban that user he is more importantXXX', 'red'))
        except Exception as e:
            await ctx.send(embed=self.say(str(e),'red'))

    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(embed=self.say('Error:User not specified', 'red'))
        if isinstance(error, commands.MemberNotFound):
            await ctx.send(embed=self.say('Error:User not found', 'red'))
        if isinstance(error, commands.BotMissingPermissions):
            await ctx.send(embed=self.say('Error:Bot doesn\'t have ban permission','red'))

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, *, member):
        if '#' in member:
            mem_name, mem_discr = member.split('#')
            banned_users = await ctx.guild.bans()
            for ban_entry in banned_users:
                user = ban_entry.user

                if (user.name, user.discriminator) == (mem_name, mem_discr):
                    await ctx.guild.unban(user)
                    await ctx.send(embed = self.say(f'{member} has been unbanned', 'blue'))
                    break
            else:
                await ctx.send(embed = self.say(f'{member} can\'t be found in banned list', 'red'))
        else:
            await ctx.send(embed = self.say('Invalid: Please provide a discriminator', 'red'))

    @unban.error
    async def unban_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(embed = self.say('You don\'t have unban permissions', 'red'))
        if isinstance(error, commands.BotMissingPermissions):
            await ctx.send(embed = self.say('Bot doesn\'t has permission to unban', 'red'))
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(embed = self.say('Enter a valid user name', 'red'))
    
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
    bot.add_cog(Mod(bot))
    print('Mod cog is loaded')