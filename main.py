
from discord.ext import commands, tasks
import datetime
from discord.ext.commands import MissingPermissions
import discord
import os
import random
from discord.utils import get
import youtube_dl
import asyncio
from discord.voice_client import VoiceClient
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from googletrans import Translator
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
from keep_alive import keep_alive

import string
import PIL
import Image
from io import BytesIO
from requests import get
import json
import aiohttp
import math

#pip install git+https://github.com/Rapptz/discord.py

gif = [
    "https://media.discordapp.net/attachments/969223004921925684/976401115216216095/77206f9ed25601b3579d53c1d737f0d6.gif",
    "https://media.discordapp.net/attachments/969223004921925684/976403532557189160/die-kill.gif",
    "https://media.discordapp.net/attachments/969223004921925684/976403890448760842/nichijou-minigun.gif",
    "https://media.discordapp.net/attachments/969223004921925684/976404455262146560/stewie-griffin-evil-plan.gif",
    "https://media.discordapp.net/attachments/969223004921925684/976404454951755796/ANu5.gif"
]

kil = [
    "is now in jail",
    "is now getting beaten up by the relatives of the person that he/she killed...",
    "is now crying because of guilt",
    "is now getting crucified by the town people while getting sacrificed to a demon",
    "is now dead because the person he/she killed pulled out the uno reverse",
    "is now thrown to the garbage truck by the police"
]

shit = [
    "ee oo ee oo", "uwu dis uwu dat", "idk now", "eiejsjsjjsd", "BRO IDK",
    "bread", "BREAD", "twurks", "i look like a frog aug"
]

score = [
    "1%", "2%", "3%", "4%", "5%", "10%", "15%", "20%", "25", "30%", "35%",
    "40%", "45%", "50%", "55%", "60%", "65%", "70%", "80%", "90%", "90%",
    "100%"
]

letter = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o",
    "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
]
ask = [
    "yes", "no", "never", "wtf yes ofcourse", "YES", "NOOO", "50/50",
    "im sorry but idk"
]

blacklisted_user = []
blacklisted_words = "fuck"




bot =  commands.Bot(command_prefix="a!", intents=intents, activity = discord.Activity(type=discord.ActivityType.watching, name="you always, prefix = a!"), status=discord.Status.do_not_disturb)



second = int(40)
kis = [  "https://media.discordapp.net/attachments/969451074320748585/976413785877254164/a039f48550983700394b558b89d2cad0.gif",
    "https://media.discordapp.net/attachments/969223004921925684/976418690104954900/2b5271e20fa65925e07d0338fa290135.gif",
    "https://media.discordapp.net/attachments/969223004921925684/976419107593396275/icegif-1008.gif",
    "https://media.discordapp.net/attachments/969223004921925684/976419450309967892/giphy_2.gif"
]

topic = [
    "how often do you cry", "whats more doors or wheels?",
    "what do you think of the person who made this bot",
    "would you rather still have the same look as your 11 year old self afer growing up or look like a 50 year old at an early age",
    "do you agree to the sentence that money grows on trees but it doesent grow on trees",
    "fun fact: theres a person looking at you right now (:"
]






@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(
            'This command is on cooldown, you can use it in 10 seconds')

  
@bot.event
async def on_ready():
    print(f'{bot.user} testbro is here!')
    user = await bot.fetch_user(f"{897320965724315739}")
    await user.send("bot is up and running :)")
    

  


@bot.command(pass_context=True)
async def int(ctx):
    if ctx.author.id in blacklisted_user:
       await ctx.send("you're blacklisted from using my commands...")
       return
    async with ctx.typing():
        await ctx.send("{} is the random integrer you got".format(
            random.randint(1, 1000001)))


@bot.command()
async def announce(ctx, *, data):
     if ctx.author.id in blacklisted_user:
       await ctx.send("you're blacklisted from using my commands...")
       return
     data = data.split('-')  # title = 0, desc = 1, footer=2
     embed = discord.Embed(title=f"{data[0]}",
                          description=f"{data[1]}",
                          color=0x00ff00)
     embed.set_footer(text=f"{data[2]}")
     await ctx.message.delete()
     await ctx.send(embed=embed)


@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def deletus(ctx, amount=5):
    if ctx.author.id in blacklisted_user:
       await ctx.send("you're blacklisted from using my commands...")
       return
    await ctx.message.delete()
    await ctx.channel.purge(limit=amount)



    

@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def avatar(ctx, *, avamember: discord.Member = None):
  if avamember == None:
    await ctx.send(ctx.message.author.avatar.url)
  else:
   userAvatarUrl = avamember.avatar.url
   await ctx.send(userAvatarUrl)


@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def askme(ctx):
    if ctx.author.id in blacklisted_user:
       await ctx.send("you're blacklisted from using my commands...")
       return
    await ctx.send(random.choice(ask))


@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def firstletter(ctx):
    if ctx.author.id in blacklisted_user:
       await ctx.send("you're blacklisted from using my commands...")
       return
    await ctx.send(random.choice(letter))


@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def rickroll(ctx):
    if ctx.author.id in blacklisted_user:
       await ctx.send("you're blacklisted from using my commands...")
       return
    await ctx.message.delete()
    await ctx.send(
        "We're no strangers to love You know the rules and so do I (do I) A full commitment's what I'm thinking of You wouldn't get this from any other guy I just wanna tell you how I'm feeling Gotta make you understand Never gonna give you up Never gonna let you down Never gonna run around and desert you Never gonna make you cry Never gonna say goodbye Never gonna tell a lie and hurt you"
    )


@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def addrole(ctx, member: discord.Member, role: discord.Role):
    if ctx.author.id in blacklisted_user:
       await ctx.send("you're blacklisted from using my commands...")
       return
    await member.add_roles(role)


@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def shouldi(ctx):
    if ctx.author.id in blacklisted_user:
       await ctx.send("you're blacklisted from using my commands...")
       return
    await ctx.send(random.choice(ask))


@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def topics(ctx):
    if ctx.author.id in blacklisted_user:
       await ctx.send("you're blacklisted from using my commands...")
       return
    await ctx.send(random.choice(topic))


@bot.command()
async def poll(ctx, *, message):
    if ctx.author.id in blacklisted_user:
       await ctx.send("you're blacklisted from using my commands...")
       return
    embed = discord.Embed(title=f'Poll by {ctx.author}',
                          description=f'{message}')
    msg = await ctx.send(embed=embed)

    emoji = '\N{THUMBS UP SIGN}'
    await msg.add_reaction(emoji)
    emoji = '\N{THUMBS DOWN SIGN}'
    await msg.add_reaction(emoji)
    emoji = '1⃣'
    await msg.add_reaction(emoji)
    emoji = '2⃣'
    await msg.add_reaction(emoji)


@bot.command()
async def randomshit(ctx):
    if ctx.author.id in blacklisted_user:
       await ctx.send("you're blacklisted from using my commands...")
       return
    embed = discord.Embed(title='randomshit', description=random.choice(shit))
    msg = await ctx.send(embed=embed)


@bot.command(pass_context=True)
@commands.cooldown(1, 10, commands.BucketType.user)
async def change(ctx, member: discord.Member, *, arg):
    if ctx.author.id in blacklisted_user:
       await ctx.send("you're blacklisted from using my commands...")
       return
    await member.edit(nick=arg)
    await ctx.send(f'Nickname was changed for {member.mention} ')


@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def ship(ctx, member: discord.Member, member2: discord.Member):
    if ctx.author.id in blacklisted_user:
       await ctx.send("you're blacklisted from using my commands...")
       return
    await ctx.send('{} shipped {} and {} the score is: {}'.format(
        ctx.author, member, member2, random.choice(score)))


@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def ytsearch(ctx, *, arg):
  if ctx.author.id in blacklisted_user:
       await ctx.send("you're blacklisted from using my commands...")
       return
  await ctx.send(     "https://m.youtube.com/results?sp=mAEA&search_query={}".format(arg))


@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def googlsearch(ctx, *, arg):
    if ctx.author.id in blacklisted_user:
       await ctx.send("you're blacklisted from using my commands...")
       return
    await ctx.send(
        "https://www.google.com/search?q={}&oq={}&aqs=chrome..69i57j69i60j69i65l3j69i60j69i59l2.5829j0j4&client=ms-android-vivo&sourceid=chrome-mobile&ie=UTF-8"
        .format(arg, arg))


@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def urban(ctx, *, arg):
    if ctx.author.id in blacklisted_user:
       await ctx.send("you're blacklisted from using my commands...")
       return
    await ctx.send(
        "https://www.urbandictionary.com/define.php?term={}".format(arg))


@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def anime(ctx, *, arg):
    if ctx.author.id in blacklisted_user:
       await ctx.send("you're blacklisted from using my commands...")
       return
    await ctx.send("https://anilist.co/search/anime?search={}".format(arg))


@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def wiktionary(ctx, *, arg):
    if ctx.author.id in blacklisted_user:
       await ctx.send("you're blacklisted from using my commands...")
       return
    await ctx.send("https://en.m.wiktionary.org/wiki/{}".format(arg))


@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def fbsearch(ctx, *, arg):
    if ctx.author.id in blacklisted_user:
       await ctx.send("you're blacklisted from using my commands...")
       return
    await ctx.send(
        "https://m.facebook.com/search/top/?q={}&ref=content_filter&tsid=0.43213277209413836&source=typeahead"
        .format(arg))


@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def wiki(ctx, *, arg):
    if ctx.author.id in blacklisted_user:
       await ctx.send("you're blacklisted from using my commands...")
       return
    await ctx.send("https://en.m.wikipedia.org/wiki/{}".format(arg))


@bot.command(pass_context=True)
@commands.cooldown(1, 10, commands.BucketType.user)
async def kill(ctx, *, arg):
    if ctx.author.id in blacklisted_user:
       await ctx.send("you're blacklisted from using my commands...")
       return
    embed = discord.Embed(
        title="{} killed {}".format(ctx.message.author.display_name, arg),
        description="{} {}".format(ctx.message.author.display_name,
                                   random.choice(kil)))
    embed.add_field(
        name="fly high {}".format(arg),
        value="may your soul fly too high and falll back to the trashcan",
        inline=False)
    await ctx.send(embed=embed)
    await ctx.send(random.choice(gif))

@bot.command(pass_context=True)
@commands.cooldown(1, 10, commands.BucketType.user)
async def kiss(ctx, *, arg):
    if ctx.author.id in blacklisted_user:
       await ctx.send("you're blacklisted from using my commands...")
       return
    embed = discord.Embed(
        title="{} kissed {}".format(ctx.message.author.display_name, arg),
        description="{} is now blushing from that romantic kiss...".format(
            arg))
    await ctx.send(embed=embed)
    await ctx.send(random.choice(kis))


class Buttons(discord.ui.View):
    def __init__(self, *, timeout=180):
        super().__init__(timeout=timeout)

    @discord.ui.button(label="yes",style=discord.ButtonStyle.danger)
    async def blurple_button(self,button:discord.ui.Button,interaction:discord.Interaction):
     interaction.disabled = True    
     interaction.style=discord.ButtonStyle.green
     await button.response.edit_message(content=f"sike,boi you thought i'd let you kill yourself :)",view=self)
    
    @discord.ui.button(label="no",style=discord.ButtonStyle.green)
    async def red_button(self,button:discord.ui.Button,interaction:discord.Interaction):
        
        await button.response.send_message("WEW LESGO NO KILLING YOURSELF")
        interaction.disabled = True
@bot.command()
async def killmyself(ctx):
    if ctx.author.id in blacklisted_user:
       await ctx.send("you're blacklisted from using my commands...")
       return
    view=Buttons()
    await ctx.send("are you sure? ):",view=view) 

afk_list = []
reason_list = []
afk_name = []

@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def stopafk(ctx):
  if ctx.author.id in blacklisted_user:
       await ctx.send("you're blacklisted from using my commands...")
       return
  await ctx.message.author.edit(nick=ctx.message.author.name)
  await ctx.send("succesfully stopped being afk :)")
  reason_list.pop() 
  afk_name.remove(ctx.message.author.name)


dm_id = []
useronly = []
@bot.command()
async def dm(ctx, user: discord.User, *, message=None):
    if ctx.author.id in blacklisted_user:
       await ctx.send("you're blacklisted from using my commands...")
       return
    if ctx.author.id != 897320965724315739:
      await ctx.reply("only my owner can use this command")
      return
    message = message or "This Message is sent via DM"
    await user.send(message)
    embed = discord.Embed(title="Bot conversation", description="please do the command a!dmreply and the message you're gonna reply, so the bot can reply to you :)")
    if user.id in dm_id:
      await ctx.reply(f"succesfully messaged {user.name}")
      print(dm_id)
    elif user.id not in dm_id:
     dm_id.append(user.id)
     dm_id.append(user.name)
     await ctx.reply(f"succesfully messaged {user.name}")
     print(dm_id)
    await asyncio.sleep(3)
    await user.send(embed=embed)
    

@bot.command()
async def dmreply(ctx, *, message = None):
  if isinstance(ctx.channel, discord.channel.DMChannel):
   if message is None:
    await ctx.reply("pls put a message")
    return
   if ctx.author.id not in dm_id:
     await ctx.reply("you havent got dmd by the bot so you cant use this command or the bot stopped the convo and your replies can no longer be seened by the bot until it starts another convo") 
     return
   user = await bot.fetch_user(897320965724315739)
   embed = discord.Embed(title="replied to bot", description=f"{ctx.author.name} is the author of the reply ")
   embed.add_field(name="The message is: ", value=message)
   embed.add_field(name="Author's id: ",value=ctx.author.id)
   await user.send(embed=embed)
   await ctx.reply("succesfully replied, please wait for the response")
   

@bot.command()
async def stopconvo(ctx, user: discord.User):
  if ctx.author.id != 897320965724315739:
    await ctx.repl6("only my owner can use this command")
    return
  if user.id not in dm_id:
    await ctx.reply("this user isnt in the conversation list")
    return
  dm_id.remove(user.id)
  dm_id.remove(user.name)
  await ctx.reply("succesfully stopped the convo")

phone_channel_name = []
phone_channel_id = []
other_channel_id = []
@bot.command()
async def startphone(ctx):
  if ctx.message.channel.id in phone_channel_id:
    await ctx.reply("You already started the phone...")
    return
  phone_channel_id.append(ctx.message.channel.id)
  phone_channel_name.append(ctx.message.channel.name)
  await ctx.reply("succesfully started the phone in this channel")



phone_convo = []
@bot.command()
async def call_phone(ctx, *, arg):
  if ctx.message.channel.id not in phone_channel_id:
    await ctx.reply("please use this command in the channel where you started the phone, the channels is: {}".format(" , ".join(phone_channel_name)))
    return

  if len(phone_channel_id) == 1:
   await ctx.send("Theres currently no other phone users...")
  elif len(phone_channel_id) > 1:
    phone_channel_id.remove(ctx.message.channel.id)
    phone_ch = await bot.fetch_channel(random.choice(phone_channel_id))
    phone_convo.append(random.choice(phone_channel_id) and ctx.message.channel.id)
    phone_channel_id.append(ctx.message.channel.id)
    
    await phone_ch.send(f"{ctx.author} | {arg}")
    await ctx.send("succesfully called phone please wait for the response")
   

ips = ["118.87.40.251",  "200.66.85.38",
"66.70.65.161",
"235.240.3.114",
"248.159.238.22",
"170.67.208.113",
"235.32.196.194",
"77.168.142.88",
"206.176.254.145",
"0.100.150.1",
"125.103.28.204",
"109.82.87.158",
"36.20.65.60",
"131.8.242.23",
"26.121.52.217",
"7.251.160.116",
"163.91.237.200",
"183.253.115.53",
"38.187.221.136",
"142.36.56.59",
"103.196.138.237"
]

flip = ["heads", "tails", "HEADS", "TAILS", "t a i l s", "h e a d s", "heds", "teyls"]

@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def ip(ctx):
  if ctx.author.id in blacklisted_user:
       await ctx.send("you're blacklisted from using my commands...")
       return
  await ctx.reply(f"{random.choice(ips)} is the random ip address you got :)")
  if random.choice(ips) == "103.196.138.237":
    await ctx.send(f"the ip you got is 103.196.138.237,congrats thats my real ip,you got that result from 1 in a 20 chances :)")



@bot.command()
async def toss(ctx):
  if ctx.author.id in blacklisted_user:
       await ctx.send("you're blacklisted from using my commands...")
       return
  await ctx.send(f'you flipped the coin and you got {random.choice(flip)}')

@bot.event
async def on_message(message):
  if "im gay" in message.content:
    await message.author.edit(nick="im gay uwu")
    await message.reply("yes you are")
  await bot.process_commands(message)

@bot.event
async def on_message(message):
 mentioned = message.raw_mentions
 if message.author == bot.user:
   return
 if any(id in afk_list for id in mentioned):
   await message.channel.send("the user you mentioned is afk reason: {}".format(', '.join(reason_list)))
   
 await bot.process_commands(message)
def gay():
  global gaysquad_list
  gaysquad_list = []
gay()
@bot.command()
async def gaysquad(ctx, *, reason=None):
 if ctx.author.id in blacklisted_user:
       await ctx.send("you're blacklisted from using my commands...")
       return
 if reason == None:
   await ctx.send("succesfully joined the gay squad you're now a member of the squad, reason:None")
   gaysquad_list.append(ctx.message.author.display_name)
 else:
   await ctx.send("succesfully joined gay squad reason: {}".format(reason))
   gaysquad_list.append(ctx.message.author.display_name)
 await ctx.send(f"the members of the gay squad are: {', '.join(gaysquad_list)}")

@bot.command()
async def gaysquadmembers(ctx):
  if ctx.author.id in blacklisted_user:
       await ctx.send("you're blacklisted from using my commands...")
       return
  await ctx.send(f"the members of the gay squad are: {', '.join(gaysquad_list)}")

@bot.command()
async def removegaysquad(ctx, *, arg=None):
 if ctx.author.id in blacklisted_user:
       await ctx.send("you're blacklisted from using my commands...")
       return
 if arg == None: 
  gaysquad_list.remove(ctx.message.author.display_name)
  await ctx.send(f"succesfully removed yourself from the gay squad :( the members are now: {', '.join(gaysquad_list)}")
 else:
   gaysquad_list.remove(arg)
   await ctx.send(f"succesfully removed {arg} from the gay squad,the members are now: {', '.join(gaysquad_list)}")

@bot.command()
async def gaysquadadd(ctx, *, arg):
  if ctx.author.id in blacklisted_user:
       await ctx.send("you're blacklisted from using my commands...")
       return
  gaysquad_list.append(arg)
  await ctx.send(f"success fully added {arg} to gay squad the members are now: {', '.join(gaysquad_list)}")

@bot.command()
async def afknames(ctx):
 if ctx.author.id in blacklisted_user:
       await ctx.send("you're blacklisted from using my commands...")
       return
 await ctx.send("The afk members are: {}".format(', '.join(afk_name)))

@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def randompass(ctx):
 if ctx.author.id in blacklisted_user:
       await ctx.send("you're blacklisted from using my commands...")
       return
 length = 10 
 characters = list(string.ascii_letters + string.digits + "@#$%&-+()/*:;!?")

 random.shuffle(characters)

 password = []
 for i in range(length):
  password.append(random.choice(characters))
 random.shuffle(password)
 await ctx.send("the password you got is: {}".format("".join(password)))

@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def reasonlist(ctx):
 if ctx.author.id in blacklisted_user:
       await ctx.send("you're blacklisted from using my commands...")
       return
 if len(reason_list) == 0:
  await ctx.send("reason list is empty")
 else:
  await ctx.send(", ".join(reason_list))


@bot.event
async def on_message(message):
  if message.author == bot.user:
    return
  if message.content in blacklisted_words:
    await message.reply("funfact: you just said a blacklisted word you're now blacklisted from using all of my command :)")
    await message.delete() 
    blacklisted_user.append(message.author.id)
    await message.channel.send("succesfully added to blacklist")
  await bot.process_commands(message)

@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def blacklistadd(ctx, member: discord.Member):
 if ctx.author.id in blacklisted_user:
       await ctx.send("you're blacklisted from using my commands...")
       return
 blacklisted_user.append(member.id)
 await ctx.send(f"succesfully added {member} to the blacklist")
@bot.command()
async def blacklist(ctx):
  if len(blacklisted_user) == 0:
    await ctx.send("theres no black listed users")
  else:
   await ctx.send(blacklisted_user)

@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def blacklistremove(ctx, member: discord.Member = None):
  if ctx.author.id in blacklisted_user:
   blacklisted_user.remove(ctx.author.id)
   await ctx.send(f"succesfully removed yourself from the blacklist")
  else:
   blacklisted_user.remove(member.id)
   await ctx.send(f"success fully removed {member} from the blacklist")


@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def everyone(ctx):
  await ctx.send("@everyone")

@bot.event
async def on_message(message):
  if message.author == bot.user:
    return
  if blacklisted_words in message.content:
    await message.reply("funfact: you just said a blacklisted word you're now blacklisted from using all of my command :)")
    await message.delete() 
    blacklisted_user.append(message.author.id)
    await message.channel.send("succesfully added to blacklist")
  await bot.process_commands(message)




@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def afk(ctx, *, reason=None):
  if ctx.author.id in blacklisted_user:
       await ctx.send("you're blacklisted from using my commands...")
       return
  if reason == None:
        await ctx.message.author.edit(nick=f"[AFK] {ctx.message.author.name}")
        await ctx.send(f"{ctx.author.mention} is now AFK, Reason: No reason specified.")
        afk_list.append(ctx.message.author.id)
        afk_name.append(ctx.message.author.name)
  else:
    await ctx.message.author.edit(nick=f"[AFK] {ctx.message.author.name}")
    await ctx.send(f"{ctx.author.mention} is now AFK, reason: {reason}")
    afk_list.append(ctx.message.author.id)
    afk_name.append(ctx.message.author.name)

@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def add(ctx, *nums):
  operation = ' + '.join(nums)
  await ctx.send(f"{operation} = {eval(operation)}")

@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def subtract(ctx, *nums):
 operation = " - ".join(nums)
 await ctx.send(f"{operation} = {eval(operation)}")

@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def multiply(ctx, *nums):
  operation = " * ".join(nums)
  await ctx.send(f"{operation} = {eval(operation)}")

@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def divide(ctx, *nums):
  operation = " / ".join(nums)
  await ctx.send(f"{operation} = {eval(operation)}")

@bot.event
async def on_message(message):
  if message.author == bot.user:
    return
  if "kms" in message.content:
    await message.delete()
    await message.channel.send("dont.")
  await bot.process_commands(message)

@bot.event
async def on_message(message):
 if message.author == bot.user:
   return
 chennel = bot.get_channel(978905532695982100)
 embed = discord.Embed(title="message author:", description=message.author)
 embed.add_field(name="message sent in:", value=message.channel.mention)
 embed.add_field(name="message content:", value=f"{message.content}, note: images cannot be logged")
 
 await chennel.send(embed=embed)
 await bot.process_commands(message)

@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def av(ctx, *, member: discord.Member=None):
 if member == None:
  member = ctx.author
  Avamember = member.avatar.url
  embed = discord.Embed(title=f"{member}s avatar")
  embed.set_image(url=Avamember)
  await ctx.send(embed=embed)
 else:
   Avamember = member.avatar.url
   embed = discord.Embed(title=f"{member}s avatar")
   embed.set_image(url=Avamember)
   await ctx.send(embed=embed)
     
@bot.event
async def on_message(message):
 if "[AFK]" in message.author.display_name: 
   await message.reply("bros chatted while afk,welcome back 😏😩")
   await message.author.edit(nick=message.author.name)
   afk_list.remove(message.author.id)
   afk_name.remove(message.author.name)
 await bot.process_commands(message)


@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def help2(ctx):
  embed = discord.Embed(title=f"my commands", description="the commands are in alphabetical order, also i still havent added all the commands in here")
  embed.add_field(name="a!help2", value="sends this message")
  embed.add_field(name="a!add", value="to use this command send !add (numbers you wanna add), note: dont add the symbol for addition")
  embed.add_field(name="a!addrole", value="adds the mentioned role to the mentioned user")
  embed.add_field(name="a!afk", value="makes you afk") 
  embed.add_field(name="a!afknames", value="sends the afk list")
  embed.add_field(name="a!anime", value="searchs the inputed anime")
  embed.add_field(name="a!announce", value="a!announce (title) (description) (footer)")
  embed.add_field(name="a!askme", value="asks the bot something like am i gay? the bot will randomly reply yes,no,etc.")
  embed.add_field(name="a!av", value="sends the mentioend user's avatar or sends the message author's avatar if no user is mentioned")
  embed.add_field(name="a!blacklist", value="sends the list of the blacklist")
  embed.add_field(name="a!blacklistadd", value="adds the mentioned user in the blacklist")
  embed.add_field(name="a!blacklistremove", value="removes the mentioned user in the blacklist")
  embed.add_field(name="a!change", value="changes the mentioned user's nickname into the inputted nickname")
  embed.add_field(name="a!deletus", value="purges the given amount of messages")
  await ctx.send(embed=embed)

count = 0
def counts():
  global count
  count += 100
def couns():
  global count
  count -= 100

@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def frvspam(ctx, *, arg=None):
  if arg is None:
    while True:
      await ctx.send("foreverspamming, type and send a!Break to stop the loop")
      if count == 100:
        break
  else:
    while True:
      await ctx.send(f"{arg}, type and send a!Break to stop the loop")
      if count == 100:
        break

@bot.command()
async def Break(ctx):
  counts()
  print(count)
  await ctx.reply("succesfully stopped the loop")
  couns()
  print(count)

@bot.event
async def on_message(message):
  if "https://" in message.content:
    await message.reply("bro sent a link 😡😡😡")
  await bot.process_commands(message)
  
@bot.command()
async def darkweb(ctx):
  await ctx.send("https://darkweb-sites.org/ please be aware of the risks on clicking this link,this site is legit and has all the links of the darkweb,i suggest using a vpn when clicking the link, the links inside the site only works when opened in tor and using the search engine duckduck.go,you cant open links from this site in any normal browser like google or chrome")




@bot.event
async def on_member_join(member):
 if member.guild.id == 966171824381632552:
  role = member.guild.get_role(970196606475436042)
  await member.add_roles(role)
  chn = member.guild.system_channel
  await chn.send(f"{member.mention} has joined we now have {member.guild.member_count} members, enjoy your stay, succesfully added gremlin role.")
 if member.guild.id == 969573605014917192:
  role = member.guild.get_role(973413641065992192)
  await member.add_roles(role)
  chn = member.guild.system_channel
  await chn.send(f"{member.mention} has joined we now have {member.guild.member_count} members, enjoy your stay, succesfully added member role.")

 elif member.id == 897320965724315739 and member.guild.id == 966171824381632552:
   ch = member.guild.system_channel
   await ch.send("Watcher has joined")
   role = member.guild.get_role(982558243819765770)
   await member.add_roles(role)
   msg = await ch.send(f"succesfully added {role.name}")
   await asyncio.sleep(5)
   await msg.delete()

@bot.event
async def on_member_remove(member):
  chn = member.guild.system_channel
  await chn.send(f"{member.name} has left us :( ,goodbye friend..")

@bot.command()
async def pokemonsearch(ctx, *, arg=None):
 if arg is None:
   await ctx.send("please put the pokemon you want to search..")
   return
 await ctx.send(f"https://www.pokemon.com/us/pokedex/{arg}/")

@bot.command()
async def pokemoncolor(ctx, *, arg=None):
 if arg is None:
   await ctx.reply("please put a pokemon color")
   return
 await ctx.send(f"https://pokemongo.gishan.net/color/{arg}")

@bot.command()
async def say(ctx, *, message=None):
  if message is None:
    await ctx.reply("bro forgor to say somethin")
    return
  await ctx.message.delete()
  await ctx.send(message)

@bot.event
async def on_message(msg):
  if msg.content == "Predator":
    await msg.reply("the leader of the giga chads ")
  await bot.process_commands(msg)




@bot.command()
async def createchannel(ctx, *, name):
 guild = ctx.message.guild
 await guild.create_text_channel(name)
 await ctx.reply(f"successfully made a channel called {name}")


swears = ["fuck", "idc", "stfu", "kys"]
chill = []
symbols = ["@", "#", "3", ":", ";", "&", "$", "%", ")", "(", "/", "1", "2", "4", "5", "6", "7", "8", "9", "10", "+", "-", "!", "?", ":3"]
@bot.event
async def on_message(message):
  if message.content in swears:
    await message.reply(f"please chill {message.author.display_name},😀 bro sweared")
  await bot.process_commands(message)   

@bot.command()
async def morsedecode(ctx, *, arg):
  for i in arg:
    if i == "a":
      await ctx.reply(f"{i} | .-")
    elif i == "b":
      await ctx.reply(f"{i} | -...")
    elif i == "c":
      await ctx.reply(f"{i} | -.-.")
    elif i == "d":
      await ctx.reply(f"{i} | -..")
    elif i == "e":
      await ctx.reply(f"{i} | .")
    elif i == "f":
      await ctx.reply(f"{i} | ..-.")
    elif i == "g":
      await ctx.reply(f"{i} | --.")
    elif i == "h":
      await ctx.reply(f"{i} | ....")
    elif i == "i":
      await ctx.reply(f"{i} | -")
    elif i == 'j':
      await ctx.reply(f"{i} | .---")
    elif i == 'k':
      await ctx.reply(f"{i} | -.-")
    elif i == 'l':
      await ctx.reply(f"{i} | .-..")
    elif i == 'm':
      await ctx.reply(f"{i} | --")
    elif i == 'n':
      await ctx.reply(f"{i} | -.")
    elif i == 'o':
      await ctx.reply(f"{i} | ---")
    elif i == 'p':
      await ctx.reply(f"{i} | .--.")
    elif i == 'q':
      await ctx.reply(f'{i} | --.-')
    elif i == 'r':
      await ctx.reply(f'{i} | .-.')
    elif i == 's':
      await ctx.reply(f'{i} | ...')
    elif i == 't':
      await ctx.reply(f'{i} | -')
    elif i == 'u':
      await ctx.reply(f'{i} |..-')
    elif i == 'v':
      await ctx.reply(f'{i} | ...-')
    elif i == 'w':
      await ctx.reply(f'{i} | .--')
    elif i == 'x':
      await ctx.reply(f'{i} | -..-')
    elif i == 'y':
      await ctx.reply(f'{i} | -.--')
    elif i == 'z':
      await ctx.reply(f'{i} | --..')

nuke = 0
@bot.command
async def nuke(ctx, channel: discord.TextChannel):
  if ctx.author.id != 897320965724315739:
    await ctx.reply("only my creator can use this")
    return
  nuke_channel = discord.utils.get(ctx.guild.channels, name=channel.name)

  if nuke_channel is not None:
        new_channel = await nuke_channel.clone(reason="Has been Nuked!")
        await nuke_channel.delete()
        await new_channel.send("THIS CHANNEL HAS BEEN NUKED!")
        await ctx.send("Nuked the Channel sucessfully!")

@bot.event
async def on_message(message):
  if "@everyone" in message.content:
    await message.reply("Bro... wtf...")
    await asyncio.sleep(10)
  await bot.process_commands(message)



@bot.command()
async def membercount(ctx):
 embed = discord.Embed(title=f"member count of {ctx.guild.name}: ", description=ctx.guild.member_count)
 await ctx.send(embed=embed)

@bot.command()
async def translate(ctx, lang, *, arg=None):
 if arg is None:
   await ctx.reply("please put an arg")
   return
 
 translator = Translator()
 trans = translator.translate(arg, dest=lang)
 await ctx.send(trans)


@bot.command()
async def reverse(ctx, *, message):
  reversed = message[::-1]
  await ctx.send(reversed)
@bot.command()
async def memes(ctx):
  embed = discord.Embed(title="", description="")

  async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/dankmemes/new.json?sort=hot') as r:
            res = await r.json()
            embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
            await ctx.send(embed=embed)






async def load_extensions():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            # cut off the .py from the file name
            await bot.load_extension(f"cogs.{filename[:-3]}")

keep_alive()
async def main():
    async with bot:
        await load_extensions()
        await bot.start(os.getenv('TOKEN'))
        
asyncio.run(main())
#pip install git+https://github.com/Rapptz/discord.py
#await  bot.process_commands(message)
