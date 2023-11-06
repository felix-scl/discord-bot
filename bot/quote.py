import os
import requests
from bot_setup import bot
from dotenv import load_dotenv

load_dotenv()


def get_quote():
    data = requests.get('https://dummyjson.com/quotes/random')
    return data.json()["quote"]


@bot.slash_command(description="Generate a random quote")
async def quote(ctx):
    channel_id = int(os.getenv("QUOTES_CHANNEL_ID"))
    if ctx.channel.id == channel_id:

        await ctx.respond(get_quote())
    else:
        channel_name = bot.get_channel(channel_id)
        await ctx.respond(f'This command is only available on {channel_name.mention}')
