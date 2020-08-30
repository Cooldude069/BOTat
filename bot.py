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
status = cycle(['Fortnite on Android', 'Fortnite on Iphone'])
global g
g = 0

@client.event
async def on_ready():
	change_status.start()
	print("Bot is ready.")

@client.command(aliases=['hi' , 'Hi' , 'Hola' , 'Sup', 'sup', 'hola', 'Hello'])
async def hello(ctx):
	await ctx.send("Hi there!")

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

@client.command()
async def dmsend(member:discord.Member, *, note):
	await member.create_dm()
	await member.dm_channel.send(note)
	await ctx.send("DM sent successfully")

@client.command(aliases=['Pop', 'POP'])
async def pop(ctx):
	await ctx.send("||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||\n||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||\n||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||\n||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||\n||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||\n||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||\n||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||\n||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||\n||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||\n||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||\n||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||\n||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||\n||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||\n||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||")
     
@client.command()
async def unban(ctx, *, member):
	banned_users = await ctx.guild.bans()
	member_name, member_discriminator = member.split('#')

	for ban_entry in banned_users:
		user = ban_entry.user

		if (user.name, user.discriminator) == (member_name, member_discriminator):
			await ctx.guild.unban(user)
			await ctx.send(f'Unbanned {user.mention}')
			return

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


@client.command(aliases=['clean'])
async def clear(ctx, amount=5):
	await ctx.channel.purge(limit=amount + 1)
	print(f'{amount} messages deleted')
	await ctx.send(f"`{amount}` messages deleted")
	time.sleep(3)
	await ctx.channel.purge(limit = 1)

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
	await member.kick(reason=reason)
	await ctx.send(f'Kicked {member.mention}')

@client.command()
async def ban(ctx, member : discord.Member, *, reason=None):
	await member.ban(reason=reason)
	await ctx.send(f'Banned {member.mention}')

@client.command(aliases=['F'])
async def f(ctx):
	await ctx.send(f'You have paid your respects')

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
