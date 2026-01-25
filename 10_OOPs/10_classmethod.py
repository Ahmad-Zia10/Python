class ChaiOrder:

    def __init__(self, tea_type, sweetness, size):
        self.tea_type = tea_type
        self.sweetness =sweetness
        self.size = size

    @classmethod
    def from_dict(cls, dict):
        return cls(
            dict["tea_type"],
            dict["sweetness"],
            dict["size"]
        )

    @classmethod
    def from_string(cls, string):
        tea_type, sweetness, size = string.split("-")
        return cls(
            tea_type,
            sweetness,
            size
        )    


class ChaiUtils():
    @staticmethod
    def is_size_available(size):
        return size in ['Small', 'Medium', 'Large']
    
print(ChaiUtils.is_size_available("Extra Large"))

order1 = ChaiOrder.from_dict({"tea_type" : "Masala", "sweetness" : "little sweet", "size" : "small"})
print(order1)

order2 = ChaiOrder.from_string("Ginger-normal sweet-large")
print(order2)

print(order1.__dict__) # __dict__ :  stores their attributes as a dictionary.It maps attribute names (strings) to their corresponding values.
print(order2.__dict__)

order3 = ChaiOrder("Lemon", "moderately sweet", "Medium")
print(order3.__dict__)