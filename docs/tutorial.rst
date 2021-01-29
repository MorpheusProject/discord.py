

.. _tutorial:

Tutorial
=========

This tutorial covers the basics of creating your own discord bot using discord.py, 
touching on various library features.

Introduction
-------------------


Before You Start
^^^^^^^^^^^^^^^^^

Before making a discord bot using discord.py it is crucial you have a intermediate
understand of the fundamentals of the Python programming language.

Useful Resources for learning Python
"""""""""""""""""""""""""""""""""""""

- For complete beginners to programming `Automate the Boring Stuff with Python`__ useful resource for getting started.
__ https://automatetheboringstuff.com/
- `The Official Python Tutorial`__ covers everything you'll need to know more in-depth.
__ https://docs.python.org/3/tutorial/
- If you're already a competent programmer look at `Learn X in Y`__'s page on python3.
__ https://learnxinyminutes.com/docs/python3/



Creating a Discord Bot
-----------------------

Copy paste from :doc:`discord`


Installing discord.py
--------------------

discord.py works with Python 3.5.3 or higher.

Setup a Virtual Environment
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

With any python project, it's bast practice to create a virtual environment to allow 
for the installation of multiple package versions.

Python comes with the ``venv`` module which can be used to create local virtual environments.

For example on Windows:

.. code-block:: bash

    PS > py -m venv ./venv

Or on macOS/Unix:

.. code-block:: bash
    
    $ python3 -m venv ./venv

This will create a new virtual environment in the ``.venv`` directory.

We can then activate our new virtual environment with the following command.

On windows:

.. code-block:: bash

    PS > ./venv/Scripts/activate.bat

Or on macOS/Unix:

.. code-block:: bash

    $ source ./venv/bin/activate

Install discord.py
^^^^^^^^^^^^^^^^^^^^^

Once we've activated our environment we can install discord.py with ``pip``:

.. code-block:: bash

    $ pip install discord.py

This will install the latest version of discord.py into our virtual environment, 
we can validate this by running.

.. code-block:: bash

    $ python -m discord -v

Creating a project
--------------------


Making bot.py
^^^^^^^^^^^^^^^^^^^^


Importing the discord module
"""""""""""""""""""""""""""""

First we'll need to import the ``discord`` module, this contains the classes and functions 
we'll need to interface with the discord API.

.. code-block:: python3

    import discord


Creating a client
""""""""""""""""""

In order to interact with the discord API we'll need to create a client.

We can do this by creating an instance of the :class:`discord.Client`

.. code-block:: python3

    client = discord.Client()


On ready
""""""""""""""""""

Now we've made a client instance we need to make it do something. discord.py is an 
event driven library, meaning usually something would happen and the client would then 
perform an action in response.

we can use the :meth:`discord.Client.event` decorator to subscribe to a specific event. 
for example say we wanted to know when the bot had logged in to discord we could listen for the 
``on_ready`` event like so:

.. code-block:: python3

    @client.event
    async def on_ready():
        print('Logged in as {0}!'.format(client.user))

When our bot logs in to the Discord API it'll now print to the console.

Making config.py
^^^^^^^^^^^^^^^^^^^^

paste token
"""""""""""""""""""""""""

.. code-block:: python3

    TOKEN = "MjM4NDk0NzU2NTIxMzc3Nzky.CunGFQ.wUILz7z6HoJzVeq6pyHPmVgQgV4"


Testing the bot
^^^^^^^^^^^^^^^^^^^^^^

Using our token
""""""""""""""""

Now we've setup some code for out bot to run when it's logged in to the Discord API we'll 
need to actually login. To do this we'll need to pass our ``TOKEN`` to the ``client`` instance.

Firstly by importing the config file.

.. code-block:: python3

    import config

Then using the :meth:`discord.Client.run` method passing in our ``TOKEN``.

.. code-block:: python3

    client.run(config.TOKEN)

Starting the script
""""""""""""""""""""

now by running the script our bot should successfully connect to the Discord API.

.. code-block:: bash

    $ python bot.py

.. code-block:: text

    Logged in as DPyBot#3333!


Recap
^^^^^^^^^^^^^^^^^^

.. code-block:: python3

    import discord

    import config

    
    client = discord.Client()


    @client.event
    async def on_ready():
        print('Logged in as {0}!'.format(client.user))


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
        await ctx.send("Hello {0}!".format(member))


The fuck is a converter
""""""""""""""""""""""""""

.. code-block:: python3

    @bot.command()
    async def hello(ctx, *, member: discord.Member):
        """TODO"""
        await ctx.send("Hello {0}!".format(member.display_name))


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
