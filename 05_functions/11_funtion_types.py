def pure_chai(cups):
    return cups*10

total_chai = 0

def impure_chai(cups):
    global total_chai
    total_chai += cups

def pour_chai(n):
    print(n)
    if n == 0:
        return "Chai Finished!"
    return pour_chai(n-1)

print(pour_chai(3))

# Lambda Function 

chai_types = ['Lemon', 'Ginger', 'Kadak', 'Masala', 'Ginger']

filtered_types = list(filter(lambda chai: chai!='Ginger', chai_types))
print(f"Filtered Chai types : {filtered_types}")