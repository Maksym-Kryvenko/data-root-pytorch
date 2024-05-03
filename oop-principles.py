class Item:
    # global values
    pay_rate = 0.8   # pay rate after 20% discount

    def __init__(self, name:str, price:float, quantity=0) -> None:
        # validate arguments
        assert price >= 0, f"Price {price} is not greater or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater or equal to zero!"

        # assign atributes
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def calculate_total_price(self) -> float:
        return self.price * self.quantity

    def __str__(self) -> str:
        return f"Item {self.name} has a total price of {self.calculate_total_price()}."

item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)

print(item1)
