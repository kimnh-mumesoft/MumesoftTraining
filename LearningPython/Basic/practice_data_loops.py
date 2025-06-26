# # bai tap 1
scores = [85, 92, 78, 60, 95, 70, 88, 55, 100, 65]
avg_score = 0
passed_students = 0
failed_students = 0
highest_score = scores[0]
lowest_score = scores[0]

for score in scores:
    avg_score += score
    if score >= 70:
        passed_students += 1
    else:
        failed_students += 1
    if score > highest_score:
        highest_score = score
    if score < lowest_score:
        lowest_score = score

avg_score /= len(scores)


print(round(avg_score, 2))
print(passed_students)
print(failed_students)
print(highest_score)
print(lowest_score)

# bai tap 2
products = [
    {"id": "P001", "name": "Laptop", "price": 1200, "quantity": 10},
    {"id": "P002", "name": "Mouse", "price": 25, "quantity": 50},
    {"id": "P003", "name": "Keyboard", "price": 75, "quantity": 30},
    {"id": "P004", "name": "Monitor", "price": 300, "quantity": 5},
    {"id": "P005", "name": "Mouse", "price": 30, "quantity": 20},  # Sản phẩm Mouse khác
]
total_value = 0

for product in products:
    print(f"{product['name']} - Gia: {product['price']}")

for product in products:
    total_value += product["price"] * product["quantity"]
print(f"Tổng giá trị các sản phẩm là: {total_value}")

for product in products:
    if product["name"] == "Mouse":
        print(
            f"ID: {product['id']}, Tên: {product['name']}, Giá: {product['price']}, Số lượng: {product['quantity']}"
        )

for product in products:
    if product["id"] == "P004":
        product["quantity"] = 15
        print(
            f"ID: {product['id']}, Tên: {product['name']}, Giá: {product['price']}, Số lượng: {product['quantity']}"
        )
