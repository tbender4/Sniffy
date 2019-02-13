import discord
from auth import token
from tools import parseMessage, processArguments, infoMode
from messages import confused  #helpMessage, confused
#import asyncio 

client = discord.Client()
prefix = "~"



@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  def sendMessage(reply):
    if type(reply) is str:
      await client.send_message(message.channel, reply)
    else:
      await client.send_message(message.channel, embed=reply)
    return

  if message.author.bot: #will ignore bots
    return

  if message.content.startswith(prefix):
    parameters = parseMessage(message)
    if len(parameters) == 0:
      sendMessage(confused)
    elif parameters[0] == "info":
      sendMessage(infoMode(parameters))
    elif parameters[0] == "compare":
      replies = sendMessage(compareMode(parameters))
      for reply in replies:
        sendMessage(reply)

client.run(token)
