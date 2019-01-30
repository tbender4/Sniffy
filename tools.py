import json
import os
#tools to format strings

def parseMessage (message):         # The first point of contact for Sniffy.
  messageString = message.content  #pass through full message from main program.
  print("Original message: " + messageString)
  messageString.lower()

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
  validArg2 = [] #pull from JSON

  data = {} #empty data dictionary
  if parameters[1] == "lever":
    absolutePath = os.path.dirname(__file__)
    with open(absolutePath + "/json/levers.json", "r") as data:
      levers = json.load(data)  #imports entire json file
      data = levers
  
  subData = data[parameters[2]]
  print(subData)