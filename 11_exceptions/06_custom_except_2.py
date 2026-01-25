class OutOfIngredientsError(Exception):
    pass

def make_chai(sugar, milk):
    if sugar == 0 or milk == 0:
        raise OutOfIngredientsError("Out of ingredients to make chai!")
    print("chai is ready...")


make_chai(0, 1)