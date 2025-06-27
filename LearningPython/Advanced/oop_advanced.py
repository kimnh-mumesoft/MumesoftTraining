# class Product:
#     def __init__(self, product_id, name, price):
#         self.product_id = product_id
#         self.name = name
#         self.price = price

#     def display_info(self):
#         print(f"ID: {self.product_id}, Name: {self.name}, Price: {self.price}")


# class Electronics(Product):
#     def __init__(self, product_id, name, price, warranty_months):
#         super().__init__(product_id, name, price)
#         self.warranty_months = warranty_months

#     def display_info(self):
#         super().display_info()
#         print(f"Warranty: {self.warranty_months} months")


# class Book(Product):
#     def __init__(self, product_id, name, price, author, page):
#         super().__init__(product_id, name, price)
#         self.author = author
#         self.page = page

#     def display_info(self):
#         super().display_info()
#         print(f"Author: {self.author}, Page: {self.page}")


# products = [
#     Electronics("EL001", "Laptop XYZ", 1200, 24),
#     Book("BK001", "Clean Code", 45, "Robert C. Martin", 464),
#     Electronics("EL002", "Smartwatch ABC", 250, 12),
# ]

# for product in products:
#     product.display_info()
#     print("-" * 20)


class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        if not isinstance(value, str) or len(value) < 3 or " " in value:
            raise ValueError(
                "Username must be a string with at least 3 characters without spaces."
            )
        self._username = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if not isinstance(value, str) or "@" not in value or "." not in value:
            raise ValueError("Email must be a valid email address.")
        self._email = value


print("\n--- Kiểm tra lớp User ---")
try:
    user1 = User("john_doe", "john.doe@example.com")
    print(f"Người dùng hợp lệ: {user1.username}, {user1.email}")

    # user1.username = "jd"  # Sẽ gây lỗi
except ValueError as e:
    print(f"Lỗi: {e}")

try:
    user2 = User("jane_smith", "jane_smith_example.com")  # Sẽ gây lỗi
    # user2.email = "jane_smith@example"
except ValueError as e:
    print(f"Lỗi: {e}")

try:
    user3 = User("valid_user", "valid@email.com")
    print(f"Người dùng hợp lệ khác: {user3.username}, {user3.email}")
    user3.email = "new.valid@email.org"  # Gán hợp lệ
    print(f"Email đã cập nhật: {user3.email}")
except ValueError as e:
    print(f"Lỗi: {e}")


# class Converter:
#     conversion_factor_cm_to_inch = 2.54

#     @staticmethod
#     def celsius_to_fahrenheit(celsius):
#         return celsius * 9 / 5 + 32

#     @staticmethod
#     def fahrenheit_to_celsius(fahrenheit):
#         return (fahrenheit - 32) * 5 / 9

#     @classmethod
#     def convert_cm_to_inch(cls, cm):
#         return cm / cls.conversion_factor_cm_to_inch

#     @classmethod
#     def convert_inch_to_cm(cls, new_factor):
#         return cls.conversion_factor_cm_to_inch * new_factor


# print("\n--- Kiểm tra Converter ---")
# print(f"30 độ C = {Converter.celsius_to_fahrenheit(30):.2f} độ F")
# print(f"86 độ F = {Converter.fahrenheit_to_celsius(86):.2f} độ C")

# print(
#     f"10 cm = {Converter.convert_cm_to_inch(10):.2f} inch (Factor: {Converter.conversion_factor_cm_to_inch})"
# )
# Converter.set_cm_to_inch_factor(2.5)  # Thay đổi hệ số
# print(
#     f"10 cm = {Converter.convert_cm_to_inch(10):.2f} inch (New Factor: {Converter.conversion_factor_cm_to_inch})"
# )
