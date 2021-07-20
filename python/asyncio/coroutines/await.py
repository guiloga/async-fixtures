########################
# Coroutines and Tasks #
########################
# index: 1

# To actually run a coroutine, asyncio provided three main mechanisms.
#   asyncio.run()
#   await on a coroutine
#   asyncio.create_task()

# Running an asyncio Program:
# asyncio.run(coro, *, debug=False)
#
# This function runs the coroutine,
# taking care of managing the asyncio event loop
# finalizing asynchronous generators,
# and closing the thread pool.
# this function cannot be called when another
# asyncio function is running in the same thread.
# This function always creates a new event loop
# and closes it at the end.
# It should be used as a main entrypoint for asyncio
# programs, and should ideally only be called once.

# Creating Tasks
# asyncio.create_task(coro, *, name=None)

# This function wraps a coroutine into a Task
# and schedule its execution. Returns a Task object.
# If name is not None, it is set as the name
# of the task using Task.set_name().
# The Task is executed in the loop returned
# by get_running_loop(), a RuntimeError is raises
# if there is no running loop in current thread.



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
