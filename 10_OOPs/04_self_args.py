class Chai_cup:
    size = 150

    def describe(self):
        return f"A {self.size}ml chai cup."

cup = Chai_cup()
print(cup.describe())
# print(Chai_cup.describe()) #Error : Chai_cup.describe() missing 1 required positional argument: 'self'

cup_two  = Chai_cup()
cup_two.size = 100
print(cup_two.describe())
print(Chai_cup.describe(cup))