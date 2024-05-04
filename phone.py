from item import Item 

class Phone(Item):
    def __init__(self, name: str, price: float, quantity=0, broken_phones=0) -> None:
        # validate arguments
        assert broken_phones >= 0, f"Broken phones {broken_phones} is not greater or equal to zero!"

        # initialize an instance
        super().__init__(name, price, quantity)
        
        # assign attributes
        self.broken_phones = broken_phones
