import threading
import time

def take_orders():
    for i in range(1,4):
        print(f"Taking the order for {i}th method")