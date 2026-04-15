class  ChaiUtils:

    @staticmethod
    def clean_ingredients(text):
        return [item.strip() for item in text.split(",")]

raw = "water , milk, ginger, honey"    
print(ChaiUtils.clean_ingredients(raw))

obj = ChaiUtils()
# print(obj.clean_ingredients(raw)) #ChaiUtils.clean_ingredients() takes 1 positional argument but 2 were given(when we did not use @staticmethod)
print(ChaiUtils.clean_ingredients(raw))
print(obj.clean_ingredients(raw))


# Static methods are used when:
# The function is conceptually related to the class
# But it does not represent a behavior of an object


#with @staticmethod, self is just a normal parameter name
# There is no magic in the word self.
# What makes self special is how the function is defined and accessed — not the name.
# Because of @staticmethod:
# Python does NOT automatically pass the instance.
# The method behaves like a plain function with two parameters: (self, text).