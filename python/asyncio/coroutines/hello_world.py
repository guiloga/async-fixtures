########################
# Coroutines and Tasks #
########################
# index: 0

# Coroutines declared with the async/await syntax are the preferred way of
# writing asyncio applications.

import asyncio


async def main():
    """prints 'hello', waits 1 second and then print 'world'"""
    print("hello")
    await asyncio.sleep(1)
    print("world")


if __name__ == "__main__":
    asyncio.run(main())

    # note that simply calling a coroutine will not schedule it to be executed
    print(main())
