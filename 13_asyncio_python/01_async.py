import asyncio

async def brew_chai():
    print("Brewing Chai...")
    await asyncio.sleep(2)
    print("Chai is ready")

asyncio.run(brew_chai())


# time.sleep() IS blocking — for that thread
# When a thread hits time.sleep(2), that thread is completely frozen for 2 seconds. It can't do anything else. The OS just says "this thread is sleeping, I'll wake it up later".
# The reason the other thread still runs is simply because — they are separate threads. The OS schedules them independently. One sleeping doesn't affect the other.
# Thread 1: [order1]--[SLEEPING 2s]--[order2]--[SLEEPING 2s]--[order3]
# Thread 2: [chai1]---[SLEEPING 2s]--[chai2]---[SLEEPING 2s]--[chai3]
#               ↑
#          Both sleeping at the same time is fine,
#          because they are INDEPENDENT threads

# Now contrast with AsyncIO — Single Thread
# There is only ONE thread. If that thread hits time.sleep(2):
# Single Thread: [brew chai]--[SLEEPING 2s, ENTIRE PROGRAM FROZEN]--[wakes up]
# Nothing else can run. The whole program is stuck. That's why asyncio uses await asyncio.sleep() instead — it pauses that coroutine but frees the thread to go run another coroutine.