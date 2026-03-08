def __init__(self, name: str, description: str, price: float, quantity: int):
    self.name = name
    self.description = description
    self.price = float(price)
    self.quantity = int(quantity)


def __repr__(self):
    return f"Product(name={self.name!r}, price={self.price}, quantity={self.quantity})"
