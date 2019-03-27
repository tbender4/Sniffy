Sniffy is a Discord bot that prints lever information on demand.

## Requirements:
- Python 3.7
- discord.py **rewrite branch**
- A valid authorization token as string variable in `auth.py`

## Installation

```
pip install -U git+https://github.com/Rapptz/discord.py@rewrite
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
