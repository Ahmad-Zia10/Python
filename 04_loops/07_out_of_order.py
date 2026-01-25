items = ['Ginger', 'Out of Stock', 'Lemon', 'Discontinued', 'Pineapple']

for item in items:
    if item == 'Out of Stock':
        continue
    elif item == 'Discontinued':
        print("Discontinued Item Found!!")
        break
    print(f"Item : {item}")

print("Outside for Loop")