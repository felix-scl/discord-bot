from bot_setup import bot


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send(f'Hello {message.author.name}')
