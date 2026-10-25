# ByteBites core domain model (see bytebites_design.md)
#
# Customer  - a user: name + purchase_history (past Orders); can be verified.
# FoodItem  - something we sell: name, price, category, popularity_rating.
# Menu      - the full collection of FoodItems; filter by category, sort.
# Order     - one transaction: the selected FoodItems and their total cost.


class FoodItem:
    """One sellable item, e.g. a 'Spicy Burger' or 'Large Soda'."""

    def __init__(self, name, price, category, popularity_rating):
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


class Order:
    """A single transaction: the items a user selected."""

    def __init__(self):
        self.items = []


class Customer:
    """A user of the app, with a record of past purchases."""

    def __init__(self, name):
        self.name = name
        self.purchase_history = []
