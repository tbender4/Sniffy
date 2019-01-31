import json
import os
#tools to format strings

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
      return formatData(subData)
  
def formatData(data):       #formats data to a Discord-friendly string
  #IMPORTANT: replace with Webhooks eventually
  #Until then format string from dictionary
  output = "\n"
  for i in data:
    if i != "isSuperceded":
      output += i + ": " + str(data[i]) + "\n"  #battop: Fanta
  print (output)
  return output
      