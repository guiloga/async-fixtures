########################
# Coroutines and Tasks #
########################
# index: 4

# Shield from cancellation:
# awaitable asyncio.shield(aw, *, loop=None)

# Protect an awaitable object from being cancelled.
# If aw is a coroutine it is automatically scheduled as a Task,
# The statement:
#   res = await shield(something())
# is equivalent to:
#   res = await something()
# except that if the coroutine containing it is cancelled,
# the Task running in something() is not cancelled.
# From the point of view of something(), the cancellation
# did not happen. Although its caller is still cancelled,
# so the wait expression still raises a
# If something is cancelled by other means
# (i.e from within itself) that would also cancel shield().
# It is desired completely to ignore cancellation
# (not recommended) the shield function should be
# combined with a try/except clause, as follows.
#   try:
#       res = await shield(something())
#   except CancelledError:
#       res = None

# Timeouts:
# coroutine asyncio.wait_for(aw, timeout, *, loop=None)

# This function wait the aw to complete with a timeout.
# If the aw is a coroutine it automatically schedules
# a Task. The 'timeout' can be either None, a float
# or int number of seconds to wait for. It timeout
# is None, it blocks until the Future completes.
# If a timeout occurs it cancels the Task and raises
# asyncio.TimeoutError.
# To avoid the task cancellation wrap it in 'shield(aw)'.
# The function will wait until the future is actually
# cancelled, to the total wait time may exceed the timeout
# time. If an exception happens during cancellation
# it is propagated.
# If the wait is cancelled, the Future aw is also cancelled.


import asyncio


async def eternity():
    # Sleep for 1 hour
    await asyncio.sleep(3600)
    print("yay!")


async def main():
    # Wait for at most 1 second
    try:
        await asyncio.wait_for(eternity(), timeout=1.0)
    except asyncio.TimeoutError:
        print("timeout!")


if __name__ == "__main__":
    asyncio.run(main())
