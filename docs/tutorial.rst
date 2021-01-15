.. currentmodule:: discord

.. _tutorial:

Tutorial
==========================


Prerequisites
--------------------------

todo:

.. _creating-a-discord-bot:

Creating a Discord bot
--------------------------

go to discord dot com etc


Installing discord.py
--------------------------

.. code-block:: bash

    pip install discord.py

n.b. maybe talk about [voice]


Creating a project
--------------------------

.. code-block:: bash
    
    python -m discord newbot .


Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^

The ``config.py`` file should be used to store the bots configuration.

yada yada yada

Copy the ``token`` :ref:`provided by discord <creating-a-discord-bot>` into the ``token`` variable.


Testing the Bot
^^^^^^^^^^^^^^^^^^^^^^^^^^


Event Listeners
--------------------------

todo: Should this be below commands?


Error Handling
^^^^^^^^^^^^^^^^^^^^^^^^^^

todo:


Commands
--------------------------

todo:


Introduction to commands
^^^^^^^^^^^^^^^^^^^^^^^^^^

todo:


Creating a command
^^^^^^^^^^^^^^^^^^^^^^^^^^

todo:


A basic ping command
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python3

    from time import perf_counter

    ...

    @bot.command()
    async def ping(ctx):
        """Returns the bots ping in milliseconds."""
        start = perf_counter()
        await ctx.channel.trigger_typing()
        end = perf_counter()

        duration = (end - start) * 1000
        await ctx.send("Pong! Took `{0:.2f}ms`".format(duration))


Converters
^^^^^^^^^^^^^^^^^^^^^^^^^^

todo:


Checks
^^^^^^^^^^^^^^^^^^^^^^^^^^

todo:


Error Handling
^^^^^^^^^^^^^^^^^^^^^^^^^^

todo:


Extensions
--------------------------

todo: 


Cogs
--------------------------

todo:

.. code-block:: bash

    python -m discord newcog my_cog


Other cog stuff? checks?
^^^^^^^^^^^^^^^^^^^^^^^^^^

todo:


Tasks
--------------------------

todo: 
