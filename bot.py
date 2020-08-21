import discord
from discord.ext import commands, tasks
import random
from itertools import cycle
import youtube_dl
import json
import asyncio
import shutil
import os
from discord.utils import get

client = commands.Bot(command_prefix="")
status = cycle(['Fortnite on Android', 'Fortnite on Iphone'])

@client.event
async def on_ready():
	change_status.start()
	print("Bot is ready.")

@client.command(aliases=['hi' , 'Hi' , 'Hola' , 'Sup'])
async def hello(ctx):
	await ctx.send("Hi there!")

@client.command()
async def unban(ctx, *, mamber):
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

@client.command()
async def oof(ctx):
	await ctx.send("OOF!")

@client.command(aliases=['clean'])
async def clear(ctx, amount=5):
	await ctx.channel.purge(limit=amount)

@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):
	await member.kick(reason=reason)
	await ctx.send(f'Kicked {member.mention}')

@client.command()
async def ban(ctx, member : discord.Member, *, reason=None):
	await member.ban(reason=reason)
	await ctx.send(f'Banned {member.mention}')

@tasks.loop(minutes=15)
async def change_status():
	await client.change_presence(activity=discord.Game(next(status)))


@client.command()
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



@client.command()
async def binod(ctx):
	await ctx.send("BINOD!!")

player = {}

@client.command(pass_context=True)
async def join(ctx):
	global voice
	channel = ctx.message.author.voice.channel
	voice = get(client.voice_clients, guild=ctx.guild)
	if voice and voice.is_connected():
		await voice.move_to(channel)
	else:
		voice = await channel.connect()
	await ctx.send(f'joined {channel}')

@client.command(pass_context=True)
async def leave(ctx):
	channel = ctx.message.author.voice.channel
	voice = get(client.voice_clients, guild=ctx.guild)

	if voice and voice.is_connected():
		await voice.disconnect()
		await ctx.send(f'Left {channel}')

@client.command(pass_context=True, aliases=['p'])
async def play(ctx, url: str):

	def check_queue():
		Queue_infile = os.path.isdir("./Queue")
		if Queue_infile is True:
			DIR = os.path.abspath(os.path.realpath("Queue"))
			length = len(os.listdir(DIR))
			still_q = length - 1
			try:
				first_file = os.listdir(DIR)[0]
			except:
				print("No more queued song(s)\n")
				queues.clear()
				return
			main_location = os.path.dirname(os.path.realpath(__file__))
			sing_path = os.path.abspath(os.path.realpath("Queue") + "\\" + first__file)
			if length != 0:
				print("Song done. playing nest queued\n")
				print(f'Songs still in queue: {still_q}')
				song_there = os.path.isfile("song.mp3")
				if song_there:
					os.remove("song.mp3")
				shutil.move(song_path, main_location)
				for file in os.listdir("./"):
					if file.endswith(".mp3"):
						os.rename(file, 'song.mp3')

				voice.play(discord.FFmpegPCMAudio("song.mp3"), after=lambda e: check_queue())
				voice.source = discord.PCMvolumrTransformer(voice.soure)
				voice.source.volume = 0.07

			else:
				queues.clear()
				return

		else:
			queues.clear()
			print("No songs were queued defore the ending of the last song\n")


	song_there = os.path.isfile("song.mp3")
	try:
		if song_there:
			os.remove("song.mp3")
			queues.clear()
			print("removed old song file")
	except PermissionError:
		print("Trying to delete song file, but it's being played")
		await ctx.send("ERROR: Music playing")
		return

	Queue_infile = os.path.isdir("./Queue")
	try:
		Queue_folder = "./Queue"
		if Queue_infile is True:
			print("Removed old Queue Folder")
			shutil.rmtree(Queue_folder)
	except:
		print("No old queue folder")

	await ctx.send("Getting everything ready now")

	voice = get(client.voice_clients, guild=ctx.guild)

	ydl_opts = {
		'format': 'bestaudio/best',
		'quiet': True,
		'postprocessors':[{
			'key':'FFmpegExtractAudio',
			'preferredcodec':'mp3',
			'preferredquality':'192',
		}],
	}

	with youtube_dl.YoutubeDL(ydl_opts) as ydl:
		print("Downloading audio now\n")
		ydl.download([url])

	for file in os.listdir("./"):
		if file.endswith(".mp3"):
			name = file
			print(f'Renamed File: {file}\n')
			os.rename(file, "song.mp3")

	voice.play(discord.FFmpegPCMAudio("song.mp3"), after=lambda e: check_queue())
	voice.source = discord.PCMVolumeTransformer(voice.source)
	voice.source.volume = 0.07

	nname = name.rsplit(".", 2)
	await ctx.send(f'Playing: {nname[0]}')
	print("Playing\n")

@client.command(pass_context=True, aliases=['stop'])
async def pause(ctx):

	voice = get(client.voice_clients, guild=ctx.guild)

	if voice and voice.is_playing():
		print("Music paused")
		voice.pause()
		await ctx.send("Music Paused")
	else:
		print("Music not playing failed pause")
		await ctx.send("Music not playing failed pause")

@client.command(pass_context=True)
async def resume(ctx):

	voice = get(client.voice_clients, guild=ctx.guild)

	if voice and voice.is_paused():
		print("Resumed Music")
		voice.resume()
		await ctx.send("Resumed Music")
	else:
		print("Music is not paused")
		await ctx.send("Music is not paused")


client.run("NzQ1OTU1OTkwNzY3NDAzMDM5.Xz5Tpw.EjdNUpcusLZkCXdk8GUTSKfUqDQ")