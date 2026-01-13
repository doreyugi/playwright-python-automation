from dataclasses import dataclass

@dataclass
class Product:
    name: str
    price: int
    quantity: int = 1
    
    def update_quantity(self, quantity: int):
        self.quantity = quantity
