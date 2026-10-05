from exceptions import (
    ProductNotFoundError,
    InvalidQuantityError,
    DuplicateProductError
)


class Product:
    def __init__(self, product_id, name, quantity, price):
        if quantity < 0:
            raise InvalidQuantityError("Quantity cannot be negative.")

        if price < 0:
            raise ValueError("Price cannot be negative.")

        self.product_id = product_id
        self.name = name
        self.quantity = quantity
        self.price = price

    def add_stock(self, quantity):
        if quantity <= 0:
            raise InvalidQuantityError("Quantity must be greater than zero.")

        self.quantity += quantity

    def remove_stock(self, quantity):
        if quantity <= 0:
            raise InvalidQuantityError("Quantity must be greater than zero.")

        if quantity > self.quantity:
            raise InvalidQuantityError("Not enough stock available.")

        self.quantity -= quantity

    def to_dict(self):
        return {
            "product_id": self.product_id,
            "name": self.name,
            "quantity": self.quantity,
            "price": self.price
        }


class Inventory:
    def __init__(self):
        self.products = {}

    def add_product(self, product):
        if product.product_id in self.products:
            raise DuplicateProductError(
                f"Product {product.product_id} already exists."
            )

        self.products[product.product_id] = product

    def remove_product(self, product_id):
        if product_id not in self.products:
            raise ProductNotFoundError(
                f"Product {product_id} not found."
            )

        del self.products[product_id]

    def get_product(self, product_id):
        if product_id not in self.products:
            raise ProductNotFoundError(
                f"Product {product_id} not found."
            )

        return self.products[product_id]

    def list_products(self):
        return list(self.products.values())
