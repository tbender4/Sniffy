import json
import os
import random
import discord
from messages import *
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
displayTypes = {
        "shaft": "{0}mm",
        #"grommet": "{0}A",
        "actuator": "{0}mm"
}
def parseMessage (message):         # The first point of contact for Sniffy.
  messageString = message.content  #pass through full message from main program.
  print("Original message: " + messageString)
  messageString = messageString.lower()

  #convert message to an array of parameters
  messageString = messageString[1:]   #removes prefix
  parameters = messageString.split()
  print(parameters)

  #reply = "Here's your info, " + str(message.author.mention) + "!\n"
  #reply += "you said: " + message.content
  return parameters

def processArguments (parameters):  #returns a message string OR None
  validArg0 = ["info", "help"] #later implement: compare
  validArg1 = ["lever"] #later implement: switch, grommet

  data = {} #empty data dictionary

  if parameters[0] not in validArg0:        #ignore invalid parameters
      return confused

  if parameters[0] == "help":
      return helpMessage

  if parameters[1] not in validArg1:
      return confused

  if parameters[1] == "lever":
    absolutePath = os.path.dirname(__file__)
    with open(absolutePath + "/json/levers.json", "r") as data:
      data = json.load(data)  #imports entire json file

      if len(parameters) == 2:
          randomKeyAppendedParameter = parameters.append(random.choice(data.keys())
          output = "Available options: " + listOptions(data, parameters)
          output += "\n Available filters: " + listOptions(data.keys()[0], randomKeyAppendedParameter)
          return  output
      subData = data[parameters[2]]
      
      if len(parameters) > 3:
          subData = filterMode(subData, parameters[3:]) #filters dictionary with parameters
      print(subData)
      #return dataToString(subData)
      return dataToEmbed(subData)
    return confused
def filterMode(data, parameters)    #dictionary, list of parameters
    if parameters

def listOptions(data, parameters): #exports keys to a list
    output = ""
    for key in data.keys():
        output += "`{}`, ".format(key)
    output = output[:-2] + "\n"    #removes extra ", "
    output += "Example: "
    for parameter in parameters:
        output += "`{}` ".format(parameter)
    output += random.choice(data.keys())
    
    return output

def dataToEmbed(data):      #TODO: make this code cleaner
  randomColor = int("0x{:06x}".format(random.randint(0, 0xFFFFFF)), 16)
  print(randomColor)
  embeddedResult = discord.Embed(colour=randomColor)

  index = 0
  for key in data:
    if key == "logo":                               #direct img URL
        embeddedResult.set_thumbnail(data[key])
    elif key = "availability":
        output = ""
        if data[key] == True:
            output = "In Stock"
        else:
            output = "Discontinued"
        embeddedResult.add_field(name=displayNames[index], value=output)
    elif data[key] == displayTypes[key]:            #adds unit to measurements
        output = displayTypes[key].format(data[key])
        embeddedResult.add_field(name=displayNames[index], value=output)
    else:
        embeddedResult.add_field(name=displayNames[index], value=data[key])
    index += 1      #iterates for displayNames
  
  embeddedResult.set_footer(text="Report inaccuracies to @thomasbender#9249")
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
      
