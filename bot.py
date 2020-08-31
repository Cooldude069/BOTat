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

client = commands.Bot(command_prefix="")
client.remove_command('help')
status = cycle(['Fortnite on Android', 'Fortnite on Iphone'])
global g
g = 0

@client.event
async def on_ready():
	change_status.start()
	print("Bot is ready.")
	async def runtime_background_task(role = discord.utils.get(server.roles, name="Moderator")):
   	while not client.is_closed:
		await client.edit_role(server="723435494578323476", role="RGB", colour=discord.Colour(0xff0000))
		await asyncio.sleep(5)
		await client.edit_role(server="723435494578323476", role="RGB", colour=discord.Colour(0xffff00))
	
@client.command(pass_context=True)
async def say(ctx, channel:discord.TextChannel , *, message):
	if ctx.message.author.guild_permissions.administrator:
		await channel.send(message)
		await ctx.send(f"{ctx.message.author.mention} sending message.....")

@client.command(aliases=['HELP', 'Help'])
async def help(ctx):
	await ctx.message.author.create_dm()
	await ctx.message.author.dm_channel.send("```i have no prefix \n addrole/removerole {user} {role name}-> adds or removes a role from the mentioned user \n mute/unmute {user}-> mutes/unmutes a user \n kick {user} {reason}-> kick a user from the server \n ban/unban {user} {reason}-> Bans/unbans a user from a server \n clear {number}-> deletes the number of messages \n dmsend {user} {message}-> send a dm message to the user \n ping-> show the bot's ping \n pop -> make a bubble wrap \n timer {amount} {unit}-> sets a timer, the units can be s, m or hr```")
	await ctx.send("Let me help you via DM")
	
@client.command(aliases=['hi' , 'Hi' , 'Hola' , 'Sup', 'sup', 'hola', 'Hello'])
async def hello(ctx):
	await ctx.send("Hi there!")
	
@client.command(pass_context=True)
async def addrole(ctx, member:discord.Member , *, role:discord.Role):
	if ctx.message.author.guild_permissions.manage_roles:
		await member.add_roles(role)
		await ctx.send(f"{role.name} has been added to {member.name} by {ctx.message.author.name}")
		
@client.command(pass_context=True)
async def removerole(ctx, member:discord.Member , *, role:discord.Role):
	if ctx.message.author.guild_permissions.manage_roles:
		await member.remove_roles(role)
		await ctx.send(f"{role.name} has been removed from {member.name} by {ctx.message.author.name}")
		
		
@client.command(pass_context=True)
async def mute(ctx, member:discord.Member):
	if ctx.message.author.guild_permissions.manage_roles:
		Mrole = discord.utils.get(member.guild.roles, name = "Muted")
		Grole = discord.utils.get(member.guild.roles, name = "Members")
		await member.remove_roles(Grole)
		await member.add_roles(Mrole)
		await ctx.send(f"{member.name} has been muted by {ctx.message.author.name}")
	
@client.command(pass_context=True)
async def unmute(ctx, member:discord.Member):
	if ctx.message.author.guild_permissions.manage_roles:
		Mrole = discord.utils.get(member.guild.roles, name = "Muted")
		Grole = discord.utils.get(member.guild.roles, name = "Members")
		await member.remove_roles(Mrole)
		await member.add_roles(Grole)
		await ctx.send(f"{member.name} has been unmuted by {ctx.message.author.name}")
		
@client.command(aliases=['AJO','Ajo'])
async def ajo(ctx):
	await ctx.send("BENJENE!!")

@client.command(aliases=["nice", "Noice", "Nice"])
async def noice(ctx):
	await ctx.send("IKR!!")

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(f'Hi {member.name}, welcome to The server!')

@client.command(aliases = ['Dmsend' , 'DMSEND'])
async def dmsend(ctx, member:discord.Member, *, note):
	if ctx.message.author.guild_permissions.manage_messages:
		await member.create_dm()
		await member.dm_channel.send(note)
		await ctx.send("DM sent successfully")
	else:
		ctx.send("You are not authorized to use this command")
	

@client.command(aliases=['Pop', 'POP'])
async def pop(ctx):
	await ctx.send("||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||\n||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||\n||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||\n||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||\n||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||\n||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||\n||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||\n||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||\n||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||\n||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||\n||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||\n||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||\n||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||\n||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||")
     
@client.command()
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
		ctx.send("You are not authorized to use this command")

@client.command()
async def ping(ctx):
	await ctx.send(f'Ping: {round(client.latency * 1000)} ms')

@client.command(aliases=['Oof', 'OOF'])
async def oof(ctx):
	await ctx.send("OOF!")

@client.command()
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
		time.sleep(tm - 3)
		await ctx.send("3")
		time.sleep(1)
		await ctx.send("2")
		time.sleep(1)
		await ctx.send("1")
		time.sleep(1)
		await ctx.send(":alarm_clock:Time Up:alarm_clock:")
	else:
		time.sleep(tm)
		await ctx.send(":alarm_clock:Time Up:alarm_clock:")
		return


@client.command(aliases=['Clear' , 'CLEAR'])
async def clear(ctx, amount=5):
	if ctx.message.author.guild_permissions.manage_messages:
		await ctx.channel.purge(limit=amount + 1)
		print(f'{amount} messages deleted')
		await ctx.send(f"`{amount}` messages deleted")
		time.sleep(2)
		await ctx.channel.purge(limit = 1)
	else:
		await ctx.send("You cannot use this command")

@client.command(aliases=['ssd', 'SSD', 'Ssd', 'Dilip', 'DILIP'])
async def dilip(ctx):
	await ctx.send("Fodo!!")

@client.command()
async def popgame(ctx, length=5):
	len = int(length)
	row = random.randint(0, len - 1)
	r = 0
	while r < len:
		if r == row:
			await ctx.send("||POP||")
		else:
			await ctx.send("||pop ||")
		r = r + 1

@client.command()
async def guess(ctx):
	global g
	g = 4	
	global no
	no = random.randint(0, 10)
	await ctx.send("```Guess The number game created. Enter your number using the command, gnumber (number). You get three chances[Note: The number should lie between 0 and 10]```")

@client.command()
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


@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):
	if ctx.message.author.guild_permissions.kick_members:
		await member.kick(reason=reason)
		await ctx.send(f'Kicked {member.mention}')
	else:
		ctx.send("You are not authorized to use this command")

@client.command()
async def ban(ctx, member : discord.Member, *, reason=None):
	if ctx.message.author.guild_permissions.ban_members:
		await member.ban(reason=reason)
		await ctx.send(f'Banned {member.mention}')
	else:
		ctx.send("You are not authorized to use this command")

@client.command(aliases=['F'])
async def f(ctx):
	await ctx.send(f'{ctx.message.author.name} has paid their respects')

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


client.run("NzQ1OTU1OTkwNzY3NDAzMDM5.Xz5Tpw.EjdNUpcusLZkCXdk8GUTSKfUqDQ")
