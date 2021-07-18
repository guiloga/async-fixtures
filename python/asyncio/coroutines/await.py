########################
# Coroutines and Tasks #
########################
# index: 1

# To actually run a coroutine, asyncio provided three main mechanisms.
#   asyncio.run()
#   await on a coroutine
#   asyncio.create_task()

import asyncio
import time


async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)


async def main():
    """prints 'hello' after waiting for 1 second, and then prints 'world'
            after waiting for 2 seconds.
    """
    print(f"started at {time.strftime('%X')}")

    await say_after(1, "hello")
    await say_after(2, "world")

    print(f"finished at time {time.strftime('%X')}")


if __name__ == "__main__":
    asyncio.run(main())
