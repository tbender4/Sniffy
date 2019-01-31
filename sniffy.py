import discord
from auth import token
from tools import parseMessage, processArguments
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
  
  if str(message.content).strip == prefix:
    return

  if message.content.startswith(prefix):
    parameters = parseMessage(message)
    if len(parameters) < 2 or parameters == None:
      return
    reply = processArguments(parameters)  #gets back after returning an argument
    await client.send_message(message.channel, reply)

client.run(token)