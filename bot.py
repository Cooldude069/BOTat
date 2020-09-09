import discord
from discord.ext import commands, tasks
import random
from itertools import cycle
import time
import json
import os
import shutil
import asyncio
from discord.utils import get
import datetime


client = commands.Bot(command_prefix=["jarvis ", "Jarvis ", ""])
client.remove_command('help')
status = cycle(['Fortnite on Android', 'Fortnite on Iphone','Wonderful Creation of Samarth','Pokemon','Valorant','PUBG','Clash Royale','Clash of Clans','Injustice' , 'SKRIBBL'])
global g
global k
k = 0
g = 0

@client.event
async def on_ready():
	change_status.start()
	print("Bot is ready.")
	
	
@client.command(aliases = ['Lockdown' , 'lockdown' , 'LOCKDOWN' , 'Lock' , 'LOCK'])
async def lock(ctx , timer = 0):
	if ctx.message.author.guild_permissions.manage_channels:
		await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False)
		if timer == 0:
			await ctx.send(f"Locked {ctx.message.channel.mention} indefinitely")
		else:
			await ctx.send(f"Locked {ctx.message.channel.mention} for `{timer}`s")
			await asyncio.sleep(timer - 3)
			await ctx.channel.set_permissions(ctx.guild.default_role , send_messages = True)
			await ctx.send(f"Unlocked {ctx.message.channel.mention}")
			
@client.command(aliases = ['UNLOCK' , 'Unlock'])
async def unlock(ctx):
	if ctx.message.author.guild_permissions.manage_channels:
		await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True)
		await ctx.send(f"Unlocked {ctx.message.channel.mention}")
	
@client.command(pass_context = True , aliases = ['POLL' , 'Poll'])
async def poll(ctx, question , *options : str):
	if ctx.message.author.top_role == 'Moderator' :
		pol = discord.Embed(title = f'**POLL**{question}' , color = discord.Color.blue())
		pol.add_field(name = f"1️⃣  {options[0]}" , value = f"2️⃣  {options[1]}" , inline = False)
		poll_1 = '1️⃣'
		poll_2 = '2️⃣'
		channel = discord.utils.get(ctx.message.author.guild.channels , name = 'l🗽l-polls')
		msg = await channel.send(embed = pol)
		await msg.add_reaction(poll_1)
		await msg.add_reaction(poll_2)
		await ctx.send(f"Your poll has successfully posted in {channel}")
	elif ctx.message.author.id == 727539383405772901:
		pol = discord.Embed(title = f'**POLL**{question}' , color = discord.Color.blue())
		pol.add_field(name = f"1️⃣  {options[0]}" , value = f"2️⃣  {options[1]}" , inline = False)
		poll_1 = '1️⃣'
		poll_2 = '2️⃣'
		channel = discord.utils.get(ctx.message.author.guild.channels , name = 'l🗽l-polls')
		msg = await channel.send(embed = pol)
		await msg.add_reaction(poll_1)
		await msg.add_reaction(poll_2)
		await ctx.send(f"Your poll has successfully posted in {channel}")
	else:
		await ctx.send("You are not authorized to use this command")
	
@client.command(aliases = ['MEME', 'Meme'])
async def meme(ctx):
	emoji_1 = '🤣'
	emoji_2 = '👍'
	emoji_3 = '👎'
	await ctx.message.add_reaction(emoji_1)
	await ctx.message.add_reaction(emoji_2)
	await ctx.message.add_reaction(emoji_3)
	
@client.command(aliases= ['Offence' , 'Complain', 'complain', 'COMPLAIN', 'OFFENCE'])
async def offence(ctx, * ,complain):
	Channel = discord.utils.get(ctx.message.author.guild.channels, name = "l🔔l-staff-notes")
	offe  = discord.Embed(title = f"{complain}" , color = discord.Color.red())
	offe.add_field(name = f"by {ctx.message.author.display_name}", value = f"Role : {ctx.message.author.top_role}" ,inline = False)
	await Channel.send(embed = offe)
	await ctx.send("Your complain has successfully been posted, Thank you")
	
@client.command(aliases= ['Suggestion', 'SUGGESTION'])
async def suggestion(ctx, * ,suggestion):
	Channel = discord.utils.get(ctx.message.author.guild.channels, name = "l🔔l-staff-notes")
	sugg  = discord.Embed(title = f"{suggestion}" , color = discord.Color.blue())
	sugg.add_field(name = f"by {ctx.message.author.display_name}", value = f"Role : {ctx.message.author.top_role}" ,inline = False)
	await Channel.send(embed = sugg)
	await ctx.send("Your suggestion has successfully been posted, Thank you")
	
@client.command(aliases=['Handjob', "HANDJOB"])
async def handjob(ctx):
	if ctx.message.author.guild_permissions.administrator:
		await ctx.send("8==:fist:==D:sweat_drops:")
	else:
		await ctx.send("Sir!, I cannot let you do that(Masturbation makes vision blurry)")
	
@client.command(pass_context=True, aliases=['Say', 'SAY'])
async def say(ctx, channel:discord.TextChannel , *, message):
	if ctx.message.author.guild_permissions.administrator:
		await channel.send(message)
		await ctx.send(f"{ctx.message.author.mention} sending message.....")
	elif ctx.message.author.id == 727539383405772901:
		await channel.send(message)
		await ctx.send(f"{ctx.message.author.mention} sending message.....")
	elif ctx.message.author.id == 707681278178230282:
		await channel.send(message)
		await ctx.send(f"{ctx.message.author.mention} sending message.....")
		
@client.command(aliases=['Reboot', 'REBOOT', 'restart', 'Restart', 'RESTART'])
async def reboot(ctx):
	if ctx.message.author.guild_permissions.manage_roles:
		print(f'{ctx.message.author.display_name} initialised reboot')
		await ctx.send(f'{ctx.message.author.display_name} initialised reboot')
		await ctx.send("Test complete. Preparing to power down and begin diagnostics...")
		await asyncio.sleep(1)
		await ctx.send("Verifying command")
		await asyncio.sleep(1)
		await ctx.send("Clearing all data...")
		await ctx.send("shutting down...")
		await ctx.send("Turning on..")
		await asyncio.sleep(1)
		await ctx.send("Reboot finished...")
		await ctx.send("Good to see you again sir!")
	else:
		await ctx.send("You are not authorized to use this command")

@client.command(aliases=['HELP', 'Help'])
async def help(ctx):
	await ctx.message.author.create_dm()
	await ctx.message.author.dm_channel.send("``` My prefix is jarvis eg. jarvis clear \n addrole/removerole {user} {role name}-> adds or removes a role from the mentioned user \n mute/unmute {user}-> mutes/unmutes a user \n kick {user} {reason}-> kick a user from the server \n ban/unban {user} {reason}-> Bans/unbans a user from a server \n clear {number}-> deletes the number of messages \n dmsend {user} {message}-> send a dm message to the user \n ping-> show the bot's ping \n pop -> make a bubble wrap \n timer {amount} {unit}-> sets a timer, the units can be s, m or hr\n complain {message}-> makes a complain and reports it to the officials\n suggestion {message}-> makes a suggestion and reports it to the officials\n poll {question} {options}-> makes a poll and posts it in the polls channel```")
	await ctx.send("Let me help you via DM")
	
@client.command(aliases=['hi' , 'Hi' , 'Hola' , 'Sup', 'sup', 'hola', 'Hello'])
async def hello(ctx):
	await ctx.send("Hello Sir!")
	
@client.command(pass_context=True, aliases=['Addrole', 'ADDROLE'])
async def addrole(ctx, member:discord.Member , *, role:discord.Role):
	if ctx.message.author.guild_permissions.administrator:
		await member.add_roles(role)
		await ctx.send(f"{role.name} has been added to {member.display_name} by {ctx.message.author.display_name}")
	elif ctx.message.author.id == 727539383405772901:
		await member.add_roles(role)
		await ctx.send(f"{role.name} has been added to {member.display_name} by {ctx.message.author.display_name}")
	else:
		await ctx.send("You are not authorized to use this command")
		
@client.command(pass_context=True, aliases=['Removerole', 'REMOVEROLE'])
async def removerole(ctx, member:discord.Member , *, role:discord.Role):
	if ctx.message.author.guild_permissions.administrator:
		await member.remove_roles(role)
		await ctx.send(f"{role.name} has been removed from {member.display_name} by {ctx.message.author.display_name}")
	elif ctx.message.author.id == 727539383405772901:
		await member.remove_roles(role)
		await ctx.send(f"{role.name} has been removed from {member.display_name} by {ctx.message.author.display_name}")
	else:
		await ctx.send("You are not authorized to use this command")
		
		
@client.command(pass_context=True, aliases=['Mute', 'MUTE'])
async def mute(ctx, member:discord.Member):
	if ctx.message.author.guild_permissions.manage_roles:
		if ctx.message.author.guild.id == 723435494578323476:
			Mrole = discord.utils.get(member.guild.roles, name = "Muted")
			Grole = discord.utils.get(member.guild.roles, name = "Members")
			await member.remove_roles(Grole)
			await member.add_roles(Mrole)
			await ctx.send(f"{member.display_name} has been muted by {ctx.message.author.display_name}")
		else:
			Mrole = discord.utils.get(member.guild.roles, name = "Muted")
			await member.add_roles(Mrole)
			await ctx.send(f"{member.display_name} has been muted by {ctx.message.author.display_name}")
	elif ctx.message.author.id == 727539383405772901:
		if ctx.message.author.guild.id == 723435494578323476:
			Mrole = discord.utils.get(member.guild.roles, name = "Muted")
			Grole = discord.utils.get(member.guild.roles, name = "Members")
			await member.remove_roles(Grole)
			await member.add_roles(Mrole)
			await ctx.send(f"{member.display_name} has been muted by {ctx.message.author.display_name}")
		else:
			Mrole = discord.utils.get(member.guild.roles, name = "Muted")
			await member.add_roles(Mrole)
			await ctx.send(f"{member.display_name} has been muted by {ctx.message.author.display_name}")
	else:
		await ctx.send("You are not authorized to use this command")
	
@client.command(pass_context=True, aliases=['Unmute', 'UNMUTE'])
async def unmute(ctx, member:discord.Member):
	if ctx.message.author.guild_permissions.manage_roles:
		if ctx.message.author.guild.id == 723435494578323476:
			Mrole = discord.utils.get(member.guild.roles, name = "Muted")
			Grole = discord.utils.get(member.guild.roles, name = "Members")
			await member.remove_roles(Mrole)
			await member.add_roles(Grole)
			await ctx.send(f"{member.display_name} has been unmuted by {ctx.message.author.display_name}")
		else:
			Mrole = discord.utils.get(member.guild.roles, name = "Muted")
			await member.remove_roles(Mrole)
			await ctx.send(f"{member.display_name} has been unmuted by {ctx.message.author.display_name}")
	elif ctx.message.author.id == 727539383405772901:
		if ctx.message.author.guild.id == 723435494578323476:
			Mrole = discord.utils.get(member.guild.roles, name = "Muted")
			Grole = discord.utils.get(member.guild.roles, name = "Members")
			await member.remove_roles(Mrole)
			await member.add_roles(Grole)
			await ctx.send(f"{member.display_name} has been unmuted by {ctx.message.author.display_name}")
		else:
			Mrole = discord.utils.get(member.guild.roles, name = "Muted")
			await member.remove_roles(Mrole)
			await ctx.send(f"{member.display_name} has been unmuted by {ctx.message.author.display_name}")
	else:
		await ctx.send("You are not authorized to use this command")
		
@client.command(aliases=['AJO','Ajo'])
async def ajo(ctx):
	await ctx.send("BENJENE!!")

@client.command(aliases=["nice", "Noice", "Nice"])
async def noice(ctx):
	await ctx.send("IKR!!")

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(f'Hi {member.display_name}, welcome to The server!')

@client.command(aliases = ['Dmsend' , 'DMSEND'])
async def dmsend(ctx, member:discord.Member, *, note):
	if ctx.message.author.guild_permissions.manage_messages:
		await member.create_dm()
		await member.dm_channel.send(note)
		await ctx.send("DM sent successfully")
	else:
		await ctx.send("You are not authorized to use this command")
	

@client.command(aliases=['Pop', 'POP'])
async def pop(ctx):
	await ctx.send("||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||\n||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||\n||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||\n||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||\n||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||\n||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||\n||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||\n||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||\n||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||\n||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||\n||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||\n||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||\n||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||\n||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||")
     
@client.command(aliases=['Unban', 'UNBAN'])
async def unban(ctx, *, member):
	if ctx.message.author.guild_permissions.ban_members:
		banned_users = await ctx.guild.bans()
		member_name, member_discriminator = member.split('#')

		for ban_entry in banned_users:
			user = ban_entry.user

			if (user.name, user.discriminator) == (member_name, member_discriminator):
				await ctx.guild.unban(user)
				await ctx.send(f'Unbanned {user.mention}')
				return
	else:
		await ctx.send("You are not authorized to use this command")

@client.command()
async def ping(ctx):
	await ctx.send(f'Ping: {round(client.latency * 1000)} ms')

@client.command(aliases=['Oof', 'OOF'])
async def oof(ctx):
	await ctx.send("OOF!")

@client.command(aliases=['Timer', 'TIMER'])
async def timer(ctx, *, Tm):
	if Tm.endswith('r'):
		tmr, un = Tm.split('h')
		tm = float(tmr) * 3600
		await ctx.send(f"Timer set for `{tmr}` hours")
	elif Tm.endswith('s'):
		tmr, un = Tm.split('s')
		tm = float(tmr)
		await ctx.send(f"Timer set for `{tmr}` seconds")
	elif Tm.endswith('m'):
		tmr, un = Tm.split('m')
		await ctx.send(f"Timer set for `{tmr}` minutes")
		tm = float(tmr) * 60
	if tm > 3.0:
		await asyncio.sleep(tm - 3)
		await ctx.send("3")
		await asyncio.sleep(1)
		await ctx.send("2")
		await asyncio.sleep(1)
		await ctx.send("1")
		await asyncio.sleep(1)
		await ctx.send(":alarm_clock:Time Up:alarm_clock:")
	else:
		await asyncio.sleep(tm)
		await ctx.send(":alarm_clock:Time Up:alarm_clock:")
		return


@client.command(aliases=['Clear' , 'CLEAR' , 'purge' , 'Purge' , 'PURGE'])
async def clear(ctx, amount=5):
	if ctx.message.author.guild_permissions.manage_messages:
		await ctx.channel.purge(limit=amount + 1)
		print(f'{amount} messages deleted by {ctx.message.author.display_name}')
		clm = await ctx.send(f"`{amount}` messages deleted")
		await clm.delete(delay = 2)
	elif ctx.message.author.id == 727539383405772901:
		await ctx.channel.purge(limit=amount + 1)
		print(f'{amount} messages deleted by {ctx.message.author.display_name}')
		clm = await ctx.send(f"`{amount}` messages deleted")
		await clm.delete(delay = 2)
	else:
		await ctx.send("You are not authorized to use this command")


@client.command(aliases=['Guess', 'GUESS'])
async def guess(ctx):
	global g
	g = 4	
	global no
	no = random.randint(0, 10)
	await ctx.send("```Guess The number game created. Enter your number using the command, gnumber (number). You get three chances[Note: The number should lie between 0 and 10]```")

@client.command(aliases=['Gnumber', 'GNUMBER'])
async def gnumber(ctx, gnum):
	global g
	if g > 2:
		if int(gnum) == no:
			await ctx.send(":partying_face: Congratulations!, You won :partying_face:")
			g = 1
		else:
			await ctx.send(f"Better Luck next time.")
			g = g - 1
	elif g == 2:
		if int(gnum) != no:
			await ctx.send(f'Better luck next time. The number was {no}')
			g = g - 1
		else:
			await ctx.send(":partying_face: Congratulations!, You won :partying_face:")
			g = 1
	elif g == 1:
		await ctx.send("```You have used all of your chances```")
		g = 0
	else:
		await ctx.send("```Guess the number game not created```")


@client.command(aliases=['Kick', 'KICK'])
async def kick(ctx, member : discord.Member, *, reason=None):
	if ctx.message.author.guild_permissions.kick_members:
		await member.kick(reason=reason)
		await ctx.send(f'Kicked {member.mention}')
	elif ctx.message.author.id == 727539383405772901:
		await member.kick(reason=reason)
		await ctx.send(f'Kicked {member.mention}')
	else:
		await ctx.send("You are not authorized to use this command")

@client.command(aliases=['Ban', 'BAN'])
async def ban(ctx, member : discord.Member, *, reason=None):
	if ctx.message.author.guild_permissions.ban_members:
		await member.ban(reason=reason)
		await ctx.send(f'Banned {member.mention}')
	elif ctx.message.author.id == 727539383405772901:
		await member.ban(reason=reason)
		await ctx.send(f'Banned {member.mention}')
	else:
		await ctx.send("You are not authorized to use this command")

@client.command(aliases=['F'])
async def f(ctx):
	await ctx.send(f'{ctx.message.author.display_name} has paid their respects')

@tasks.loop(minutes=15)
async def change_status():
	await client.change_presence(activity=discord.Game(next(status)))


@client.command(aliases=['8ball', 'Qna'])
async def qna(ctx, *, question):
	responses = ["It is certain.",
                 "As I see it, yes.",
                 "Reply hazy, try again.",
                 "Don't count on it.",
                 "It is decidedly so.",
                 "Most likely.",
                 "Ask again later.",
                 "My reply is no.",
                 "Without a doubt.",
                 "Outlook good.",
                 "Better not tell you now.",
                 "My sources say no.",
                 "Yes – definitely.",
                 "Yes.",
                 "Cannot predict now.",
                 "Outlook not so good.",
                 "You may rely on it.",
                 "Signs point to yes.",
                 "Concentrate and ask again.",
                 "Very doubtful.",
                 "Na na tahse nhu te"]
	await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')


@client.command(aliases=['Binod', 'BINOD'])
async def binod(ctx):
	await ctx.send("BINOD!!")
	
@client.command(aliases = ['Rainbow' , 'RAINBOW'])
async def rainbow(ctx , member:discord.Member, times = 1):
	if ctx.message.author.guild_permissions.administrator:
		i = 0
		k = 0
		while i < times:
			red = discord.utils.get(member.guild.roles, name = "Red")
			blue = discord.utils.get(member.guild.roles, name = "Blue")
			green = discord.utils.get(member.guild.roles, name = "Green")
			yellow = discord.utils.get(member.guild.roles, name = "Yellow")
			purple = discord.utils.get(member.guild.roles, name = "Purple")
			await asyncio.sleep(5)
			await member.add_roles(red)
			await asyncio.sleep(5)
			await member.add_roles(blue)
			await member.remove_roles(red)
			await asyncio.sleep(5)
			await member.add_roles(green)
			await member.remove_roles(blue)
			await asyncio.sleep(5)
			await member.add_roles(yellow)
			await member.remove_roles(green)
			await asyncio.sleep(5)
			await member.add_roles(purple)
			await member.remove_roles(yellow)
			await asyncio.sleep(5)
			await member.remove_roles(purple)
			i += 1
					
@client.command(aliases=['rainstop'])
async def colorstop(ctx):
	k = 1
	
@client.command(aliases = ['Slowmode' , 'SLOWMODE'])
async def slowmode(ctx, st = 5):
	if ctx.message.author.guild_permissions.manage_channels:
		await ctx.message.channel.edit(slowmode_delay = st)
		await ctx.send(f"Slowmode set for`{st}` seconds")
		
@client.command(aliases = ['Slowend' , 'SLOWEND'])
async def slowend(ctx):
	if ctx.message.author.guild_permissions.manage_channels:
		await ctx.message.channel.edit(slowmode_delay = 0)
		await ctx.send("Slowmode removed")

	
@client.event
async def on_message(message):
	if len(message.content) == 0:
		if message.channel.name == '🤣meme-competiton':
			meme_1 = '🤣'
			meme_2 = '👍'
			meme_3 = '👎'
			await message.add_reaction(meme_1)
			await message.add_reaction(meme_2)
			await message.add_reaction(meme_3)
				
	await client.process_commands(message)


client.run("NzQ1OTU1OTkwNzY3NDAzMDM5.Xz5Tpw.EjdNUpcusLZkCXdk8GUTSKfUqDQ")
