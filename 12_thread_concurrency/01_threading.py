import threading
import time

def take_orders():
    for i in range(1,4):
        print(f"Taking the {i}th order")
        time.sleep(2)

def brew_chai():
    for i in range(1,4):
        print(f"Brewing {i}th chai")
        # time.sleep(3) if it's not there, then after starting thread calls order_chai() -> prints -> encounters time.sleep() -> switches to this thread and completely executes this since there is no time.sleep() here. i.e. brewing chai for ,1,2,3 is printed and then the OS switches to the the order_chai_thread
        time.sleep(3)


#create threads 
order_chai_thread = threading.Thread(target=take_orders) # create a thread and assign it which task to run
brew_chai_thread = threading.Thread(target=brew_chai) 

#start thread
order_chai_thread.start() # now the thread starts executing. Runs the task, i.e. the order_chai() function -> prints the statement -> encounters time.sleep() -> this is key, the thread is executing and it encounters a delay time, so the OS quickly switches to the other threads being run.
brew_chai_thread.start() 

# wait for both to finish .Don't move forward until both workers are done. Do not exit before they both are done. 
order_chai_thread.join()
brew_chai_thread.join()
