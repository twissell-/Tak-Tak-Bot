import logging
import os
import sys
import traceback
import time

import discord
from discord.ext import commands

from utils import (
    command_prefix,
    spoilers,
    command_help
)

# Define all variables to be used around the script
description = '''Un bot todo loco 24/7'''
bot = commands.Bot(command_prefix=command_prefix, description=description)

# Setup basic logging for the bot
logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)


@bot.event
async def on_ready():
    logger.info('Bot is ready for use')


@bot.event
async def on_command_error(error, context):
    if hasattr(context.command, 'on_error'):
        return

    # get the original exception
    error = getattr(error, 'original', error)

    if isinstance(error, commands.CommandNotFound):
        return

    if isinstance(error, commands.MissingRequiredArgument):
        await bot.delete_message(context.message)

        await bot.send_message(
            context.message.channel,
            content=command_help.get(context.command)
        )

        return

    # ignore all other exception types, but print them to stderr
    logger.error('Ignoring exception in command {}:'.format(context.command))

    logger.error(type(error), error, error.__traceback__)


@bot.command(pass_context=True)
async def limpiar(context, number: int):
    """Clear a specified number of messages in the chat"""
    await bot.delete_message(context.message)

    deleted = await bot.purge_from(context.message.channel, limit=number)
    notification = await bot.send_message(context.message.channel, 'Borrados {} mensaje(s)'.format(len(deleted)))

    time.sleep(10)
    await bot.delete_message(notification)


@bot.command(pass_context=True)
async def spoiler(context, title, text):
    """Creates an spoiler as a pastebin."""
    await bot.delete_message(context.message)

    spoiler_url = spoilers.execute(text)

    em = discord.Embed(title=':warning: SPOILER: {0}'.format(title), description=spoiler_url, colour=0xEA0000)

    await bot.send_message(
        context.message.channel,
        embed=em
    )

if __name__ == '__main__':
    bot.run(os.environ['APP_TOKEN'])

