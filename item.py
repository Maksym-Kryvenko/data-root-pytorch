import csv

class Item:
    # global values
    pay_rate = 0.8   # pay rate after 20% discount
    all = []

    def __init__(self, name:str, price:float, quantity=0) -> None:
        # validate arguments
        assert price >= 0, f"Price {price} is not greater or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater or equal to zero!"

        # assign attributes
        self.__name = name  # single underscore indicates that atribute is read-only, double - makes it private, can't be called from the outside
        self.__price = price
        self.quantity = quantity

        # actions to execute
        Item.all.append(self)
    
    # -------- SATISFY ENCAPSULATION PRINCIPLE -------- #
    @property
    # property decorator = read-only attribute
    def name(self):
        return self.__name
    
    @property
    def price(self):
        return self.__price

    @name.setter
    # allow to change read-only attributes
    def name(self, value):
        if len(value) > 15:
            raise Exception("The name is too long!")
        else:
            self.__name = value
    # ------------------------------------------------- #

    # --------------- CLASS METHODS ------------------- #
    def calculate_total_price(self) -> float:
        return self.__price * self.quantity
    
    def apply_discount(self) -> None:
        self.__price = self.__price * self.pay_rate

    def apply_increment(self, increment_value) -> None:
        self.__price = self.__price * (1 + increment_value)
    # ------------------------------------------------- #

    # in case of using print for instance
    def __str__(self) -> str:
        return f"Item {self.name} has a total price of {self.calculate_total_price()}."

    # instead of hash number of instance it returns a particular form
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.name}', {self.__price}, {self.quantity}')"

    # pick up data from csv to create class instances
    @classmethod
    def instantiate_from_csv(cls):
        with open('input_data/items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        
        for item in items:
            Item(
                name=item.get('item'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity')))
    
    # it will count out the floats that are point zero (i.e. 5.0, 10.0)
    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            # print("01")
            # count out the floats that are point zero
            return num.is_integer()
        elif isinstance(num, int):
            # print("02")
            return True
        else:
            # prin t("03")
            return False
    
    # --------------- SATISFY ABSTRACTION PRINCIPLE ---------------------- #
    # make these methods PRIVATE with double underscore
    def __connect(self, smtp_server):
        pass

    def __prepare_body(self):
        return f"""
        Hello someone.
        We have {self.name} {self.quantity} times.
        Regards, Owner Name.
        """
    
    def __send(self):
        pass

    def send_email(self):
        self.__connect()
        self.__prepare_body()
        self.__send()
    # -------------------------------------------------------------------- #
