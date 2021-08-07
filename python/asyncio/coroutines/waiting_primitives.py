########################
# Coroutines and Tasks #
########################
# index: 5

# Waiting Primitives
# coroutine asyncio.wait(
#   aws, *, loop=None, timeout=None, return_when=ALL_COMPLETED)

# Run awaitable objects in the aws iterable concurrently
# and block until the condition specified by `return_when`.
# Returns two sets of Tasks/Futures: (done, pending).
# Usage:
#   done, pending = await asyncio.wait(aws)
# note that this function does not raise asyncio.TimeoutError.
# Futures or Tasks that aren't done when the timeout occurs
# are simply returned in the second set.

#  asyncio.as_completed(aws, *, loop=None, timeout=None)¶
# Run awaitable objects in the aws iterable concurrently.
# Return an iterator of coroutines. Each coroutine returned can be awaited
# to get the earliest next result from the iterable of the remaining awaitables.


import asyncio


async def foo():
    # await asyncio.sleep(1.2)
    return 12


async def wait_coroutines():
    tasks = {asyncio.create_task(foo()) for _ in range(3)}
    done, pending = await asyncio.wait(tasks, timeout=1)

    for t in tasks:
        if t in done:
            # Everything worked as expected, the coro is done.
            print("Task %s is done" % t)
        if t in pending:
            # something failed
            print("Task %s is pending" % t)

    for p in pending:
        print("Awaiting task %s" % p)
        await p
        print("Awaited %s" % p)


async def complete_coroutines():
    tasks = {asyncio.create_task(foo()) for _ in range(3)}
    for coro in asyncio.as_completed(tasks, timeout=1):
        result = await coro
        print("Completed coro %s with result=%s" % (coro, result))


async def main():
    await wait_coroutines()
    await complete_coroutines()


if __name__ == "__main__":
    asyncio.run(main())
