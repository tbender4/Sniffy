Sniffy is a Discord bot that prints lever information on demand.

## Requirements:
- Python 3.7
- Git (recommended)
- discord.py 
- A valid authorization token

## Installation
First get the discord.py rewrite branch for python using Terminal/Command Line:

 - Unix OS (macOS, Linux):
```
pip install -U discord.py
```
 - Windows:
```
py -m pip install -U discord.py
```
Then grab the bot's source code:
```
git clone https://github.com/tbender4/Sniffy.git
cd sniffy
```
See [this guide](https://github.com/reactiflux/discord-irc/wiki/Creating-a-discord-bot-&-getting-a-token) to generate a unique authorization token. Add your token to `auth.py` in the following format:
```python
token = "YOUR_TOKEN_HERE"
```
Note: Keep the token surrounded by parentheses.

Finally, run the bot with:
```python3 sniffy.py```

If you wish to run the bot in the background for a headless instance, run the bot with:
```nohup python3 sniffy.py &```

## Usage

Info mode:
Prints information about a given lever. Send `~info LEVER` in any channel the bot has presence in. If you want to only show specific information, send `~info LEVER FILTER1 FILTER2 FILTER3...`.
To list all of the available levers and filters, simply send `~info`.

Compare mode:
Compares two different levers and prints the differences. Send `~compare LEVER1 LEVER2` in any channel the bot has presence in. To list all of the available levers, simply send `~compare`.

The database of levers are kept in `json/levers.json`.
Logos are kept in `logos/`.
