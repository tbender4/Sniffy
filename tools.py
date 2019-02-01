import json
import os
import random
import discord
#tools to format strings

displayNames = [
    "Name: ",
    "Availability: ",
    "Battop: ",
    "Shaft Diameter: ",
    "Collar type: ",
    "Base: ",
    "Bushing: ",
    "Grommet Hardness: ",
    "Actuator Diameter: ",
    "Switch Model: ",
    "Switch Spacing: ",
    "Notes: ",
    "Superceded By: "
  ]
def parseMessage (message):         # The first point of contact for Sniffy.
  messageString = message.content  #pass through full message from main program.
  print("Original message: " + messageString)
  messageString = messageString.lower()

  #convert message to an array of parameters
  messageString = messageString[1:]   #removes prefix
  parameters = messageString.split()
  print(parameters)

  reply = "Here's your info, " + str(message.author.mention) + "!\n"
  reply += "you said: " + message.content
  return parameters

def processArguments (parameters):  #returns a message string OR None
  validArg0 = ["info"] #later implement: compare
  validArg1 = ["lever"] #later implement: switch, grommet

  data = {} #empty data dictionary
  
  if parameters[0] not in validArg0:        #ignore invalid parameters
      return 
  if parameters[1] not in validArg1:
      return

  if parameters[1] == "lever":
    absolutePath = os.path.dirname(__file__)
    with open(absolutePath + "/json/levers.json", "r") as data:
      data = json.load(data)  #imports entire json file

      subData = data[parameters[2]]
      print(subData)
      #return dataToString(subData)
      return dataToEmbed(subData)

def dataToEmbed(data):
  randomColor = int("0x{:06x}".format(random.randint(0, 0xFFFFFF)), 16)
  print(randomColor)
  embeddedResult = discord.Embed(colour=randomColor)

  index = 0
  for key in data:
    embeddedResult.add_field(name=displayNames[index], value=data[key])
    index += 1
  
  return embeddedResult
  
def dataToString(data):       #formats data to a Discord-friendly string
  #IMPORTANT: replace with Webhooks eventually
  #Until then format string from dictionary
  output = "\n"

  index = 0  # iterating displayNames
  for key in data:
    newLine = "**" + displayNames[index] + ":** " + str(data[key]) + "\n"  #battop: Fanta
    output += newLine
    index += 1
  print (output)
  return output
      
