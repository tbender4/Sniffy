import json
import os
import random
import discord
from messages import *
#tools to format strings


leverDisplayNames = {
  "name": "Name: ",
  "is_available": "Availability: ",
  "battop": "Battop: ",
  "shaft": "Shaft Diameter: ",
  "collar": "Collar Type: ",
  "base": "Base: ",
  "bushing": "Bushing: ",
  "grommet": "Grommet Tension: ",
  "actuator": "Actuator Diameter: ",
  "switch": "Switch Model: ",
  "switch_spacing": "Switch Spacing: ",
  "notes": "Notes: "
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

  if parameters[0] == "help":
      return helpMessage

  if parameters[0] not in validArg0:        #ignore invalid parameters
      return confused
  if parameters[1] not in validArg1:
      return confused

  if parameters[1] == "lever":
    absolutePath = os.path.dirname(__file__)
    with open(absolutePath + "/json/levers.json", "r") as data:
      data = json.load(data)  #imports entire json file

      if len(parameters) == 2:
          output = "Available options:\n" + listOptions(data, parameters)
          
          
          output += "\n\n Available filters:\n" + listFilters(data, parameters)
          return output

      subData = data[parameters[2]]
      
      if len(parameters) > 3:
          subData = filterMode(subData, parameters[3:]) #filters dictionary with parameters
      print(subData)
      #return dataToString(subData)
      return dataToEmbed(subData)
    return confused

def filterMode(data, parameters):   #dictionary, list of parameters
  filteredData = {}
  for parameter in parameters:
    if parameter in data:
      filteredData.update({parameter:data[parameter]})
  return filteredData

def listFilters(data, parameters): #exports keys to a list
  filterData = data[list(data)[0]]
  filterParameters = parameters
  filterParameters.append(random.choice(list(data)))

  print("~~~~~~~~~~~~~~~~~LIST FILTERS~~~~~~~~~~~~~~~~~~")
  print(filterData)

  print(filterParameters)

  output = listOptions(filterData, filterParameters)  #reuse of listOptions
  output += "\n Note: multiple filters can be chained."
  return output

def listOptions(data, parameters): #exports keys to a list
  output = ""
  for key in data:
    output += "`{}`, ".format(key)
  output = output[:-2] + "\n"    #removes extra ", "
  output += "Example: `~"
  for parameter in parameters: #prints out existing parameters, then adds a random parameter
    output += "{} ".format(parameter)
  output += random.choice(list(data))
  output += "`"
  
  return output

def dataToEmbed(data):      #TODO: make this code cleaner
  randomColor = int("0x{:06x}".format(random.randint(0, 0xFFFFFF)), 16)
  print(randomColor)
  embeddedResult = discord.Embed(colour=randomColor)
  index = 0
  #embeddedResult.set_thumbnail(url=data["logo"])
  print(len(data.keys()))
  for key in data:
    if key == "logo":
      embeddedResult.set_thumbnail(url=data[key])
    elif key == "isAvailable":
      status = ""
      if data[key] == True:
        status = "In Stock"
      else:
        status = "Discontinued"
      embeddedResult.add_field(name=leverDisplayNames[key], value=status)
    elif isinstance(data[key], (int, float)) and not isinstance(data[key], bool):
      measurementWithUnit = str(data[key]) + "mm"
      embeddedResult.add_field(name=leverDisplayNames[key], value=measurementWithUnit)
    else:
      embeddedResult.add_field(name=leverDisplayNames[key], value=data[key])
  return embeddedResult

  for key in data:
    if key == "logo":                               #direct img URL
      embeddedResult.set_thumbnail(url=data[key])
      print("logo")
    elif key == "isAvailable":
      output = ""
      if data[key] == True:
        output = "In Stock"
      else:
        output = "Discontinued"
      print(output)
      embeddedResult.add_field(name=leverDisplayNames[key], value=output)
    elif isinstance(data[key], int) or isinstance(data[key], float):            #adds unit to measurements
      output = str(data[key]) + "mm"
      print(output)
      embeddedResult.add_field(name=leverDisplayNames[key], value=output)
    else:
      print(data[key])
      embeddedResult.add_field(name=leverDisplayNames[key], value=data[key])
    index += 1      #iteratleverDisplayNames[key]
  return embeddedResult
  
def dataToString(data):       #formats data to a Discord-friendly string
  #IMPORTANT: replace with Webhooks eventually
  #Until then format string from dictionary
  output = "\n"

  index = 0  # iteleverDisplayNames[key]
  for key in data:
    newLine = "**" + leverDisplayNames[key] + ":** " + str(data[key]) + "\n"  #battop: Fanta
    output += newLine
    index += 1
  print (output)
  return output
      
