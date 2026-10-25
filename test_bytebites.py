import pytest

from models import Customer, FoodItem, Menu, Order


@pytest.fixture
def menu():
    m = Menu()
    m.add_item(FoodItem("Spicy Burger", 9.99, "Mains", 4.7))
    m.add_item(FoodItem("Large Soda", 2.50, "Drinks", 4.1))
    m.add_item(FoodItem("Brownie", 3.75, "Desserts", 4.9))
    m.add_item(FoodItem("Iced Tea", 2.25, "Drinks", 3.8))
    return m


# --- Order totals -----------------------------------------------------------

def test_calculate_total_with_multiple_items():
    # A $10 burger and a $5 soda should total $15.
    order = Order()
    order.add_item(FoodItem("Burger", 10.00, "Mains", 4.5))
    order.add_item(FoodItem("Soda", 5.00, "Drinks", 4.0))
    assert order.calculate_total() == 15.00


def test_order_total_is_zero_when_empty():
    # A transaction with nothing added costs 0, not an error.
    assert Order().calculate_total() == 0


def test_order_total_has_no_floating_point_noise():
    # 0.1 + 0.2 style float errors must not leak into a price.
    order = Order()
    order.add_item(FoodItem("A", 0.10, "Drinks", 3))
    order.add_item(FoodItem("B", 0.20, "Drinks", 3))
    assert order.calculate_total() == 0.30


def test_order_counts_duplicate_items_each_time():
    # Picking the same item twice charges for it twice.
    soda = FoodItem("Large Soda", 2.50, "Drinks", 4.1)
    order = Order()
    order.add_item(soda)
    order.add_item(soda)
    assert order.calculate_total() == 5.00


# --- Menu filtering ---------------------------------------------------------

def test_filter_by_category_returns_only_that_category(menu):
    names = [i.name for i in menu.filter_by_category("Drinks")]
    assert names == ["Large Soda", "Iced Tea"]


def test_filter_by_category_ignores_case(menu):
    assert len(menu.filter_by_category("dEsSeRtS")) == 1


def test_filter_by_unknown_category_returns_empty_list(menu):
    assert menu.filter_by_category("Soup") == []


def test_filter_does_not_change_the_menu(menu):
    menu.filter_by_category("Drinks")
    assert len(menu.items) == 4


# --- Menu sorting -----------------------------------------------------------

def test_sort_by_popularity_puts_most_popular_first(menu):
    names = [i.name for i in menu.sort_by_popularity()]
    assert names == ["Brownie", "Spicy Burger", "Large Soda", "Iced Tea"]


def test_sorting_does_not_reorder_the_stored_menu(menu):
    original = list(menu.items)
    menu.sort_by_popularity()
    assert menu.items == original


# --- Customer verification --------------------------------------------------

def test_new_customer_is_not_verified():
    assert Customer("Ada").is_verified() is False


def test_customer_with_purchase_history_is_verified():
    ada = Customer("Ada")
    order = Order()
    order.add_item(FoodItem("Soda", 2.50, "Drinks", 4.0))
    ada.purchase_history.append(order)
    assert ada.is_verified() is True


# --- Validation -------------------------------------------------------------

def test_negative_price_is_rejected():
    with pytest.raises(ValueError):
        FoodItem("Free Money", -1, "Mains", 5)


def test_blank_item_name_is_rejected():
    with pytest.raises(ValueError):
        FoodItem("   ", 1, "Mains", 5)


def test_blank_customer_name_is_rejected():
    with pytest.raises(ValueError):
        Customer("")
