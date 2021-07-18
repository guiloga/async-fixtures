########################
# Coroutines and Tasks #
########################
# index: 3

# We say that an object is an awaitable
# if it can be used with a await expression.
# Many asyncio APIs are designed to accept await awaitables.

# There are three main types of awaitable objects:
#   Coroutines, Tasks and Futures.

# Coroutines:
# Python coroutines are awaitables and therefore can be await from
# another coroutines.
# The term "coroutine" can be used for two closely related concepts:
#   - a coroutine function: an async def function.
#   - a coroutine object: an object returned by a coroutine function.

# Tasks:
# Tasks are used to schedule coroutines concurrently.
# When a coroutine is wrapped into a Task with functions
# like asyncio.create_task(), the coroutine is automatically
# scheduled to run soon.

# Futures:
# A Future is a special low-level awaitable object that represents
# an eventual result of an asynchronous operation.
# When a Future object is awaited, it means that the coroutine
# will wait until the Future is resolved in some other place.
# Future objects in asyncio are needed to allow callback-based code
# to be used with async/await syntax.
# Normally there is no need to create Future objects
# at the application level code.

import asyncio
import argparse
import functools
import sys

parser = argparse.ArgumentParser(
    description="Run the awaitables fixture specifying a different "
    "kind of an awaitable object: (coroutine, task, future)"
)
parser.add_argument(
    "kind", type=str, help="The awaitable object: (coroutine, task, future)"
)


async def nested():
    return 42


async def run_coroutine():
    # Nothing happens if we just call "nested()".
    # A coroutine object is created but not awaited,
    # so it *won't run at all*.
    coro = nested()
    print(coro)

    # Let's do it differently now and await it:
    print(await nested())


# Tasks
async def run_task():
    # Schedule nested() to run soon concurrently with main().
    task = asyncio.create_task(nested())

    # "task" can now be used to cancel "nested()" or can simply be
    # awaited to wait until it is complete:
    print(await task)


# Futures
# This example creates a Future object, creates and schedules
# an asynchronous Task to set result for the Future and waits
# until the Future has a result.


async def set_after(fut, delay, value):
    # Sleep for *delay* seconds
    await asyncio.sleep(delay)

    # Set *value* as a result of *fut* Future
    fut.set_result(value)


async def run_future():
    # Get the current event loop
    loop = asyncio.get_running_loop()

    # Create a new Future object
    fut = loop.create_future()

    # Adding a Callback: call 'print("Future:", fut)' when "fut" is done.
    fut.add_done_callback(functools.partial(print, "Future is done:"))

    # Run "set_after()" coroutine in a parallel Task.
    # We are using the low-level "loop.create_task()" API here because
    # we already have a reference to the event loop at hand.
    # Otherwise we could have just used "asyncio.create_task()".
    loop.create_task(set_after(fut, 1, "... world"))

    print("hello ...")

    # Wait until *fut* has a result and print it
    print(await fut)


async def main(kind: str):
    awaitable = getattr(sys.modules[__name__], f"run_{kind}")
    await awaitable()


if __name__ == "__main__":
    args = parser.parse_args()
    asyncio.run(main(args.kind))
