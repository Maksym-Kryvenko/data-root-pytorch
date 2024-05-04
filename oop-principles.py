from item import Item
from phone import Phone

phone1 = Phone("jscPhoneV10", 500, 5)
phone1.calculate_total_price()
phone2 = Phone("jscPhoneV20", 700, 5)

print(phone1.name)

phone1.name = "jscPhoneV30"

print(phone1.name)
