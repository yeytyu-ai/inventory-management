import unittest
from inventory import Inventory


class TestInventory(unittest.TestCase):

    def setUp(self):
        self.inventory = Inventory()

    def test_add_product(self):
        self.inventory.add_product("Laptop", 10, 50000)
        product = self.inventory.get_product("Laptop")

        self.assertEqual(product["quantity"], 10)
        self.assertEqual(product["price"], 50000)

    def test_remove_product(self):
        self.inventory.add_product("Mouse", 5, 500)
        self.inventory.remove_product("Mouse")

        self.assertIsNone(self.inventory.get_product("Mouse"))

    def test_update_quantity(self):
        self.inventory.add_product("Keyboard", 10, 1000)
        self.inventory.update_quantity("Keyboard", 20)

        product = self.inventory.get_product("Keyboard")
        self.assertEqual(product["quantity"], 20)


if __name__ == "__main__":
    unittest.main()
