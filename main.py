import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

offers = [
    {
        "shop": "Boots",
        "offer": "Example Boots reward",
        "status": "Check availability"
    },
    {
        "shop": "Superdrug",
        "offer": "Example Superdrug reward",
        "status": "Check availability"
    }
]

@bot.command()
async def offers_list(ctx):
    message = "**Retail Rewards Available**\n"
    for item in offers:
        message += f"\n**{item['shop']}**\n{item['offer']}\nStatus: {item['status']}\n"
    await ctx.send(message)

@bot.event
async def on_ready():
    print(f"Bot online as {bot.user}")

bot.run(os.getenv("DISCORD_TOKEN"))
