Sniffy is a Discord bot that prints lever information on demand.

## Requirements:
- Python 3.7
- Git (recommended)
- discord.py **rewrite branch**
- A valid authorization token as string variable in `auth.py`

## Installation
First get the discord.py rewrite branch for python using Terminal/Command Line:

 - Unix OS (macOS, Linux):
```
pip install -U git+https://github.com/Rapptz/discord.py@rewrite
```
 - Windows:
```
py -m pip install -U git+https://github.com/Rapptz/discord.py@rewrite
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
