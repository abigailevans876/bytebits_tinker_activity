### Visual UML representation based on the client feature request and the four required classes:
classDiagram
    class Customer {
        -name: String
        -purchaseHistory: List<Transaction>
        +browseMenu(menu: Menu) : void
        +createTransaction() : Transaction
    }

    class FoodItem {
        -name: String
        -price: double
        -category: String
        -popularityRating: double
        +getName() : String
        +getPrice() : double
        +getCategory() : String
        +getPopularityRating() : double
    }

    class Menu {
        -items: List<FoodItem>
        +addItem(item: FoodItem) : void
        +filterByCategory(category: String) : List<FoodItem>
        +sortByPopularity() : List<FoodItem>
    }

    class Transaction {
        -selectedItems: List<FoodItem>
        -totalCost: double
        +addItem(item: FoodItem) : void
        +calculateTotal() : double
        +getTotalCost() : double
    }

    Customer "1" --> "0..*" Transaction : has purchase history / places
    Menu "1" *-- "0..*" FoodItem : contains
    Transaction "1" *-- "1..*" FoodItem : stores selected items



    +-------------------+        +-------------------+
    |      Customer     |        |       Menu        |
    |-------------------|        |-------------------|
    | - name: String    |<>------| - items: List     |
    | - purchaseHistory |        |-------------------|
    |-------------------|        | + addItem()       |
    | + browseMenu()    |        | + filterByCategory() |
    | + createTransaction() |   + sortByPopularity() |
    +-------------------+        +-------------------+
    
                |
                | places
                v
    
    +-------------------+
    |    Transaction    |
    |-------------------|
    | - selectedItems   |
    | - totalCost       |
    |-------------------|
    | + addItem()       |
    | + calculateTotal()|
    +-------------------+
    
                |
                | stores
    
    +-------------------+
    |     FoodItem      |
    |-------------------|
    | - name: String    |
    | - price: double   |
    | - category: String|
    | - popularityRating|
    +-------------------+
