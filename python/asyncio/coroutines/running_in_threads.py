######################
# Running in Threads #
######################
# index: 6

# Running in Threads
#   coroutine asyncio.to_thread(func, /, *args, **kwargs)
# Asynchronously run function func in a separate thread.
# Any args, kwargs supplied to this function are directly passed to func.
# Also the current contextvars.Context is propagated, allowing context
# variables from the event loop thread to be accessed in the separate thread.
# Returns a coroutine that can be awaited to get the eventual result of func.
# This coroutine function is primarily intended to be used for executing
# IO-bound functions/methods that otherwise will block the event loop
# if they where ran in the main thread.

# Directly calling the blocking_io() in any coroutine would block
# the event loop for its duration, resulting in an additional 1 second
# of run time. Instead by using asyncio.to_thread(), we can run it
# in a separate thread without blocking the event loop.

import asyncio
import time


def blocking_io():
    print(f"start blocking_io at {time.strftime('%X')}")
    # Note that time.sleep() can be replaced with any blocking
    # IO-bound operation, such as file operations.
    time.sleep(1)
    # await asyncio.sleep(1)
    print(f"blocking_io complete at {time.strftime('%X')}")


async def main():
    print(f"started main at {time.strftime('%X')}")

    # blocking_io()
    await asyncio.gather(
        asyncio.to_thread(blocking_io),
        asyncio.sleep(1),
    )

    print(f"finished main at {time.strftime('%X')}")


if __name__ == "__main__":
    asyncio.run(main())
