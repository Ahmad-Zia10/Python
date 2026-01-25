from functools import wraps

def require_admin(func):
    @wraps(func)
    def wrapper(user_role):
        if(user_role != "admin"):
            print("Access Denied: admins only")
            return None #optional
        else:
            return func(user_role)
    return wrapper

@require_admin
def access_tea_inventory(role):
    print(f"Access Granted to Tea Inventory")

access_tea_inventory("User")
access_tea_inventory("admin")