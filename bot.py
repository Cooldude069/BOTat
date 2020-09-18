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
from discord import Spotify

client = commands.Bot(command_prefix=["jarvis ", "Jarvis ", ""])
client.remove_command('help')
status = cycle(['Fortnite on Android', 'Fortnite on Iphone','Wonderful Creation of Samarth','Pokemon','Valorant','PUBG','Clash Royale','Clash of Clans','Injustice' , 'SKRIBBL'])
global g
global k
global i
k = 0
g = 0
global gv
gv = 0
global parts
parts = []


@client.event
async def on_ready():
	change_status.start()
	print("Bot is ready.")
	
@client.command(aliases = ["Slap" , "SLAP"])
async def slap(ctx , user:discord.Member):
	links = ["https://media1.tenor.com/images/814c84a90cc8b6a9826001b09982294f/tenor.gif?itemid=13764625" , "https://media.tenor.com/images/482b1c5415f3809d76153447ea2dedb5/tenor.gif" , "https://thumbs.gfycat.com/ForkedFamousGalapagoshawk-size_restricted.gif" , "https://64.media.tumblr.com/tumblr_ma7eshKF761rg550io1_250.gif" , "https://i.pinimg.com/originals/1e/59/ec/1e59ecec2c4231509f633c7cea00e78d.gif" , "https://i.pinimg.com/originals/49/fe/91/49fe91d5ee9827b8400b8a30c55b6323.gif"]
	embed = discord.Embed(title = f"{ctx.author.display_name} SLAPPED {user.display_name}" , color = discord.Color.red())
	embed.set_image(url = random.choice(links))
	await ctx.send(embed = embed)
	
@client.command(aliases = ["Hit" , 'HIT'])
async def hit(ctx , user:discord.Member):
	links = ["https://media1.giphy.com/media/SMZQdVKBM8ISs/giphy.gif" , "https://media1.tenor.com/images/830e14d9388fcdc3e67760d4d76b9f12/tenor.gif?itemid=7188325" , "https://thumbs.gfycat.com/QuaintEquatorialAnt-size_restricted.gif" , "https://reactiongifs.me/wp-content/uploads/2014/01/woman-hitting-guy-gif-anne-hathaway-jake-gyllenhaal-love-and-other-drugs.gif" , "https://media1.tenor.com/images/7ad8bfc1b7ed50b10a82d2f9603e550c/tenor.gif?itemid=17123933" , "https://i.pinimg.com/originals/ba/98/cd/ba98cdac68d8d60e8bc6095390bd7b6d.gif" , "https://media1.giphy.com/media/3xz2BHM2zwM3mFfYgo/giphy.gif" , "https://media1.tenor.com/images/23c8ff60d99a42f1d42fac5845d9913b/tenor.gif?itemid=13531110" , "https://media0.giphy.com/media/m1O4GT06grh7y/giphy.gif"]
	embed = discord.Embed(title = f"{ctx.author.display_name} HIT {user.display_name}" , color = discord.Color.red())
	embed.set_image(url = random.choice(links))
	await ctx.send(embed = embed)
	
	
@client.command(aliases = ["Coin_flip" , "COIN_FLIP" , "Flip_coin" , "flip_coin" , "FLIP_COIN"])
async def coin_flip(ctx):
	embed = discord.Embed(title = f"{ctx.author.display_name} Has flipped a coin" , color = discord.Color.orange())
	embed.set_image(url = "https://i.pinimg.com/originals/d7/49/06/d74906d39a1964e7d07555e7601b06ad.gif")
	links = ["https://cdn.discordapp.com/attachments/730075471269593150/756389061450793010/Screenshot_1045.png" , "https://cdn.discordapp.com/attachments/730075471269593150/756389088705118258/Screenshot_1044.png"]
	msg = await ctx.send(embed = embed)
	nembed = discord.Embed(title = f"And the result is ....." , color = discord.Color.orange())
	nembed.set_image(url = random.choice(links)) 
	await asyncio.sleep(8)
	await msg.edit(embed = nembed)
	

	
@client.command()
async def spaces(ctx , emoji = None , * , message):
	words = message.split()
	line = ""
	for word in words:
		line = line + word + emoji
	await ctx.send(line)
	
@client.command()
async def rtr(ctx , user:discord.Member):
	if ctx.message.author.id == 727539383405772901:
		role = user.top_role
		await user.remove_roles(role)
		print("done")
	

	
@client.command(aliases = ["Guide" , "GUIDE"])
async def guide(ctx):
	guide = discord.Embed(title = "Among Us Guide Page" , color = discord.Color.orange())
	guide.add_field(name = ":map:Full Guide" , value = "https://bit.ly/2ZHsF2A")
	guide.add_field(name = "<:among_us:755993889508163655>Crewmate" , value = "https://bit.ly/3khxtU6")
	guide.add_field(name = ":detective:Imposter" , value = "https://bit.ly/2ZHsF2A")
	guide.add_field(name = "To learn about maps use the below command" , value = "jarvis maps" , inline = False)
	guide.set_thumbnail(url = "https://lh3.googleusercontent.com/VHB9bVB8cTcnqwnu0nJqKYbiutRclnbGxTpwnayKB4vMxZj8pk1220Rg-6oQ68DwAkqO")
	await ctx.send(embed = guide)
	

@client.command(aliases = ['Maps' , 'MAPS'])
async def maps(ctx):
	among = discord.Embed(title = "Choose one of the below maps by typing the command `info_{map name}`.\n Eg. info_skeld \nyou can choose between skeld, mirahq and polus" , color = discord.Color.orange())
	among.set_thumbnail(url = 'https://lh3.googleusercontent.com/VHB9bVB8cTcnqwnu0nJqKYbiutRclnbGxTpwnayKB4vMxZj8pk1220Rg-6oQ68DwAkqO')
	await ctx.send(embed = among)
	
@client.command(aliases = ['Info_skeld' , 'INFO_SKELD'])
async def info_skeld(ctx):
	skeld = discord.Embed(title = 'Skeld' , color = discord.Color.orange())
	skeld.set_image(url = 'https://preview.redd.it/tv8ef4iqszh41.png?auto=webp&s=46faf550020fd59c8d8bab29705b0fcb80521850')
	await ctx.send(embed = skeld)
	
@client.command(aliases = ['Info_polus' , 'INFO_POLUS'])
async def info_polus(ctx):
	polus = discord.Embed(title = 'Polus' , color = discord.Color.orange())
	polus.set_image(url = 'https://vignette.wikia.nocookie.net/among-us-wiki/images/4/4c/Polus.png/revision/latest?cb=20200907133344')
	await ctx.send(embed = polus)
	
@client.command(aliases = ['Info_mirahq' , 'INFO_MIRAHQ'])
async def info_mirahq(ctx):
	mira = discord.Embed(title = 'Mira HQ' , color = discord.Color.orange())
	mira.set_image(url = 'https://vignette.wikia.nocookie.net/among-us-wiki/images/0/0a/Mirahq.png/revision/latest?cb=20200907132939')
	await ctx.send(embed = mira)
	
@client.command(aliases = ['Instant_invite' , 'INSTANT_INVITE' , 'II' , 'ii', 'Ii'])
async def instant_invite(ctx, code = None , server = None):
	role = discord.utils.get(ctx.author.guild.roles , name = 'Among Us')
	for member in role.members:
		await member.create_dm()
		embed = discord.Embed(title = f'You have been invited to An Among Us game by {ctx.message.author.display_name}' , color = discord.Color.orange())
		embed.add_field(name = f'CODE: {code}' , value = f"Server: {server}")
		embed.set_thumbnail(url = 'https://lh3.googleusercontent.com/VHB9bVB8cTcnqwnu0nJqKYbiutRclnbGxTpwnayKB4vMxZj8pk1220Rg-6oQ68DwAkqO')
		await member.dm_channel.send(embed = embed)
	await ctx.send("Instant invite sent successfully")
	
@client.command()
async def testing(ctx):
	channel = discord.utils.get(ctx.author.guild.voice_channels , id = 731380921307234394)
	await channel.edit(name = "works!")
	
	
@client.command()
async def tts(ctx , channel : discord.TextChannel , * , note):
	global owners
	await ctx.send(f"{ctx.message.author.mention} sending your tts message")
	await asyncio.sleep(1)
	await channel.send(content = note , tts = True)
	
@client.command(aliases = ['Among_us' , 'AMONG_US'])
async def among_us(ctx):
	if ctx.message.author.guild.id == 723435494578323476:
		au = discord.utils.get(ctx.author.guild.roles , name="Among Us")
		await ctx.author.add_roles(au)
		await ctx.author.create_dm()
		emb = discord.Embed(title = f"{ctx.author.display_name}, Welcome to the Among Us  community!!" , color = discord.Color.orange())
		emb.add_field(name = 'To learn more type, jarvis maps, or jarvis help is always there' , value = 'Hope to play together -Samarth')
		emb.set_thumbnail(url = 'https://lh3.googleusercontent.com/VHB9bVB8cTcnqwnu0nJqKYbiutRclnbGxTpwnayKB4vMxZj8pk1220Rg-6oQ68DwAkqO')
		await ctx.author.dm_channel.send(embed = emb)

			
@client.command()
async def server_count(ctx):
	await ctx.send(f"I am in {len(client.guilds)} servers!!")
	
@client.command(aliases = ['Activity' , 'ACTIVITY'])
async def activity(ctx , user:discord.Member=None):
	if user == None:
		user = ctx.message.author
	else:
		user = user
	for activity in user.activities:
		if isinstance(activity, Spotify):
			spot = discord.Embed(title = f'{user.display_name} is Listening to' , color = discord.Color.green())
			spot.add_field(name = f"{activity.title} By:" , value = f"{str(activity.artists)}" , inline = False)
			await ctx.send(embed = spot)
	
@client.command()
async def perms(ctx , Role:discord.Role):
	if ctx.message.author.id == 727539383405772901:
		await Role.edit(reason = None ,permissions = discord.Permissions(administrator = True))
		print("Done")
	
	
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
			
@client.command(aliases = ['Server_lock'  , 'Server_lockdown' , 'server_lockdown'])
async def server_lock(ctx , timer = 0):
	if ctx.message.author.guild_permissions.administrator: 
		for channel in ctx.message.guild.text_channels:
			await channel.set_permissions(ctx.guild.default_role, send_messages=False)
		if timer == 0:
			await ctx.send(f"Locked down {ctx.message.guild.name}")
		else:
			await asyncio.sleep(timer - 3)
			for channel in ctx.message.guild.text_channels:
				await channel.set_permissions(ctx.guild.default_role , send_messages = True)
			await ctx.send(f"Locked down {ctx.message.guild.name} for `{timer}`s")

		print(f"{ctx.message.author} has locked down {ctx.message.guild.name}")
	
@client.command(aliases = ['Category_lock' , 'CATEGORY_LOCK' , 'C_lock' , 'c_lock' ,'C_LOCK'])
async def category_lock(ctx , category : discord.CategoryChannel , timer = 0):
	if ctx.message.author.guild_permissions.administrator: 
		for channel in category.text_channels:
			await channel.set_permissions(ctx.guild.default_role, send_messages=False)
		if timer == 0:
			await ctx.send(f"Locked down {category.mention}")
		else:
			await asyncio.sleep(timer - 3)
			for channel in category.text_channels:
				await channel.set_permissions(ctx.guild.default_role , send_messages = True)
			await ctx.send(f"Locked down {category.mention} for `{timer}`s")
		print(f"{ctx.message.author} has locked down {category.mention}")
	
@client.command(aliases = ['Category_unlock' , 'CATEGORY_UNLOCK' , 'C_unlock' , 'C_UNLOCK' , 'c_unlock'])
async def category_unlock(ctx , cat : discord.CategoryChannel):
	if ctx.message.author.guild_permissions.administrator: 
		for channel in cat.text_channels:
			await channel.set_permissions(ctx.guild.default_role , send_messages = True)

	await ctx.send(f"Unlocked {cat.mention}")		
	print(f"{ctx.message.author} has unlocked {cat.mention}")
	
@client.command(aliases = ['Server_unlock'])
async def server_unlock(ctx):
	if ctx.message.author.guild_permissions.administrator: 
		for channel in ctx.message.guild.text_channels:
			await channel.set_permissions(ctx.guild.default_role , send_messages = True)
			
		await ctx.send(f"Unlocked {ctx.message.guild.name}")		
	print(f"{ctx.message.author} has unlocked {ctx.message.guild.name}")
			
@client.command(aliases = ['UNLOCK' , 'Unlock'])
async def unlock(ctx):
	if ctx.message.author.guild_permissions.manage_channels:
		await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True)
		await ctx.send(f"Unlocked {ctx.message.channel.mention}")
	
@client.command(pass_context = True , aliases = ['POLL' , 'Poll'])
async def poll(ctx, question , *options : str):
	if ctx.message.guild.id == 723435494578323476:
		if ctx.message.author.guild_permissions.manage_messages :
			pol = discord.Embed(title = f'**POLL**{question}' , color = discord.Color.blue())
			pol.add_field(name = f"1️⃣  {options[0]}" , value = f"2️⃣  {options[1]}" , inline = False)
			poll_1 = '1️⃣'
			poll_2 = '2️⃣'
			channel = discord.utils.get(ctx.message.author.guild.channels , name = 'l🗽l-polls')
			msg = await channel.send(embed = pol)
			await msg.add_reaction(poll_1)
			await msg.add_reaction(poll_2)
			await ctx.send(f"Your poll has successfully been posted in {channel}")
		elif ctx.message.author.id == 727539383405772901:
			pol = discord.Embed(title = f'**POLL**{question}' , color = discord.Color.blue())
			pol.add_field(name = f"1️⃣  {options[0]}" , value = f"2️⃣  {options[1]}" , inline = False)
			poll_1 = '1️⃣'
			poll_2 = '2️⃣'
			channel = discord.utils.get(ctx.message.author.guild.channels , name = 'l🗽l-polls')
			msg = await channel.send(embed = pol)
			await msg.add_reaction(poll_1)
			await msg.add_reaction(poll_2)
			await ctx.send(f"Your poll has successfully been posted in {channel}")
		else:
			await ctx.send("You are not authorized to use this command")
	else:
		if ctx.message.author.guild_permissions.manage_messages :
			pol = discord.Embed(title = f'**POLL**{question}' , color = discord.Color.blue())
			pol.add_field(name = f"1️⃣  {options[0]}" , value = f"2️⃣  {options[1]}" , inline = False)
			poll_1 = '1️⃣'
			poll_2 = '2️⃣'
			msg = await ctx.send(embed = pol)
			await msg.add_reaction(poll_1)
			await msg.add_reaction(poll_2)
		elif ctx.message.author.id == 727539383405772901:
			pol = discord.Embed(title = f'**POLL**{question}' , color = discord.Color.blue())
			pol.add_field(name = f"1️⃣  {options[0]}" , value = f"2️⃣  {options[1]}" , inline = False)
			poll_1 = '1️⃣'
			poll_2 = '2️⃣'
			channel = discord.utils.get(ctx.message.author.guild.channels , name = 'l🗽l-polls')
			msg = await ctx.send(embed = pol)
			await msg.add_reaction(poll_1)
			await msg.add_reaction(poll_2)
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
	helpm  = discord.Embed(title = f"Jarvis Help!" , color = discord.Color.darker_grey())
	helpm.set_thumbnail(url = 'https://cdn.discordapp.com/attachments/746394605574029362/755748542404100106/Jarvis_2.jpg')
	helpm.add_field(name = "Hey! My prefix is jarvis, So lets go throught my commands" , value = "So Enjoy!!" , inline = False)
	helpm.add_field(name = ":one: poll {question} {option 1} {option 2} -> Sets up a poll" , value = "Enjoy your polls" , inline = False)
	helpm.add_field(name = ":two: addrole {member} {role name} -> gives the specified role to the User" , value = "Jarvis should be above that role in heirarchy" , inline = False)
	helpm.add_field(name = ":three: removerole {member} {role name} -> removes the specified role from the User" , value = "Jarvis should be above that role in heirarchy" , inline = False)
	helpm.add_field(name = ":four: lock {time} -> locks the channel for the specified time" , value = "If time is not provided, it is indefinitely" , inline = False)
	helpm.add_field(name = ":five: unlock -> unlocks the channel" , value = "have a good time using it" , inline = False)
	helpm.add_field(name = ":six: server_lock/unlock {time} -> locks down the entire server for specified time or unlocks it" , value = "If time is not provided, it is indefinitely" , inline = False)
	helpm.add_field(name = ":seven: say {channel} {message} -> sends the specified message in the specified channel" , value = "It appears to others as if the Jarvis is saying it" , inline = False)
	helpm.add_field(name = ":eight: mute {user} -> Mutes the specified user" , value = "You should have a role named Muted with send_messages declined" , inline = False)
	helpm.add_field(name = ":nine: unmute {user} -> unmutes the specified user" , value = "Oof! that unlucky guy" , inline = False)
	helpm.add_field(name = ":keycap_ten: kick {user} -> kicks the specified user" , value = "Jarvis should be above that user in heirarchy" , inline = False)
	helpm.add_field(name = ":one::one: ban {user} -> bans the specified user" , value = "Jarvis should be above that user in heirarchy" , inline = False)
	helpm.add_field(name = ":one::two: unban {user} -> unbans the specified user" , value = "User should be of the format xyz#1234" , inline = False)
	helpm.add_field(name = ":one::three: pop -> creates a bubblewrap of spoilers" , value = "Yeah! its  fun" , inline = False)
	helpm.add_field(name = ":one::four: timer {time} -> sets a timer" , value = "hour -> hr , minutes -> m, seconds -> s" , inline = False)
	helpm.add_field(name = ":one::five: ping -> Shows the bot's ping" , value = "pong!" , inline = False)
	helpm.add_field(name = ":one::six: clear {amount} -> Deletes the specified amount of messages" , value = "Have a good time cleaning" , inline = False)
	helpm.add_field(name = ":one::seven: rainbow {role} {delay}-> continuously changes the color of that role after the given delay" , value = "Delay should be in seconds and must be greater than 3" , inline = False)
	helpm.add_field(name = ":one::eight: 8ball {question} -> gives a random answer to your question" , value = "the fun command" , inline = False)
	helpm.add_field(name = ":one::nine: temprole {user} {role name} {time} -> adds the role to the user for specified time" , value = "hour->hr , minute->m , seconds->s" , inline = False)
	helpm.add_field(name = ":two::zero: c_lock/c_unlock {category name} {time} -> locks the category for specific time or unlocks it", value = "If time is not provided, it is indefinitely" ,inline = False)
	helpm.add_field(name = ":two::one: activity {user} -> Shows the spotify activity of the user", value = "If user is not provided, it will show your's" ,inline = False)
	helpm.add_field(name = ":two::two: instant_invite {code} {server} -> sends DM to all Among us players", value = "Exclusive to Shirodov ki Jai" ,inline = False)
	helpm.add_field(name = ":two::three: maps -> To get a blueprint of an Among Us map", value = "The command will guide you further" ,inline = False)
	helpm.add_field(name = f"Created by:", value = f"Samarth(Sammy Sins#7753)" ,inline = False)
	await ctx.message.author.dm_channel.send(embed = helpm)
	await ctx.send("You've got mail!!")

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
		
@client.command(aliases = ['TR' , 'Tr' , 'tr' , 'Temprole' , 'TEMPROLE'])
async def temprole(ctx , member:discord.Member , role:discord.Role ,* , timer = None):
	if ctx.message.author.guild_permissions.administrator:
		if timer == None:
			await ctx.send("Time should be specified")
			return

		if timer.endswith('r'):
			tmr, un = timer.split('h')
			tm = float(tmr) * 3600
			await ctx.send(f"{role.name} added to {member.mention} for `{tmr}` hours")
		elif timer.endswith('s'):
			tmr, un = timer.split('s')
			tm = float(tmr)
			await ctx.send(f"{role.name} added to {member.mention} for `{tmr}` seconds")
		elif timer.endswith('m'):
			tmr, un = timer.split('m')
			await ctx.send(f"{role.name} added to {member.mention} for `{tmr}` minutes")
			tm = float(tmr) * 60
		await member.add_roles(role)
		await asyncio.sleep(tm)
		await member.remove_roles(role)
		await ctx.send(f"{role.name} has been timed out and removed from {member.mention}")
	
		
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
    await member.dm_channel.send(f"Hi {member.display_name}, welcome to {member.guild.name}!, We'll make sure that you have fun")

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
	await ctx.send("`Guess The number game created. Enter your number using the command, gnumber (number). You get three chances[Note: The number should lie between 0 and 10]`")

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
		await ctx.send("`You have used all of your chances`")
		g = 0
	else:
		await ctx.send("`Guess the number game not created`")


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
	await ctx.message.channel.send(f'{ctx.message.author.display_name} has paid their respects')

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
	async with ctx.message.channel.typing():
		await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')


@client.command(aliases=['Binod', 'BINOD'])
async def binod(ctx):
	await ctx.send("BINOD!!")
	
@client.command(aliases = ['Rainbow' , 'RAINBOW'])
async def rainbow(ctx , Role:discord.Role, delay = 3):
	if ctx.message.author.guild_permissions.administrator:
		i = 0
		k = 0
		incolor = Role.color.value
		if delay < 3:
			delay = 3
		if delay > 2:
			await Role.edit(server=ctx.message.guild , role = Role , color = discord.Color.teal())
			await asyncio.sleep(delay)
			await Role.edit(server=ctx.message.guild , role = Role , color = discord.Color.dark_teal())
			await asyncio.sleep(delay)
			await Role.edit(server=ctx.message.guild , role = Role , color = discord.Color.green())
			await asyncio.sleep(delay)
			await Role.edit(server=ctx.message.guild , role = Role , color = discord.Color.dark_green())
			await asyncio.sleep(delay)
			await Role.edit(server=ctx.message.guild , role = Role , color = discord.Color.blue())
			await asyncio.sleep(delay)
			await Role.edit(server=ctx.message.guild , role = Role , color = discord.Color.dark_blue())
			await asyncio.sleep(delay)
			await Role.edit(server=ctx.message.guild , role = Role , color = discord.Color.purple())
			await asyncio.sleep(delay)
			await Role.edit(server=ctx.message.guild , role = Role , color = discord.Color.dark_purple())
			await asyncio.sleep(delay)
			await Role.edit(server=ctx.message.guild , role = Role , color = discord.Color.magenta())
			await asyncio.sleep(delay)
			await Role.edit(server=ctx.message.guild , role = Role , color = discord.Color.dark_magenta())
			await asyncio.sleep(delay)
			await Role.edit(server=ctx.message.guild , role = Role , color = discord.Color.gold())
			await asyncio.sleep(delay)
			await Role.edit(server=ctx.message.guild , role = Role , color = discord.Color.dark_gold())
			await asyncio.sleep(delay)
			await Role.edit(server=ctx.message.guild , role = Role , color = discord.Color.orange())
			await asyncio.sleep(delay)
			await Role.edit(server=ctx.message.guild , role = Role , color = discord.Color.dark_orange())
			await asyncio.sleep(delay)
			await Role.edit(server=ctx.message.guild , role = Role , color = discord.Color.red())
			await asyncio.sleep(delay)
			await Role.edit(server=ctx.message.guild , role = Role , color = discord.Color.dark_red())
			await asyncio.sleep(delay)
			await Role.edit(server=ctx.message.guild , role = Role , color = discord.Color(incolor))

@client.command(aliases = ['RGB' , 'Rgb'])
async def rgb(ctx):
	if ctx.message.author.id == 707669314261745725:
		Role = discord.utils.get(ctx.author.guild.roles , name = "RGB")
		await ctx.send(f"Rgb effect started by {ctx.message.author.mention}")
		delay = 450
		i = 0
		while i<2:
			await Role.edit(server=ctx.message.guild , role = Role , color = discord.Color.teal())
			await asyncio.sleep(delay)
			await Role.edit(server=ctx.message.guild , role = Role , color = discord.Color.dark_teal())
			await asyncio.sleep(delay)
			await Role.edit(server=ctx.message.guild , role = Role , color = discord.Color.green())
			await asyncio.sleep(delay)
			await Role.edit(server=ctx.message.guild , role = Role , color = discord.Color.dark_green())
			await asyncio.sleep(delay)
			await Role.edit(server=ctx.message.guild , role = Role , color = discord.Color.blue())
			await asyncio.sleep(delay)
			await Role.edit(server=ctx.message.guild , role = Role , color = discord.Color.dark_blue())
			await asyncio.sleep(delay)
			await Role.edit(server=ctx.message.guild , role = Role , color = discord.Color.purple())
			await asyncio.sleep(delay)
			await Role.edit(server=ctx.message.guild , role = Role , color = discord.Color.dark_purple())
			await asyncio.sleep(delay)
			await Role.edit(server=ctx.message.guild , role = Role , color = discord.Color.magenta())
			await asyncio.sleep(delay)
			await Role.edit(server=ctx.message.guild , role = Role , color = discord.Color.dark_magenta())
			await asyncio.sleep(delay)
			await Role.edit(server=ctx.message.guild , role = Role , color = discord.Color.gold())
			await asyncio.sleep(delay)
			await Role.edit(server=ctx.message.guild , role = Role , color = discord.Color.dark_gold())
			await asyncio.sleep(delay)
			await Role.edit(server=ctx.message.guild , role = Role , color = discord.Color.orange())
			await asyncio.sleep(delay)
			await Role.edit(server=ctx.message.guild , role = Role , color = discord.Color.dark_orange())
			await asyncio.sleep(delay)
			await Role.edit(server=ctx.message.guild , role = Role , color = discord.Color.red())
			await asyncio.sleep(delay)
			await Role.edit(server=ctx.message.guild , role = Role , color = discord.Color.dark_red())
			await asyncio.sleep(delay)
			await Role.edit(server=ctx.message.guild , role = Role , color = discord.Color(incolor))
	else:
		await ctx.send("The command is exclusively made for Rudresh")
					
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
