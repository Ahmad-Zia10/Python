import asyncio
import time
from  concurrent.futures import ThreadPoolExecutor

def check_stock(item):
    print(f"Checking {item} stock in store....")
    time.sleep(2) # Blocking Operation
    print(f"{item} stock : 42")

async def main():
    loop = asyncio.get_running_loop()
    with ThreadPoolExecutor() as pool:
        result = await loop.run_in_executor(pool, check_stock, "Masala Chai")
        print(result)

asyncio.run(main())


# The Problem
# You're in asyncio (single thread). You need to call time.sleep() or requests.get() — blocking code you can't change.
# pythonasync def main():
#     time.sleep(2)  # FREEZES the entire event loop
# The event loop is stuck. Nothing else can run.

# What run_in_executor does
# It offloads that blocking call to a separate thread, so the event loop stays free.
# pythonasync def main():
#     loop = asyncio.get_running_loop()
#     await loop.run_in_executor(pool, time.sleep, 2)
#     # event loop is FREE during those 2 seconds

# Visually
# Without run_in_executor:
# Event Loop Thread:  [task1]--[FROZEN 2s]--[task2]
#                                ↑
#                           time.sleep() blocked everything
# With run_in_executor:
# Event Loop Thread:  [task1]--[free]--[free]--[task2]
#                                 ↑
# Worker Thread:              [time.sleep 2s running here]
# The blocking code is pushed to a worker thread, and the event loop thread gets a simple await — meaning it can go do other coroutines while the worker thread handles the blocking work.

# Simple one line summary

# run_in_executor = "run this blocking function in a thread, but let me await its result like it's async"

# It's a bridge between blocking code and async code.