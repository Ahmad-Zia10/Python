from functools import wraps

def log_activity(func):
    @wraps(func)
    def wrapper(*args, **kwargs): 
        print(f"🚀 Calling: {func.__name__}")
        result = func(*args, **kwargs)
        # func(*args, **kwargs)   # calls func(1, 2, x=3)
        # func(args, kwargs)      # calls func((1, 2), {'x': 3})
        print(f"✅ Finished: {func.__name__}")
        return result
    return wrapper

@log_activity
def brew_chai(type):
    print(f"Brewing chai {type}.")

# The above code from @log_activity i translates to this code below:
# def brew_chai(type):
#     print(f"Brewing chai {type}.")

# brew_chai = log_activity(brew_chai)

# So brew_chai no longer is the original function — it’s whatever log_activity returns. In your code, log_activity returns wrapper
#brew_chai → refers to wrapper (a function defined inside log_activity)
#The original function is available inside that closure as func.

brew_chai("Masala")