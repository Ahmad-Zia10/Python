import os
print(os.getcwd())
# file = open("lesson.txt", "w")

# try:
#     file.write("Learning exception handling")
# finally:
#     file.close()

with open("order.txt", "w") as file:
    file.write("Ginger Chai - 2 cups")