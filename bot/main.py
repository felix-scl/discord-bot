import os
from dotenv import load_dotenv

from bot.hello import client

load_dotenv()


if __name__ == '__main__':
    client.run(os.getenv("DISCORD_TOKEN"))

