from discord.ext import commands
import discord
from discord.utils import get
import asyncio
import time
import math
import json
muted = []
black_listed_words = []
muted_users = []
class Moderation(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
  
  @commands.command()
  @commands.has_permissions(kick_members=True)
  async def kick(self, ctx, member: discord.Member = None, *,  reason=None):
    if member is None:
      await ctx.reply("please mention the user you wanna kick")
      return
    if reason is None:
     await member.kick(reason=reason)
     await ctx.send(f"{ctx.author.name} has kicked {member.name} reason: No reason specified")
    else:
     await member.kick(reason=reason)
     await ctx.send(f"{ctx.author.name} has kicked {member.name} reason: {reason}")
  @commands.command()
  @commands.has_permissions(ban_members=True)
  async def ban(self, ctx, member: discord.Member = None, *, reason=None):
    if member is None:
      await ctx.reply("please mention a member you want to ban")
      return
    if reason is None:
      await member.ban(reason=reason)
      await ctx.send(f"{ctx.author.name} has banned {member.name} reason: reason is not specified")
    else:
      await member.ban(reason=reason)
      await ctx.send(f"{ctx.author.name} has banned {member.name} reason: {reason}")
  @commands.command()
  @commands.has_permissions(administrator=True)
  @commands.guild_only()
  async def unban(self, ctx, user: discord.User):
    await ctx.guild.unban(user)
    await ctx.send(f"{ctx.author.name} has unbanned {user.name}")
  
  @commands.command()
  @commands.has_permissions(administrator=True)
  async def mute(self, ctx, member: discord.Member):
     if member.id in muted:
       await ctx.reply("user is already muted")
       return
     muted.append(member.id)
     muted_users.append(member.name)
     await ctx.send(f"{ctx.author.name} has muted {member.name}, do the command a!unmute [mention the user you wanna unmute] to unmute the user")
  
  @commands.command()
  async def unmute(self, ctx, member: discord.Member):
     if ctx.author.id in muted:
       await ctx.reply("you cant use this command you're muted")
       return
     if member.id not in muted:
       await ctx.reply("the user you mentioned is not muted")
       return
     muted.remove(member.id)
     muted_users.remove(member.name)
     await ctx.reply(f"succesfully unmuted {member.name}")
  

 
  @commands.Cog.listener()
  async def on_message(self, message):
    if message.content in black_listed_words:
     await message.reply("bro said a banned word")
     await message.delete()
  
  @commands.Cog.listener()
  async def on_message(self, message):
     if message.author.id in muted:
       msg = await message.reply("you're muted")
       await message.delete()
       await asyncio.sleep(4)
       await msg.delete()
  #black_listed_words
  @commands.command()
  async def blacklistwords(self, ctx, arg1 = None, arg2 = None, arg3 = None, arg4 = None):
      if arg2 is None and arg3 is None:
       black_listed_words.append(arg1)
       await ctx.send("succesfully added {} to the blacklisted words list, the list is now: {}".format(arg1, " , ".join(black_listed_words)))
      elif arg3 is None:
       black_listed_words.append(arg1)
       black_listed_words.append(arg2)
       await ctx.send("succesfully added {} and {} to the blacklisted words list, the list is now: {}".format(arg1, arg2, " , ".join(black_listed_words))) 
  
      else:
       black_listed_words.append(arg1)
       black_listed_words.append(arg2)
       black_listed_words.append(arg3)
       await ctx.send("succesfully added {} and {} and {}to the blacklisted words list, the list is now: {}".format(arg1, arg2, arg3, " , ".join(black_listed_words)))  
  
      
      
 

  @commands.command()
  async def blacklistedwords(self, ctx):
      if len(black_listed_words) == 0:
       await ctx.send("Theres currently no blacklisted words")
       return
      await ctx.send("the blacklisted words are: {}".format(" , ".join(black_listed_words))) 
  @commands.command()
  async def mutedusers(self, ctx):
    if len(muted_users) == 0:
      await ctx.send("theres currently no muted users")
    else:
      await ctx.send("the muted users are: {}".format(" , ".join(muted_users)))

stocks = ["Bitcoin", "Ethereum"]
stocks_test = {
  
}


class Market_economy(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
  @commands.command()
  async def stockmarket(self, ctx):
    embed = discord.Embed(title="The Stock Market", description="Do the command a!stockmarketbuy {stockname} , to buy a stock...")
    embed.add_field(name="Bitcoin", value="Bitcoin price and value today: 21,375.80 usd")
    embed.add_field(name="Ethereum", value="Ethereum price and value today: 1,238.18 usd")
    await ctx.send("Note: The prices will change every 24 hours or less", embed=embed)
    
  @commands.command()
  async def stockmarketbuy(self, ctx, stock=None):
    if stock is None:
      await ctx.reply("pls put a stock")
      return
    if stock not in stocks:
      await ctx.reply("this stock doesent exist the stocks are: {}".format(" , ".join(stocks)))
      return
    await ctx.send(f"succesfully bought {stock} ")
    stocks_test[f"stocks of: {ctx.author.id}, {ctx.author.name}"] = stock
    print(stocks_test)

async def setup(bot):
  await bot.add_cog(Moderation(bot))
  await bot.add_cog(Market_economy(bot))
