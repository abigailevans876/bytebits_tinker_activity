# ByteBites model summary:
# Customer: represents a user and tracks their name and purchase history.
# FoodItem: represents a menu item with a name, price, category, and popularity rating.
# Menu: stores the collection of available food items and supports filtering by category.
# Transaction: groups selected items into one purchase and calculates the total cost.

class Customer:
    def __init__(self, name):
        self.name = name
        self.purchaseHistory = []

    def browseMenu(self, menu):
        # Allows the customer to inspect the available menu items.
        return menu.items

    def createTransaction(self):
        # Creates a new transaction for the customer.
        return Transaction()


class FoodItem:
    def __init__(self, name, price, category, popularityRating):
        self.name = name
        self.price = float(price)
        self.category = category
        self.popularityRating = float(popularityRating)

        if self.price < 0:
            raise ValueError("Price cannot be negative.")

    def getName(self):
        return self.name

    def getPrice(self):
        return self.price

    def getCategory(self):
        return self.category

    def getPopularityRating(self):
        return self.popularityRating


class Menu:
    def __init__(self):
        self.items = []

    def addItem(self, item):
        # Adds a FoodItem to the menu catalog.
        self.items.append(item)

    def filterByCategory(self, category):
        # Returns only the items matching the given category.
        return [item for item in self.items if item.getCategory() == category]

    def sortByPopularity(self):
        # Returns items ordered from most popular to least popular.
        return sorted(self.items, key=lambda item: item.getPopularityRating(), reverse=True)


class Transaction:
    def __init__(self):
        self.selectedItems = []
        self.totalCost = 0.0

    def addItem(self, item):
        # Adds a selected FoodItem to this transaction.
        self.selectedItems.append(item)

    def calculateTotal(self):
        # Sums the price of each selected item and stores the result.
        self.totalCost = round(sum(item.getPrice() for item in self.selectedItems), 2)
        return self.totalCost

    def getTotalCost(self):
        # Returns the transaction's total cost.
        return self.calculateTotal()


if __name__ == "__main__":
    burger = FoodItem("Spicy Burger", 8.99, "Entrees", 4.8)
    soda = FoodItem("Large Soda", 2.25, "Drinks", 4.6)
    pie = FoodItem("Chocolate Pie", 4.50, "Desserts", 4.9)
    fries = FoodItem("Loaded Fries", 5.75, "Sides", 4.7)

    menu = Menu()
    menu.addItem(burger)
    menu.addItem(soda)
    menu.addItem(pie)
    menu.addItem(fries)

    drinks = menu.filterByCategory("Drinks")
    popular_items = menu.sortByPopularity()

    customer = Customer("Alex")
    order = customer.createTransaction()
    order.addItem(burger)
    order.addItem(soda)
    order.addItem(fries)

    print("Drinks in menu:", [item.getName() for item in drinks])
    print("Most popular to least:", [item.getName() for item in popular_items])
    print("Order total:", order.getTotalCost())
    print("Selected items:", [item.getName() for item in order.selectedItems])
