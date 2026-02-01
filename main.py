import os
import discord
from discord.ext import commands

token = os.getenv("DISCORD_TOKEN", "")

# sanitize token to prevent hidden newlines/spaces from clipboard/paste
token = token.replace("\r", "").replace("\n", "").strip()
if token.lower().startswith("bot "):
    token = token[4:].strip()

if not token:
    raise RuntimeError("DISCORD_TOKEN is missing in Railway Variables")

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

bot.run(token)
