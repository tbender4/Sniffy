import discord
from auth import token
from tools import parseMessage, processArguments
from messages import *  #helpMessage, confused
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
    await client.send_message(message.channel, confused)
    return

  if message.content.startswith(prefix):
    parameters = parseMessage(message)
    reply = processArguments(parameters)  #gets back either an str or a discord.Embed
    if type(reply) is str:
        await client.send_message(message.channel, reply)
    else:
        await client.send_message(message.channel, embed=reply)

client.run(token)
