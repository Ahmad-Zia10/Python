def brew_chai(flavor):
    if flavor not in ["masala", "ginger", "lemon"]:
        raise ValueError("Flavor not in our menu.")
    print(f"Brewing {flavor} chai...")

brew_chai("mint")