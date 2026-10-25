# ByteBites core domain model (see bytebites_design.md)
#
# Customer  - a user: name + purchase_history (past Orders); can be verified.
# FoodItem  - something we sell: name, price, category, popularity_rating.
# Menu      - the full collection of FoodItems; filter by category, sort.
# Order     - one transaction: the selected FoodItems and their total cost.


class FoodItem:
    """One sellable item, e.g. a 'Spicy Burger' or 'Large Soda'."""

    def __init__(self, name, price, category, popularity_rating):
        if not name.strip() or not category.strip():
            raise ValueError("FoodItem name and category cannot be blank")
        if price < 0:
            raise ValueError("FoodItem price cannot be negative")
        self.name = name
        self.price = price
        self.category = category
        self.popularity_rating = popularity_rating

    def __repr__(self):
        return (f"FoodItem(name={self.name!r}, price={self.price}, "
                f"category={self.category!r}, popularity_rating={self.popularity_rating})")


class Menu:
    """The full collection of FoodItems."""

    def __init__(self):
        self.items = []

    def add_item(self, item):
        """Add a FoodItem to the menu."""
        self.items.append(item)

    def filter_by_category(self, category):
        """Return items whose category matches, ignoring case and outer spaces."""
        wanted = category.strip().lower()
        return [item for item in self.items if item.category.strip().lower() == wanted]

    def sort_by_popularity(self):
        """Return a new list of items, most popular first (ties keep menu order)."""
        return sorted(self.items, key=lambda item: item.popularity_rating, reverse=True)


class Order:
    """A single transaction: the items a user selected."""

    def __init__(self):
        self.items = []

    def add_item(self, item):
        """Add a selected FoodItem to the order."""
        self.items.append(item)

    def calculate_total(self):
        """Return the total cost of all selected items (0 if the order is empty)."""
        return round(sum(item.price for item in self.items), 2)


class Customer:
    """A user of the app, with a record of past purchases."""

    def __init__(self, name):
        if not name.strip():
            raise ValueError("Customer name cannot be blank")
        self.name = name
        self.purchase_history = []

    def is_verified(self):
        """A customer counts as a real user if they have at least one past purchase."""
        return len(self.purchase_history) > 0


if __name__ == "__main__":
    # Manual scenario: add items, sort, filter, total.
    menu = Menu()
    for item in [
        FoodItem("Spicy Burger", 9.99, "Mains", 4.7),
        FoodItem("Large Soda", 2.50, "Drinks", 4.1),
        FoodItem("Brownie", 3.75, "Desserts", 4.9),
        FoodItem("Iced Tea", 2.25, "Drinks", 3.8),
    ]:
        menu.add_item(item)

    print("Drinks:", [i.name for i in menu.filter_by_category("drinks")])
    print("By popularity:", [i.name for i in menu.sort_by_popularity()])

    order = Order()
    order.add_item(menu.items[0])
    order.add_item(menu.items[1])
    print("Order total:", order.calculate_total())

    ada = Customer("Ada")
    print("Verified before purchase:", ada.is_verified())
    ada.purchase_history.append(order)
    print("Verified after purchase:", ada.is_verified())
