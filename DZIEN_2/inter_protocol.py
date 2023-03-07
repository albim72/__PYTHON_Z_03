from typing import List,Protocol

class Item(Protocol):
    quantity:float
    price:float


class Product:
    def __init__(self,name:str,quantity:float,price:float):
        self.name = name
        self.quantity = quantity
        self.price = price

def calculate_total(items:List[Item]) -> float:
    return sum([item.quantity*item.price for item in items])

total = calculate_total(
    [
        Product('masło',3,5.78),
        Product('papryka',0.6,21.55),
        Product('Woda mineralna',6,1.89)
    ]
)

print(f"do zapłaty: {total} zł")

