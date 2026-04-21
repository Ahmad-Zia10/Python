import asyncio
import time 
async def brew(name):
    print(f"Brewing {name} chai...")
    await  asyncio.sleep(2)
    # time.sleep(2)
    print(f"{name} chai is ready")

async def main():
    await asyncio.gather(
        brew("Masala"),
        brew("Ginger"),
        brew("Lemon")

    )

asyncio.run(main())
# We decalre three coroutines(brew("Masala"),brew("Ginger"),brew("Lemon"))) , 1st coroutine runs -> prints Brewing Masala chai...
# -> encounters await keyword -> await yields control back to event loop, asyncio.sleep(2) -> does not sit idle for these 2 secs it executes the next coroutine..so on