import asyncio
import time

import discord
from discord.ext import commands

import config


intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print('Logged in as {0}!'.format(bot))


@bot.event
async def on_message(message):
    await bot.process_commands(message)
    ...  # TODO


@bot.event
async def on_member_join(member):
    ...  # TODO


@bot.command()
async def ping(ctx):
    """Returns the bots ping in milliseconds."""
    start = time.perf_counter()
    await ctx.channel.trigger_typing()
    end = time.perf_counter()

    duration = (end - start) * 1000
    await ctx.send("Pong! Took `{0:.2f}ms`".format(duration))


@bot.command()
async def hello(ctx, *, member: discord.Member):
    """TODO"""
    await ctx.send("Hello {0}!`".format(member.display_name))


@bot.command()
@commands.has_permissions(ban_members=True)
@commands.bot_has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason: str = None):
    """TODO"""
    reactions = ('👍', '👎')

    message = await ctx.send('Are you sure you want to ban {0}?'.format(member))
    for reaction in reactions:
        await message.add_reaction(reaction)

    def check(reaction, user):
        return reaction.message == message and user == ctx.message.author and str(reaction.emoji) in reactions

    try:
        reaction = await bot.wait_for('reaction_add', timeout=60, check=check)
    except asyncio.TimeoutError:
        return
    finally:
        await message.delete()

    if str(reaction.emoji) == '👍':
        await member.ban(reason = reason)


bot.run(config.TOKEN)
