1. Encapsulation
Encapsulation can be used by bundling all relevant information and behaviors for each product into a single class, and restricting direct access to that data. Instead of having separate variables and functions scattered throughout the code, the product's data and the operations that act on that data are kept together inside one unit, with the data itself made private.
The main object is a Product class. The properties involved include name, price, and stock_quantity, which would be kept as private attributes rather than directly editable. The methods involved could include update_stock(), apply_discount(), or sell_item(), all of which act as the only approved way to read or change the product's internal data.
Applying encapsulation eliminates the need for global variables and scattered functions, and prevents other parts of the program from accidentally setting stock_quantity to an invalid value like a negative number. Since all product-related data and logic live inside the Product class and can only be changed through its own methods, the code becomes more organized, easier to debug, and less prone to accidental modification from outside the class.
2. Abstraction
Abstraction can be used by defining what every product must be able to do, such as calculate_price() or restock(), without exposing or requiring the caller to know how each product type does it internally. The store owner or cashier only needs to call straightforward methods without worrying about the underlying steps each product takes to complete them.
This could be modeled with an abstract Product class or interface that declares methods like sell(quantity) and restock(quantity) but leaves the specific implementation to each subclass. The cashier-facing code only interacts with these high-level method names, never with the step-by-step logic behind them.
Abstraction makes the system more user-friendly and readable, especially for non-programmers who might use the system. It also reduces errors, because users only interact with a clean, simplified interface and never need to understand or manage the internal steps behind each action.
3. Inheritance

Inheritance can be used by creating a general Product parent class that holds common attributes and methods, and then creating specialized child classes like Beverage, Snack, CannedGood, and Dairy that inherit from it. Each child class can add its own unique features while reusing everything from the parent.
The objects involved are the parent Product class and its child subclasses. The properties inherited include name, price, and stock. Child classes may add their own specific properties like volume (for Beverage), weight (for Snack), or expiration_date (for Dairy). Methods like calculate_discount() can also be inherited and optionally overridden.
Inheritance reduces code duplication significantly, common properties and methods are written only once in the parent class. This makes the system more manageable and easier to update, because changes to the parent class automatically apply to all child classes, saving time and reducing errors when adding new product categories.
4. Polymorphism
Polymorphism can be used by allowing different product types to respond to the same method name in their own unique way. For example, a display_info() method might show different details depending on whether the product is a beverage (showing volume) or a snack (showing weight), even though the method is called the same way for all products.
The objects involved are the various child classes like Beverage, Snack, and Dairy. The methods involved are shared ones like display_info(), calculate_discount(), or restock(). Each subclass implements these methods differently based on its own specific properties and business rules.
Polymorphism simplifies the main inventory loop or user interface, because you can treat all products uniformly. You can loop through a list of mixed product objects and call the same methods on each without needing if-elif checks to determine the product type. This makes the code more flexible, extensible, and easier to maintain when adding new product categories in the future.
Reflection Question:
After completing your explanations, answer the following question in 3-5 sentences:
Among the four pillars of Object-Oriented Programming, which do you think would be most useful in improving the sari-sari store inventory system? Explain your answer. 
I choose encapsulation as the most important pillar because it directly determines how manageable the rest of the system becomes. By bundling each product's data and behavior into one class, it becomes much easier to track which properties belong to which object instead of hunting through scattered variables across the program. This grouping also makes handling the inventory system more precise, since changes to stock or price can only happen through the product's own methods, reducing the chance of unintended or inconsistent updates. In this way, encapsulation acts as the practical foundation that makes the inventory system organized, predictable, and easier to maintain as it grows.

# ENCAPSULATION
class Product:
    private name, price, stock_quantity

    method update_stock(amount):
        stock_quantity = stock_quantity + amount   # only way to change stock

    method sell_item(quantity):
        if stock_quantity >= quantity:
            stock_quantity = stock_quantity - quantity


# ABSTRACTION
abstract class Product:
    method sell(quantity)     # what to do — no implementation shown
    method restock(quantity)  # how it's done is hidden from the user

cashier calls: product.sell(2)   # doesn't need to know internal steps


# INHERITANCE
class Product:
    name, price, stock_quantity
    method display_info()

class Beverage inherits Product:
    volume                     # extra property
    method display_info():     # can override parent's version
        print(name, price, volume)

class Snack inherits Product:
    weight                     # extra property


# POLYMORPHISM
for item in inventory_list:      # mixed list of Beverage, Snack, Dairy
    item.display_info()          # same method call, different result per type


