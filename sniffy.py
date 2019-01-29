import discord
from auth import token
#import asyncio 

client = discord.Client()
prefix = "?"

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  if message.content.startswith(prefix):
    reply = "Got your message, " + str(message.author.mention) + "!\n"
    reply += "you said: " + message.content
    print(reply)
    await client.send_message(message.channel, reply)
    

client.run(token)