chai_type = "Ginger"

def kitchen():
    # nonlocal chai_type - Gives error :No binding for nonlocal "chai_type" foundPylance because there is no
    # outer function that has this chai_type variable
    # global chai_type
    chai_type = "Lemon"
    def counter2():
        global chai_type
        chai_type = "Elaichi"
    counter2()
    print(f"Kitchen Chai type: {chai_type}")


kitchen()
print(f"Chai Type Globally : {chai_type}")