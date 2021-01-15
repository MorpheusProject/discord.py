#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from time import perf_counter

from discord.ext import commands
import discord
import config

class Bot(commands.Bot):
    def __init__(self, **kwargs):
        super().__init__(command_prefix=commands.when_mentioned_or('$'), **kwargs)
        for cog in config.cogs:
            try:
                self.load_extension(cog)
            except Exception as exc:
                print('Could not load extension {0} due to {1.__class__.__name__}: {1}'.format(cog, exc))

    async def on_ready(self):
        print('Logged on as {0} (ID: {0.id})'.format(self.user))


bot = Bot()

@bot.command()
async def ping(ctx):
    """Returns the bots ping in milliseconds."""
    start = perf_counter()
    await ctx.channel.trigger_typing()
    end = perf_counter()

    duration = (end - start) * 1000
    await ctx.send("Pong! Took `{0:.2f}ms`".format(duration))

bot.run(config.token)
