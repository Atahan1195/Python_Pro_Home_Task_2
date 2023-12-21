#                   Home Task Pro 2

# Task - 1
# Создайте класс Product для описания продукта (товара). В качестве атрибутов продукта можно употреблять название,
# цену и описание. Создайте несколько инстансов класса Product.
# Создайте класс Cart, который будет выступать в качестве корзины с продуктами определенного покупателя.
# Корзина может содержать несколько продуктов определенного количества. Реализуйте метод вычисления стоимости корзины.
# Во всех классах должен быть определен метод str.

# class Product:
#     """Class for product
#     Attributes:
#         name (str): name of product
#         price (int): price of product
#         description (str): description of product
#     """
#
#     def __init__(self, name, price, description):
#         self.name = name
#         self.price = price
#         self.description = description
#
#     def __str__(self):
#         return f"Product: {self.name}, price: {self.price}, description: {self.description}"
#
#
# class Cart:
#     """
#     Class for cart
#     Attributes:
#         customer_name (str): name of customer
#         products (dict): dictionary of products
#     """
#
#     def __init__(self, customer_name):
#         self.customer_name = customer_name
#         self.products = {}
#
#     def add_product(self, product, quantity):
#         """
#         Add product to cart
#         :param product: product
#         :param quantity: quantity of product
#         :return: None
#         """
#
#         if product not in self.products:
#             self.products[product] = 0
#         self.products[product] += quantity
#
#     def calculate_total(self):
#         """
#         Calculate total price of cart
#         :return: total price
#         """
#
#         total = 0
#         for product, quantity in self.products.items():
#             total += product.price * quantity
#         return total
#
#     def __str__(self):
#         """
#         String representation of cart
#         :return: string
#         """
#
#         cart_str = f"Cart for {self.customer_name}:\n"
#         for product, quantity in self.products.items():
#             cart_str += f"{product.name}: {product.description} - {quantity}\n"
#         cart_str += f"Total: {self.calculate_total()}$"
#         return cart_str
#
#
# product_1 = Product("Apple", 10, "Green apple")
# product_2 = Product("Orange", 20, "Orange orange")
# product_3 = Product("Banana", 30, "Yellow banana")
# product_4 = Product("Pineapple", 40, "Yellow pineapple")
# product_5 = Product("Grape", 50, "Purple grape")
#
# cart = Cart(input("Enter your name: "))
#
# cart.add_product(product_1, 2)
# cart.add_product(product_2, 3)
# cart.add_product(product_3, 4)
# cart.add_product(product_4, 5)
# cart.add_product(product_5, 6)
#
# print(cart)


# Task - 2
# Необходимо разработать Python-скрипт, возвращающий пользователю меню ресторана.
# Обычно меню ресторана содержит следующие элементы:
# - категории блюд (например, закуски, основные блюда, десерты).
# - блюда в каждой категории.
# Основные классы, которые необходимо создать для реализации меню ресторана:
# Класс Блюдо: отвечает за сохранение информации об отдельном блюде, включая его название, описание и цену.
# Класс Категория блюд: отвечает за сохранение блюд, относящихся к конкретной категории. Включает список объектов Блюдо.
#
# Для реализации приложения может быть использован следующий шаблон
#
# class Dish:
#     def __init__(self, name, description, price):
#         pass
#
# class MenuCategory:
#     def __init__(self, name, dishes):
#         pass


class Dish:
    """Class for dish
    Attributes:
        name (str): name of dish
        description (str): description of dish
        price (int): price of dish
    """

    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price

    def __str__(self):
        return f"{self.name}: {self.description} - {self.price}$"


class MenuCategory:
    """Class for menu category
    Attributes:
        name (str): name of category
        dishes (list): list of dishes
    """

    def __init__(self, name, dishes):
        self.name = name
        self.dishes = dishes

    def __str__(self):
        menu_category_str = f"{self.name}:\n"
        for dish in self.dishes:
            menu_category_str += f"{dish}\n"
        return menu_category_str


class RestaurantMenu:
    """Class for restaurant menu
    Attributes:
        menu_categories (list): list of menu categories
    """

    def __init__(self, menu_categories):
        self.menu_categories = menu_categories

    def __str__(self):
        restaurant_menu_str = ""
        for menu_category in self.menu_categories:
            restaurant_menu_str += f"{menu_category}\n"
        return restaurant_menu_str


dish1 = Dish("Caesar Salad", "Fresh romaine lettuce, croutons, and parmesan cheese.", 12.99)
dish2 = Dish("Chicken Wings", "Fried chicken wings with BBQ sauce.", 8.99)
dish3 = Dish("Chicken Fingers", "Fried chicken fingers with BBQ sauce.", 9.99)
dish4 = Dish("Chicken Burger", "Chicken burger with BBQ sauce.", 10.99)
dish5 = Dish("Chicken Sandwich", "Chicken sandwich with BBQ sauce.", 11.99)
dish6 = Dish("Ukrainian borscht", "Fried chicken nuggets with BBQ sauce.", 7.99)
dish7 = Dish("Chicken Soup", "Chicken soup with BBQ sauce.", 6.99)

menu_category1 = MenuCategory("Appetizers", [dish1, dish2])
menu_category2 = MenuCategory("Main Dishes", [dish3, dish4, dish5])
menu_category3 = MenuCategory("Soups", [dish6, dish7])

restaurant_menu = RestaurantMenu([menu_category1, menu_category2, menu_category3])

print(restaurant_menu)
