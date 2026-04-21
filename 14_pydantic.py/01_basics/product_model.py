from pydantic import BaseModel

class Product(BaseModel):
    uid : int
    name : str
    price : float
    in_stock : bool = True #default value is true


product1 = Product(id=1, name = "Laptop", price= 999.99, in_stock=True)
product2 = Product(id=2, name="Mouse", price=24.33)

product3 = Product(name="Keyboard")