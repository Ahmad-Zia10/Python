import asyncio
import threading
import time

def background_worker():
    while True:
        time.sleep(1)
        print(f"Loggin in the system healt ⏰")

async def fetch_orders():
    await asyncio.sleep(3)
    print(f"🎁 order fetched")

threading.Thread(target=background_worker, daemon=True).start()

asyncio.run(fetch_orders())

#A daemon thread means — "this thread should die when the main program exits".