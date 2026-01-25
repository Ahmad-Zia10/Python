favourite_pizzas = [
    "Deep Dish Pizza",
    "Neopolitan Pizza",
    "Thin Crust Pizza",
    "Cheese Burst Pizza",
    "Neopolitan Pizza",
    "Fried Pizza"
]


# Task 1 : Find unique pizzas in favourite pizzas
unique_pizza = {pizza for pizza in favourite_pizzas }
print(unique_pizza)

italian_pizzas = {pizza for pizza in favourite_pizzas if "Neopolitan" in pizza or "Fried" in pizza}
print(italian_pizzas)

recipes = {
    "Deep Dish Pizza" : ["Sour Dough", "Cheeze", "Marinara Sauce", "Cheddar Cheeze"],
    "Neopolitan Pizza" : ["Sour Dough", "Marinara Sauce","Burrata"],
    "Cheese Burst Pizza" : ["Sour Dough", "Marinara Sauce", "Liquid Cheeze"]
}

# Get unique ingredients from recipes
unique_ingredients = {item for ingredients in recipes.values() for item in ingredients}
print(unique_ingredients)

