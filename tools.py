#tools to format strings

def parseMessage (message):
  messageString = message.content
  print(messageString)
  messageString.lower()

  messageString = messageString[1:]   #removes prefix
  parameters = messageString.split()
  print(parameters)

  return messageString
#pass through full message from main program.
#will get extracted here