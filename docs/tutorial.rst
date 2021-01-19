.. currentmodule:: discord

.. _tutorial:

Tutorial
==========================


Intro
-------------------


Prereqs
^^^^^^^^^^^^^^^^^


tag lp
""""""""""""""


Creating a bot
-----------------------------


fuck is a token
^^^^^^^^^^^^^^^^^^^^^


Installing discord.py
--------------------


Setup a Virtual Environment
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    PS > py -m venv ./venv
    PS > ./venv/Scripts/activate

.. code-block:: bash
    
    $ python3 -m venv ./venv
    $ source ./venv/bin/activate


Install discord.py
^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    $ pip install discord.py


Creating a project
--------------------


Making bot.py
^^^^^^^^^^^^^^^^^^^^

import discord/commands
"""""""""""""""""""""""""

.. code-block:: python3

    import discord


subclass bot
"""""""""""""""""""""""""

.. code-block:: python3

    client = discord.Client()


On ready
'''''''''''''''''''''

.. code-block:: python3

    @client.event
    async def on_ready():
        print('Logged in as {0}!'.format(client))


Making config.py
^^^^^^^^^^^^^^^^^^^^

paste token
"""""""""""""""""""""""""

.. code-block:: python3

    TOKEN = "MjM4NDk0NzU2NTIxMzc3Nzky.CunGFQ.wUILz7z6HoJzVeq6pyHPmVgQgV4"


Testing the bot
^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python3

    import config


.. code-block:: python3

    client.run(config.TOKEN)



Recap
^^^^^^^^^^^^^^^^^^

.. code-block:: python3

    import discord

    import config

    
    client = discord.Client()


    @client.event
    async def on_ready():
        print('Logged in as {0}!'.format(client))


    client.run(config.TOKEN)


More Event listeners
--------------------


On Message
^^^^^^^^^^^^

.. code-block:: python3

    
    @client.event
    async def on_message(message):
        ...



On Member Join
^^^^^^^^^^^^^^^^^


.. code-block:: python3

    @client.event
    async def on_member_join(member):
        ...


Intents
""""""""

.. code-block:: python3

    intents = discord.Intents.default()
    intents.members = True

    client = discord.Client(intents=intents)



Recap
^^^^^^


.. code-block:: python3

    import discord

    import config


    intents = discord.Intents.default()
    intents.members = True

    client = discord.Client(intents=Intents)


    @client.event
    async def on_ready():
        print('Logged in as {0}!'.format(client))


    @client.event
    async def on_message(message):
        ...

    
    @client.event
    async def on_member_join(member):
        ...


    client.run(config.TOKEN)


Creating commands
--------------------


.. code-block:: python3

    from discord.ext import commands


.. code-block:: python3

    bot = commands.Bot(command_prefix="!", intents=intents)


Ping command
^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python3

    import time

    ...

    @bot.command()
    async def ping(ctx):
        """Returns the bots ping in milliseconds."""
        start = perf_counter()
        await ctx.channel.trigger_typing()
        end = perf_counter()

        duration = (end - start) * 1000
        await ctx.send("Pong! Took `{0:.2f}ms`".format(duration))


On message fucked my beans
"""""""""""""""""""""""""""

.. code-block:: python3

    @bot.event
    async def on_message(message):
        await bot.process_commands(message)

        ...


Huzzah!


Recap
""""""

.. code-block:: python3

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
        ...

    
    @bot.event
    async def on_member_join(member):
        ...


    @bot.command()
    async def ping(ctx):
        """Returns the bots ping in milliseconds."""
        start = perf_counter()
        await ctx.channel.trigger_typing()
        end = perf_counter()

        duration = (end - start) * 1000
        await ctx.send("Pong! Took `{0:.2f}ms`".format(duration))


    bot.run(config.TOKEN)


Uptime command
^^^^^^^^^^^^^^^^^^^^^^


Botvar / instance var
""""""""""""""""""""""""

.. code-block:: python3

    @bot.event
    async def on_message(message):
        await bot.process_commands(message)

        ...


.. code-block:: python3

    import time

    ...

    @bot.command()
    async def ping(ctx):
        """Returns the bots ping in milliseconds."""
        start = time.perf_counter()
        await ctx.channel.trigger_typing()
        end = time.perf_counter()

        duration = (end - start) * 1000
        await ctx.send("Pong! Took `{0:.2f}ms`".format(duration))


Hello command
^^^^^^^^^^^^^^^^^^^^^^


What are arguments
"""""""""""""""""""""""

.. code-block:: python3

    @bot.command()
    async def hello(ctx, *, member):
        """TODO"""
        await ctx.send("Hello {0}!`".format(member))


The fuck is a converter
""""""""""""""""""""""""""

.. code-block:: python3

    @bot.command()
    async def hello(ctx, *, member: discord.Member):
        """TODO"""
        await ctx.send("Hello {0}!`".format(member.display_name))


Help command
^^^^^^^^^^^^^^^^^^^

TODO: Idk

The default help command
"""""""""""""""""""""""""""


DIY Help command
""""""""""""""""""""""


Ban command
^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python3

    @bot.command()
    async def ban(ctx, member: discord.Member, *, reason: str = None):
        """TODO"""
        await member.ban(reason = reason)


Checks
""""""""""""""""""""""

.. code-block:: python3

    @bot.command()
    @commands.has_permissions(ban_members=True)
    async def ban(ctx, member: discord.Member, *, reason: str = None):
        """TODO"""
        await member.ban(reason = reason)



Permissions
""""""""""""""""""""""

.. code-block:: python3

    @bot.command()
    @commands.has_permissions(ban_members=True)
    @commands.bot_has_permissions(ban_members=True)
    async def ban(ctx, member: discord.Member, *, reason: str = None):
        """TODO"""
        await member.ban(reason = reason)


wait_for confirmation
""""""""""""""""""""""

.. code-block:: python3

    import asyncio

    ...

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


TODO: The rest
------------------------------
