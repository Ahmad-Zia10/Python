def updated_order():
    chai_type = "Lemon"
    def kitchen():
        nonlocal chai_type
        chai_type = "Kesar"
    kitchen()
    print(f"Chai type : {chai_type}")

updated_order()