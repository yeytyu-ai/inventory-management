class InventoryError(Exception):
    """Base exception for inventory errors."""
    pass


class ProductNotFoundError(InventoryError):
    """Raised when a product is not found."""
    pass


class InvalidQuantityError(InventoryError):
    """Raised when an invalid quantity is provided."""
    pass


class DuplicateProductError(InventoryError):
    """Raised when a product already exists."""
    pass
