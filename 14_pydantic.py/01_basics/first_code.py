from pydantic import BaseModel


# pydantic classes always inherit BaseModel
# we define how data will look like
class User(BaseModel):
    id : int
    name : str
    is_active : bool

input_data = {'id':101, 'name': "Ahmad", 'is_active':True}
# input_data = {'id':101, 'name': "Ahmad", 'is_active':25} // gives value 

user  = User(**input_data)
print(user)