import threading
import time

def brew_Chai():
    print(f"{threading.current_thread().name} started brewing...")
    count = 0
    for _ in range(100_000_000):
        count += 1
    print(f"{threading.current_thread().name} finished brewing.")

thread1  = threading.Thread(target=brew_Chai, name="Barista-1")
thread2 = threading.Thread(target=brew_Chai, name="Barista-2")

start = time.time()
thread1.start()
thread2.start()
thread1.join()
thread2.join()
end = time.time()

print(f"total time taken: {end -start:.2f} seconds")


# How this maps to the GIL
# The GIL (Global Interpreter Lock) is a mutex that allows only one thread to execute Python bytecode at a time, even on a multi-core machine.
# Here's what's actually happening under the hood:
# Thread 1: [runs ~100 bytecodes] → releases GIL → [waits] → [gets GIL again] → ...
# Thread 2: [waits for GIL]       → gets GIL    → [runs]  → releases GIL     → ...
# Python's interpreter itself enforces this — every ~100 bytecode instructions (or every 5ms in Python 3.2+), the current thread is forced to release the GIL and let others compete for it. This is called the "check interval".