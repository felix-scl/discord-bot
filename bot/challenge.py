import json
import random
import os
from bot_setup import bot
from dotenv import load_dotenv
from utils.url_validation import url_validation
from utils.html_parse import get_h1_text

load_dotenv()
data_path = os.path.join(os.path.dirname(__file__), '.', 'data', 'challenges.json')


def get_random_challenge():
    with open(data_path, 'r') as file:
        data = json.load(file)
    random_challenge = random.choice(data['challenges'])
    return random_challenge['name'], random_challenge['url']


def get_all_challenges():
    with open(data_path, 'r') as file:
        data = json.load(file)
    return data['challenges']


def add_challenge_to_file(name, url):
    with open(data_path, 'r') as file:
        data = json.load(file)
    data['challenges'].append({'name': name, 'url': url})
    with open(data_path, 'w') as file:
        json.dump(data, file)


@bot.slash_command(description='Get a random challenge')
async def challenge(ctx):
    if ctx.channel.id == int(os.getenv('QUOTES_CHANNEL_ID')):
        await ctx.respond('This channel is only for quotes')
    else:
        name, url = get_random_challenge()
        await ctx.respond(f'{name} {url}')


@bot.slash_command(description='Get all challenges')
async def challenges_list(ctx):
    if ctx.channel.id == int(os.getenv('QUOTES_CHANNEL_ID')):
        await ctx.respond('This channel is only for quotes')
    else:
        challenges = get_all_challenges()
        response = ''
        for item in challenges:
            response += f'{item["name"]} {item["url"]}\n'
        await ctx.respond(response)


@bot.slash_command(description='Add a challenge')
async def add_challenge(ctx, challenge_url):
    if ctx.channel.id == int(os.getenv('QUOTES_CHANNEL_ID')):
        await ctx.respond('This channel is only for quotes')
    else:
        if url_validation(challenge_url, 'https', 'codingchallenges.fyi'):
            challenge_name = get_h1_text(challenge_url)
            add_challenge_to_file(challenge_name, challenge_url)
            await ctx.respond(f'Added: {challenge_name} {challenge_url}')
        else:
            await ctx.respond(f'Unable to add: {challenge_url} please check it is a valid Coding Challenge')
