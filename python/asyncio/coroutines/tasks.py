########################
# Coroutines and Tasks #
########################
# index: 2

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
    task1 = asyncio.create_task(say_after(1, "hello"))

    task2 = asyncio.create_task(say_after(2, "world"))

    print(f"started at {time.strftime('%X')}")

    # Wait until both tasks are completed, should take around 2 seconds.
    await task1
    await task2

    print(f"finished at time {time.strftime('%X')}")


if __name__ == "__main__":
    asyncio.run(main())

    # Note that the code runs 1 second, faster than the await.py fixture.
