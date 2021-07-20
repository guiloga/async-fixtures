########################
# Coroutines and Tasks #
########################
# index: 2

# To actually run a coroutine, asyncio provided three main mechanisms.
#   asyncio.run()
#   await on a coroutine
#   asyncio.create_task()

# Running Tasks concurrently:
# awaitable asyncio.gather(*aws, loop=None, return_exceptions=False)

# Runs awaitable objects in the *aws sequence concurrently.
# If any awaitable in aws is a coroutine it is automatically
# scheduled as a Task.
# If all awaitables are completed successfully, the result
# is an aggregate list of returned values. The order
# of result values corresponds to the order of awaitables in awa.
# If 'return_exceptions' is False (default), the first raised
# exception is propagated to the task that awaits on gather().
# Other awaitables in the aws sequence won't be cancelled and
# will continue to run.
# If 'return_exceptions' is True, exceptions are threaded as
# same as successful results, and aggregated in the results list.
# If gather() is cancelled, all submitted awaitables thar are not
# completed yet are also cancelled.
# If any Task or Future from the aws sequence is cancelled,
# it is threated as if it raised CancelledError - the gather()
# call it is not cancelled in this case.
# This is to prevent the cancellation of one submitted Task/Future
# to cause other Task/Future to be cancelled.


import asyncio
import time


async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)


async def factorial(name, number):
    f = 1
    for i in range(2, number + 1):
        print(
            f"Task {name}: Compute factorial({number}), currently i={i}...")
        await asyncio.sleep(1)
        f *= i
    print(f"Task {name}: factorial({number}) = {f}")
    return f


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

    # Schedule three calls concurrently
    L = await asyncio.gather(
        factorial("A", 2),
        factorial("B", 3),
        factorial("C", 4),
    )
    print(L)


if __name__ == "__main__":
    asyncio.run(main())

    # Note that the code runs 1 second, faster than the await.py fixture.
