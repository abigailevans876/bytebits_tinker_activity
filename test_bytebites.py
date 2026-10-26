from models import Customer, FoodItem, Menu, Transaction

def test_order_total_with_multiple_items():
    burger = FoodItem("Spicy Burger", 8.99, "Entrees", 4.8)
    soda = FoodItem("Large Soda", 2.25, "Drinks", 4.6)
    fries = FoodItem("Loaded Fries", 5.75, "Sides", 4.7)

    order = Transaction()
    order.addItem(burger)
    order.addItem(soda)
    order.addItem(fries)

    assert order.calculateTotal() == 16.99
    assert order.getTotalCost() == 16.99


def test_empty_transaction_total_is_zero():
    order = Transaction()

    assert order.calculateTotal() == 0.0
    assert order.getTotalCost() == 0.0


def test_menu_filters_items_by_category():
    menu = Menu()
    burger = FoodItem("Spicy Burger", 8.99, "Entrees", 4.8)
    soda = FoodItem("Large Soda", 2.25, "Drinks", 4.6)
    pie = FoodItem("Chocolate Pie", 4.50, "Desserts", 4.9)

    menu.addItem(burger)
    menu.addItem(soda)
    menu.addItem(pie)

    drinks = menu.filterByCategory("Drinks")

    assert len(drinks) == 1
    assert drinks[0].getName() == "Large Soda"


def test_menu_sorts_items_by_popularity():
    menu = Menu()
    burger = FoodItem("Spicy Burger", 8.99, "Entrees", 4.8)
    soda = FoodItem("Large Soda", 2.25, "Drinks", 4.6)
    pie = FoodItem("Chocolate Pie", 4.50, "Desserts", 4.9)

    menu.addItem(burger)
    menu.addItem(soda)
    menu.addItem(pie)

    sorted_items = menu.sortByPopularity()

    assert [item.getName() for item in sorted_items] == [
        "Chocolate Pie",
        "Spicy Burger",
        "Large Soda",
    ]


def test_customer_can_create_transaction():
    customer = Customer("Alex")

    transaction = customer.createTransaction()

    assert isinstance(transaction, Transaction)


def test_negative_price_raises_value_error():
    try:
        FoodItem("Bad Item", -1.00, "Drinks", 2.0)
        assert False, "Expected ValueError for negative price"
    except ValueError:
        pass