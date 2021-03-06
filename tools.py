import json
import os
import random
import discord
from messages import confused, helpMessage
#tools to format strings


leverDisplayNames = {
  "name": "Name: ",
  "is_available": "Availability: ",
  "battop": "Battop: ",
  "shaft": "Shaft Diameter: ",
  "mount": "Mount: ",
  "collar": "Collar Type: ",
  "base": "Base: ",
  "bushing": "Bushing: ",
  "spring": "Uses Spring: ",
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
  messageString = messageString.strip()
  messageString = messageString[1:]   #removes prefix

  #convert message to an array of parameters
  parameters = messageString.split()
  return parameters

def infoMode(parameters):
  data = {}   #working dictionary
  absolutePath = os.path.dirname(__file__)
  with open(absolutePath + "/json/levers.json", "r") as data:
    data = json.load(data)  #imports entire json file

  if len(parameters) == 1:
    output = "**Available options:**\n" + listOptions(data, parameters)
    output += "\n\n**Available (optional) filters:**\n" + listFilters(data, parameters)
    return output

  subData = data[parameters[1]]   #info myoungshin <- subDictionary from 'myoungshin' key
                                  #TODO Exception handling for invalid keys
  if len(parameters) > 2:         #info myoungshin grommet
    subData = filterMode(subData, parameters[2:]) #filters dictionary with all keys user specifies
    print(subData)
    #return dataToString(subData)
  return dataToEmbed(subData)

def boldDataValues (dictionary):
  for key in dictionary:
    dictionary.update({key: "**" + dictionary[key] + "**"})
  return dictionary

def formatData(data):   #convert all to String with appropriate formatting
  for key in data:
    if key == "spring":
      if data[key] == True:
        data.update({key:"Yes"})
      else:
        data.update({key:"No"})
    if key == "is_available":
      if data[key] == True:
        data.update({key:"Available"})
      else:
        data.update({key:"Unavailable"})
    elif isinstance(data[key], (int, float)) and not isinstance(data[key], bool):
      data.update({key:str(data[key]) + "mm"})
  return data

def compareMode(parameters):
  #parameters = "compare myoungshin taeyoung"
  data = {}   #working dictionary
  absolutePath = os.path.dirname(__file__)
  with open(absolutePath + "/json/levers.json", "r") as data:
    data = json.load(data)  #imports entire json file
  
  if len(parameters) == 1:
    output = "**Available options:**\n" + listOptions(data, parameters)
    return output

  if len(parameters) != 3:
    return [confused]   #TODO make dedicated description of compare mode

  # convert all values to string + pre-format TODO: clean up dataToEmbed code.
  lever1 = data[parameters[1]]  #data[myoungshin]
  lever2 = data[parameters[2]]  #data[taeyoung]
  #lever1 = formatData(data[parameters[1]]) #data[myoungshin]
  #lever2 = formatData(data[parameters[2]]) #data[taeyoung]
  lever1Diff = {}
  lever2Diff = {}
  common = {}
  for key in lever1:
    if lever1[key] == lever2[key]:
      common.update({key: lever1[key]})
    else:
      lever1Diff.update({key: lever1[key]})
      lever2Diff.update({key: lever2[key]})

  lever1Embed = dataToEmbed(lever1Diff)
  lever2Embed = dataToEmbed(lever2Diff)
  #TODO: Properly implement bold
  #lever1Embed = dataToEmbed(boldDataValues(lever1Diff))
  #lever2Embed = dataToEmbed(boldDataValues(lever2Diff))
  commonEmbed = dataToEmbed(common)
  lever1Embed.set_author(name=parameters[1])
  lever2Embed.set_author(name=parameters[2])
  commonEmbed.set_author(name="Common in both")
  return  [lever1Embed, lever2Embed, commonEmbed]

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
          output = "**Available options:**\n" + listOptions(data, parameters)
          
          
          output += "\n\n**Available (optional) filters:**\n" + listFilters(data, parameters)
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
  if parameter[0] == "compare":
    randomColor = str(random.choice(list(data)))
    randomColor2 = str(random.choice(list(data)))
    while (randomColor2 == random):
      randomColor2 = random.choice(list(data))
    output += randomColor
    output += randomColor2

  output += "`"
  
  return output


def dataToEmbed(data):      #TODO: make this code cleaner
  randomColor = int("0x{:06x}".format(random.randint(0, 0xFFFFFF)), 16)
  print(randomColor)
  embeddedResult = discord.Embed(colour=randomColor)
  data = formatData(data)
  print(len(data.keys()))
  for key in data:
    if key == "logo":
      embeddedResult.set_thumbnail(url=data[key])
    else:
      embeddedResult.add_field(name=leverDisplayNames[key], value=data[key])
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
      
