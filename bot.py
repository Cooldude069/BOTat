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
from tkinter import *
import math

client = commands.Bot(command_prefix=["jarvis ", "Jarvis ", ""])
client.remove_command('help')
status = cycle(['Fortnite on Android', 'Fortnite on Iphone','Wonderful Creation of Samarth','Pokemon','Valorant','PUBG','Clash Royale','Clash of Clans','Injustice'])
global g
g = 0

@client.event
async def on_ready():
	change_status.start()
	print("Bot is ready.")
	
@client.command(aliases=['calcy','Calcy'])
async def calculator(ctx):
	root = Tk()
	root.title("Simple Calculator")

	e = Entry(root, width=40, borderwidth=7)
	e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


	def button_click(number):
		#e.delete(0, END)
		current = e.get()
		e.delete(0, END)
		e.insert(0, str(current) + str(number))


	def button_clear():
		e.delete(0, END)


	def button_add():
		global fn
		global f_num
		first_add = e.get()
		f_num = int(first_add)
		e.delete(0, END)
		fn = 1

	def button_sub():
		global fn
		global f_num
		first_sub = e.get()
		f_num = int(first_sub)
		e.delete(0, END)
		fn = 2

	def button_multiply():
		global fn
		global f_num
		first_mult = e.get()
		f_num = int(first_mult)
		e.delete(0, END)
		fn = 3

	def button_divide(): 
		global fn
		global f_num
		first_div = e.get()
		f_num = int(first_div)
		e.delete(0, END)
		fn = 4

	def button_sqrt():
		global fn
		global f_num
		first_sqrt = e.get()
		f_num = int(first_sqrt)
		e.delete(0, END)
		e.insert(0, pow(f_num,1.0/2))
	def button_cbrt():
		global fn
		global f_num
		first_cbrt = e.get()
		f_num = int(first_cbrt)
		e.delete(0, END)
		e.insert(0, pow(f_num,1.0/3))

	def button_tan():
		global fn
		global f_num
		first_tan = e.get()
		f_num = int(first_tan)
		e.delete(0, END)
		angle = math.pi * f_num / 180
		e.insert(0, math.tan(angle))

	def button_sine():
		global fn
		global f_num
		first_sine = e.get()
		f_num = int(first_sine)
		e.delete(0, END)
		angle = math.pi * f_num / 180
		e.insert(0, math.sin(angle))

	def button_cos():
		global fn
		global f_num
		first_cos = e.get()
		f_num = int(first_cos)
		e.delete(0, END)
		angle = math.pi * f_num / 180
		e.insert(0, math.cos(angle))

	def button_log():
		global fn
		global f_num
		first_log = e.get()
		f_num = int(first_log)
		e.delete(0, END)
		e.insert(0, math.log(f_num))


	def button_equal():
		if(fn == 1):
			second_number = e.get()
			e.delete(0, END)
			e.insert(0, f_num + int(second_number))
		elif(fn == 4):
			second_number = e.get()
			e.delete(0, END)
			e.insert(0, f_num / int(second_number))
		elif(fn == 3):
			second_number = e.get()
			e.delete(0, END)
			e.insert(0, f_num * int(second_number))
		else:
			second_number = e.get()
			e.delete(0, END)
			e.insert(0, f_num - int(second_number))



		#define buttons

	button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1), bg="white", fg="black")
	button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2), bg="white", fg="black")
	button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3), bg="white", fg="black")
	button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4), bg="white", fg="black")
	button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5), bg="white", fg="black")
	button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6), bg="white", fg="black")
	button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7), bg="white", fg="black")
	button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8), bg="white", fg="black")
	button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9), bg="white", fg="black")
	button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0), bg="white", fg="black")
	button_add = Button(root, text="+", padx=39, pady=20, command=button_add, bg="white", fg="red")
	button_equal = Button(root, text="=", padx=87, pady=20, command=button_equal, bg="white", fg="red")
	button_clear = Button(root, text="Clear", padx=77, pady=20, command=button_clear, bg="white", fg="red")
	button_sub = Button(root, text="-", padx=40, pady=20, command=button_sub, bg="white", fg="red")
	button_multiply = Button(root, text="x", padx=40, pady=20, command=button_multiply, bg="white", fg="red")
	button_divide = Button(root, text="/", padx=40, pady=20, command=button_divide, bg="white", fg="red")
	button_sqrt = Button(root, text="√x", padx=35, pady=20, command=button_sqrt, bg="white", fg="red")
	button_cbrt = Button(root, text="∛x", padx=35, pady=20, command=button_cbrt, bg="white", fg="red")
	button_tan = Button(root, text="tan", padx=35, pady=20, command=button_tan, bg="white", fg="red")
	button_sine = Button(root, text="sine", padx=35, pady=20, command=button_sine, bg="white", fg="red")
	button_cos = Button(root, text="cos", padx=35, pady=20, command=button_cos, bg="white", fg="red")
	button_log = Button(root, text="ln", padx=35, pady=20, command=button_log, bg="white", fg="red")

	#put buttons on screen
	button_1.grid(row=5, column=0)
	button_2.grid(row=5, column=1)
	button_3.grid(row=5, column=2)

	button_4.grid(row=4, column=0)
	button_5.grid(row=4, column=1)
	button_6.grid(row=4, column=2)

	button_7.grid(row=3, column=0)
	button_8.grid(row=3, column=1)
	button_9.grid(row=3, column=2)

	button_0.grid(row=6, column=0)
	button_add.grid(row=7,column=0)
	button_clear.grid(row=6,column=1, columnspan=2)
	button_equal.grid(row=7,column=1, columnspan=2)
	button_sub.grid(row=8,column=0)
	button_divide.grid(row=8, column=1)
	button_multiply.grid(row=8, column=2)

	button_sqrt.grid(row=2, column=0)
	button_cbrt.grid(row=2, column=1)
	button_tan.grid(row=2, column=2)

	button_sine.grid(row=1, column=0)
	button_cos.grid(row=1, column=1)
	button_log.grid(row=1, column=2)

	root.mainloop()
	
@client.command(aliases=['giverep', 'Giverep', 'GIVEREP', 'Thanks', 'thanks', 'THANKS', 'thank', 'Thank', 'THANK', 'Ty', 'TY'])
async def ty(ctx , member:discord.Member):
	await open_account(member)

	users = await get_bank_data()
	user = member

	users[str(user.id)]["wallet"] += 1

	with open("thank.json", "w") as f:
		json.dump(users,f)
		
	await ctx.send(f"Added +1 rep to {member.display_name}")

@client.command(aliases=['Rep', 'REP', 'Reputation', 'reputation', 'REPUTATION'])
async def rep(ctx, member:discord.Member):
	await open_account(member)
	user = member
	users = await get_bank_data()

	wallet_amt = users[str(user.id)]["wallet"]

	em = discord.Embed(title = f"{user.display_name}'s reputation ",color = discord.Color.red())
	em.add_field(name = "Helps", value = wallet_amt)
	await ctx.send(embed = em)



async def open_account(user):

	users = await get_bank_data()

	with open("thank.json", "r") as f:
		users = json.load(f)

	if str(user.id) in users:
		return False
	else:
		users[str(user.id)] = {}
		users[str(user.id)]["wallet"] = 0

	with open("thank.json", "w") as f:
		json.dump(users,f)
	return True

async def get_bank_data():
	with open("thank.json", "r") as f:
		users = json.load(f)

	return users
	
@client.command(pass_context=True, aliases=['Say', 'SAY'])
async def say(ctx, channel:discord.TextChannel , *, message):
	if ctx.message.author.guild_permissions.administrator:
		await channel.send(message)
		await ctx.send(f"{ctx.message.author.mention} sending message.....")
		
@client.command(aliases=['Reboot', 'REBOOT', 'restart', 'Restart', 'RESTART'])
async def reboot(ctx):
	if ctx.message.author.guild_permissions.manage_roles:
		print(f'{ctx.message.author.display_name} initialised reboot')
		await ctx.send(f'{ctx.message.author.display_name} initialised reboot')
		await ctx.send("Test complete. Preparing to power down and begin diagnostics...")
		time.sleep(1)
		await ctx.send("Verifying command")
		time.sleep(1)
		await ctx.send("Clearing all data...")
		await ctx.send("shutting down...")
		await ctx.send("Turning on..")
		time.sleep(1)
		await ctx.send("Reboot finished...")
		await ctx.send("Good to see you again sir!")
	else:
		await ctx.send("You are not authorized to use this command")

@client.command(aliases=['HELP', 'Help'])
async def help(ctx):
	await ctx.message.author.create_dm()
	await ctx.message.author.dm_channel.send("```My prefix is jarvis eg. jarvis clear \n addrole/removerole {user} {role name}-> adds or removes a role from the mentioned user \n mute/unmute {user}-> mutes/unmutes a user \n kick {user} {reason}-> kick a user from the server \n ban/unban {user} {reason}-> Bans/unbans a user from a server \n clear {number}-> deletes the number of messages \n dmsend {user} {message}-> send a dm message to the user \n ping-> show the bot's ping \n pop -> make a bubble wrap \n timer {amount} {unit}-> sets a timer, the units can be s, m or hr```")
	await ctx.send("Let me help you via DM")
	
@client.command(aliases=['hi' , 'Hi' , 'Hola' , 'Sup', 'sup', 'hola', 'Hello'])
async def hello(ctx):
	await ctx.send("Hello Sir!")
	
@client.command(pass_context=True, aliases=['Addrole', 'ADDROLE'])
async def addrole(ctx, member:discord.Member , *, role:discord.Role):
	if ctx.message.author.guild_permissions.manage_roles:
		await member.add_roles(role)
		await ctx.send(f"{role.name} has been added to {member.display_name} by {ctx.message.author.display_name}")
	else:
		await ctx.send("You are not authorized to use this command")
		
@client.command(pass_context=True, aliases=['Removerole', 'REMOVEROLE'])
async def removerole(ctx, member:discord.Member , *, role:discord.Role):
	if ctx.message.author.guild_permissions.manage_roles:
		await member.remove_roles(role)
		await ctx.send(f"{role.name} has been removed from {member.display_name} by {ctx.message.author.display_name}")
	else:
		await ctx.send("You are not authorized to use this command")
		
		
@client.command(pass_context=True, aliases=['Mute', 'MUTE'])
async def mute(ctx, member:discord.Member):
	if ctx.message.author.guild_permissions.manage_roles:
		Mrole = discord.utils.get(member.guild.roles, name = "Muted")
		Grole = discord.utils.get(member.guild.roles, name = "Members")
		await member.remove_roles(Grole)
		await member.add_roles(Mrole)
		await ctx.send(f"{member.display_name} has been muted by {ctx.message.author.display_name}")
	else:
		await ctx.send("You are not authorized to use this command")
	
@client.command(pass_context=True, aliases=['Unmute', 'UNMUTE'])
async def unmute(ctx, member:discord.Member):
	if ctx.message.author.guild_permissions.manage_roles:
		Mrole = discord.utils.get(member.guild.roles, name = "Muted")
		Grole = discord.utils.get(member.guild.roles, name = "Members")
		await member.remove_roles(Mrole)
		await member.add_roles(Grole)
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
		print(f'{amount} messages deleted by {ctx.message.author.display_name}')
		await ctx.send(f"`{amount}` messages deleted")
		time.sleep(2)
		await ctx.channel.purge(limit = 1)
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
	else:
		await ctx.send("You are not authorized to use this command")

@client.command(aliases=['Ban', 'BAN'])
async def ban(ctx, member : discord.Member, *, reason=None):
	if ctx.message.author.guild_permissions.ban_members:
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


client.run("NzQ1OTU1OTkwNzY3NDAzMDM5.Xz5Tpw.EjdNUpcusLZkCXdk8GUTSKfUqDQ")
