import logging
import os

import discord
from discord.ext import commands

from utils import spoilers

# Define all variables to be used around the script
description = '''Un bot todo loco 24/7'''
bot = commands.Bot(command_prefix='--', description=description)

# Setup basic logging for the bot
logging.basicConfig(level=logging.WARNING)


@bot.event
async def on_ready():
    print('Bot is ready for use')


@bot.command(pass_context=True)
async def spoiler(context, title, text):
    """Creates an spoiler as a pastebin."""
    await bot.delete_message(context.message)
    spoiler_url = spoilers.create(text)

    em = discord.Embed(title=':warning: SPOILER: {0}'.format(title), description=spoiler_url, colour=0xEA0000)

    await bot.send_message(
        context.message.channel,
        embed=em
    )

if __name__ == '__main__':
    bot.run(os.environ['APP_TOKEN'])

