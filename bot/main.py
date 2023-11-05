import os
from dotenv import load_dotenv
from bot_setup import bot
import hello

load_dotenv()


def main():
    @bot.event
    async def on_ready():
        print(f'Logged in as {bot.user}')

    bot.run(os.getenv("DISCORD_TOKEN"))


if __name__ == '__main__':
    main()
