ByteBites Domain Model

This UML class diagram defines the core domain entities required for the ByteBites application. The Customer class represents a registered user and stores a purchase history to confirm prior account activity. The FoodItem class models the products sold, including their identity, category, unit price, and popularity. The Menu class manages the full product catalog and supports filtering and sorting based on menu attributes. The Transaction class represents a completed or active purchase session, binds selected items to a customer, and calculates the total cost.

+--------------------------------------------------+
| Customer                                         |
+--------------------------------------------------+
| - name: String                                   |
| - purchaseHistory: List<Transaction>              |
+--------------------------------------------------+
| + Customer(name: String)                          |
| + getName(): String                              |
| + addPurchase(transaction: Transaction): void    |
| + getPurchaseHistory(): List<Transaction>        |
+--------------------------------------------------+

                 |
                 | purchaseHistory
                 v

+--------------------------------------------------+
| Transaction                                      |
+--------------------------------------------------+
| - customer: Customer                             |
| - selectedItems: List<FoodItem>                  |
+--------------------------------------------------+
| + Transaction(customer: Customer,                 |
|   selectedItems: List<FoodItem>)                  |
| + addItem(item: FoodItem): void                  |
| + getSelectedItems(): List<FoodItem>             |
| + calculateTotal(): double                       |
| + getCustomer(): Customer                        |
+--------------------------------------------------+

                 |
                 | includes
                 v

+--------------------------------------------------+
| FoodItem                                         |
+--------------------------------------------------+
| - name: String                                   |
| - price: double                                  |
| - category: String                               |
| - popularityRating: int                          |
+--------------------------------------------------+
| + FoodItem(name: String, price: double,          |
|   category: String, popularityRating: int)       |
| + getName(): String                              |
| + getPrice(): double                             |
| + getCategory(): String                          |
| + getPopularityRating(): int                     |
+--------------------------------------------------+

                 ^
                 | contains

+--------------------------------------------------+
| Menu                                             |
+--------------------------------------------------+
| - items: List<FoodItem>                          |
+--------------------------------------------------+
| + Menu(items: List<FoodItem>)                    |
| + addItem(item: FoodItem): void                  |
| + getItems(): List<FoodItem>                    |
| + filterByCategory(category: String): List<FoodItem> |
| + sortByPopularity(): List<FoodItem>             |
+--------------------------------------------------+