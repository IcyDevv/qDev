import discord
import os

from discord.ext import commands
from keep_alive import keep_alive

client = discord.Client()
bot = commands.Bot(command_prefix="!")
val = None

@client.event
async def on_ready():
    print("Online!")
    print(client.user)

@bot.command()
async def setup(ctx,*,channel):
     author = ctx.message.author
     await ctx.send("Setup successfull!")
     file = open("channels.txt", "a+")
     file.write(str(author)+" : "+channel+"n/")
     val = channel


@bot.command()
async def post(ctx,jobtype,aboutjob,*,payment):
    author = ctx.message.author
    file = open("posts.txt", "a+")
    file.write(str(author)+" : "+jobtype+aboutjob+payment+"n/")
    str
    embed = discord.Embed(
        title = "Job Post",
        description = "offered by..",
        colour = discord.Colour.blue()
    )

    embed.set_footer(text = "Made by Icy_Devv with discord.py")
    embed.set_author(name = "qDev#2580")
    embed.add_field(name = "Job Type", value = jobtype)
    embed.add_field(name = "About the job", value = aboutjob)
    embed.add_field(name = "Payment", value = payment)
    await ctx.send("Job Post Submitted!")
    channel = bot.get_channel(val)
    message = await channel.send(embed=embed)
    await message.add_reaction('❤️')
    await message.add_reaction('🔒')
    if client.

    


keep_alive()
token = ("TOKEN HERE")
bot.run(token)