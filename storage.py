import json
import csv
from inventory import Product


def save_to_json(products, filename="products.json"):
    data = [product.to_dict() for product in products]

    with open(filename, "w") as file:
        json.dump(data, file, indent=4)


def load_from_json(filename="products.json"):
    with open(filename, "r") as file:
        data = json.load(file)

    return [
        Product(
            item["product_id"],
            item["name"],
            item["quantity"],
            item["price"]
        )
        for item in data
    ]


def save_to_csv(products, filename="products.csv"):
    with open(filename, "w", newline="") as file:
        fieldnames = ["product_id", "name", "quantity", "price"]

        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for product in products:
            writer.writerow(product.to_dict())


def load_from_csv(filename="products.csv"):
    products = []

    with open(filename, "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            products.append(
                Product(
                    row["product_id"],
                    row["name"],
                    int(row["quantity"]),
                    float(row["price"])
                )
            )

    return products
