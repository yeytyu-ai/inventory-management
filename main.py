from inventory import Inventory

def main():
    inventory = Inventory()

    while True:
        print("\n--- Inventory Management ---")
        print("1. Add Product")
        print("2. View Products")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            product_id = input("Product ID: ")
            name = input("Product Name: ")
            quantity = int(input("Quantity: "))
            price = float(input("Price: "))

            inventory.add_product(product_id, name, quantity, price)
            print("Product added successfully!")

        elif choice == "2":
            products = inventory.get_all_products()

            if not products:
                print("No products found.")
            else:
                for product in products:
                    print(product)

        elif choice == "3":
            print("Exiting...")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
