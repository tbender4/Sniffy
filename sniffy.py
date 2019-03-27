import discord
from auth import token
from tools import parseMessage, processArguments, infoMode, compareMode
from messages import confused  #helpMessage, confused
#import asyncio 

client = discord.Client()
prefix = "~"



@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):

  if message.author.bot: #will ignore bots
    return

  if message.content.startswith(prefix):
    parameters = parseMessage(message)
    #await message.channel.send("test")
    if len(parameters) == 0:
      await message.channel.send(confused)
      return
    elif parameters[0] == "info":
      output = infoMode(parameters)
      if isinstance(output, discord.Embed):
        await message.channel.send(embed=output)
      else:
        await message.channel.send(output)
        return
    elif parameters[0] == "compare":
      replies = compareMode(parameters)
      if replies[0] == confused:
        await message.channel.send(replies[0])
        return
      for reply in replies:
        await message.channel.send(embed=reply)

client.run(token)
