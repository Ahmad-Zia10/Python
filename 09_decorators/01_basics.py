from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper():
        print("Before function runs")
        func()
        print("After Funciton runs")
    return wrapper

@my_decorator
def greet():
    print("Hello from decorators class from chaicode!!")

greet()
print(greet.__name__) #without using @wraps(func), it prints wrapper. to avoid use the @

