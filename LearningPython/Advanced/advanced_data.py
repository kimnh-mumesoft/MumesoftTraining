# from collections import defaultdict

# # Ví dụ: Đếm tần suất xuất hiện của các từ
# word_counts = defaultdict(int)  # int() mặc định là 0
# words = ["apple", "banana", "apple", "orange", "banana", "apple"]

# for word in words:
#     word_counts[
#         word
#     ] += 1  # Nếu 'word' chưa có, word_counts[word] sẽ là 0 trước khi cộng 1

# print("Đếm từ với defaultdict:", word_counts)
# # Output: Đếm từ với defaultdict: defaultdict(<class 'int'>, {'apple': 3, 'banana': 2, 'orange': 1})

# # Ví dụ: Nhóm các phần tử vào list
# category_items = defaultdict(list)  # list() mặc định là []
# data = [("fruit", "apple"), ("vegetable", "carrot"), ("fruit", "banana")]

# for category, item in data:
#     category_items[category].append(item)

# print("Nhóm mục theo danh mục:", category_items)
# # Output: Nhóm mục theo danh mục: defaultdict(<class 'list'>, {'fruit': ['apple', 'banana'], 'vegetable': ['carrot']})


# from collections import Counter

# # Đếm tần suất ký tự trong chuỗi
# sentence = "hello world"
# char_counts = Counter(sentence)
# print("Đếm ký tự với Counter:", char_counts)
# # Output: Đếm ký tự với Counter: Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})

# # Đếm từ trong list
# fruits = ["apple", "banana", "apple", "orange", "banana", "apple"]
# fruit_counts = Counter(fruits)
# print("Đếm trái cây với Counter:", fruit_counts)
# # Output: Đếm trái cây với Counter: Counter({'apple': 3, 'banana': 2, 'orange': 1})

# print("3 phần tử phổ biến nhất:", fruit_counts.most_common(2))  # Top 2 phổ biến nhất
# # Output: 3 phần tử phổ biến nhất: [('apple', 3), ('banana', 2)]


# from datetime import datetime, date, time, timedelta

# # Lấy thời gian hiện tại
# now = datetime.now()
# print("Thời gian hiện tại (datetime):", now)
# # Output: Thời gian hiện tại (datetime): 2025-06-27 08:31:25.123456 (số có thể khác)

# # Lấy ngày hiện tại
# today = date.today()
# print("Ngày hiện tại (date):", today)

# # Tạo một đối tượng datetime cụ thể
# specific_dt = datetime(2025, 12, 25, 10, 30, 0)  # Năm, tháng, ngày, giờ, phút, giây
# print("Thời gian cụ thể:", specific_dt)

# # Định dạng datetime sang chuỗi (strftime - string format time)
# formatted_dt = now.strftime("%Y-%m-%d %H:%M:%S")
# print("Thời gian định dạng:", formatted_dt)  # 2025-06-27 08:31:25

# # Chuyển chuỗi thành datetime (strptime - string parse time)
# date_string = "2024-01-15 14:00:00"
# parsed_dt = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
# print("Chuỗi được phân tích thành datetime:", parsed_dt)

# # Cộng trừ thời gian với timedelta
# future_date = now + timedelta(days=7, hours=3)
# print("7 ngày và 3 giờ sau:", future_date)

# past_date = now - timedelta(weeks=2)
# print("2 tuần trước:", past_date)

# # Tính khoảng thời gian giữa hai datetime
# time_difference = now - parsed_dt
# print("Khoảng thời gian (timedelta):", time_difference)
# print("Số ngày trong khoảng thời gian:", time_difference.days)

# import json
# from datetime import datetime

# # --- json.dumps() và json.loads() ---

# # Đối tượng Python (dictionary)
# python_dict_data = {
#     "name": "Alice",
#     "age": 30,
#     "is_student": False,
#     "courses": ["Math", "Science"],
#     "address": {"street": "123 Main St", "city": "Anytown"},
# }

# # Chuyển đổi Python dict sang chuỗi JSON
# json_string_data = json.dumps(
#     python_dict_data, indent=4
# )  # indent=4 để định dạng đẹp, dễ đọc
# print("Python dict thành chuỗi JSON:")
# print(json_string_data)
# Output:
# {
#     "name": "Alice",
#     "age": 30,
#     "is_student": false,
#     "courses": [
#         "Math",
#         "Science"
#     ],
#     "address": {
#         "street": "123 Main St",
#         "city": "Anytown"
#     }
# }

# Chuỗi JSON
# json_str = '{"product": "Laptop", "price": 1200, "in_stock": true}'

# # Chuyển đổi chuỗi JSON thành đối tượng Python (dict)
# python_object_from_json = json.loads(json_str)
# print("\nChuỗi JSON thành Python object (dict):", python_object_from_json)
# print(
#     "Tên sản phẩm:", python_object_from_json["product"]
# )  # Truy cập như dict bình thường

# # --- json.dump() và json.load() (làm việc với tệp) ---

# # Ghi dữ liệu Python dict vào tệp JSON
# file_name = "data.json"
# data_to_save = {
#     "users": [
#         {"id": 1, "username": "user1", "email": "user1@example.com"},
#         {"id": 2, "username": "user2", "email": "user2@example.com"},
#     ],
#     "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
# }

# try:
#     with open(file_name, "w", encoding="utf-8") as f:
#         json.dump(
#             data_to_save, f, indent=4, ensure_ascii=False
#         )  # ensure_ascii=False để hỗ trợ UTF-8
#     print(f"\nĐã ghi dữ liệu vào '{file_name}'")
# except IOError as e:
#     print(f"Lỗi khi ghi tệp JSON: {e}")

# # Đọc dữ liệu từ tệp JSON
# try:
#     with open(file_name, "r", encoding="utf-8") as f:
#         loaded_data = json.load(f)
#     print(f"Đã đọc dữ liệu từ '{file_name}':")
#     print(loaded_data)
#     print("Tên người dùng đầu tiên:", loaded_data["users"][0]["username"])
# except FileNotFoundError:
#     print(f"Tệp '{file_name}' không tồn tại.")
# except json.JSONDecodeError as e:  # Bắt lỗi nếu file không phải là JSON hợp lệ
#     print(f"Lỗi khi phân tích cú pháp JSON: {e}")
# except IOError as e:
#     print(f"Lỗi khi đọc tệp JSON: {e}")

from collections import Counter, defaultdict
from json import dump, load, JSONDecodeError


log_entries = [
    "2025-06-27 10:05:00 - LOGIN",
    "2025-06-27 10:10:30 - LOGOUT",
    "2025-06-27 10:15:00 - LOGIN",
    "2025-06-28 09:00:00 - LOGIN",
    "2025-06-28 09:30:00 - REPORT_GENERATED",
    "2025-06-28 10:00:00 - LOGOUT",
    "2025-06-29 11:00:00 - LOGIN",
]

# Đếm số lập tập
print("--- Tần suất từng loại sự kiện ---")
# Trích xuất loại sự kiện từ mỗi log entry
event_types = [entry.split(" - ")[-1] for entry in log_entries]
event_counts = Counter(event_types)
print("Tần suất sự kiện:", event_counts)
# Expected Output: Counter({'LOGIN': 4, 'LOGOUT': 2, 'REPORT_GENERATED': 1})
dates = [entry.split(" ")[0] for entry in log_entries]
date_counts = Counter(dates)
# time_count = defaultdict(int)
# for entry in log_entries:
#     time = entry.split(" ")[0]
#     time_count[time] += 1

print(date_counts)

app_config = {
    "database": {
        "host": "localhost",
        "port": 5432,
        "user": "admin",
        "password": "secure_password",
    },
    "api_keys": {"weather_api": "YOUR_WEATHER_API_KEY", "map_api": "YOUR_MAP_API_KEY"},
    "debug_mode": True,
    "version": 1.0,
}

file_name = "config.json"
try:
    with open(file_name, "w", encoding=("utf-8")) as file:
        dump(app_config, file, indent=4, ensure_ascii=False)
except IOError as e:
    print(f"Error when writing file {e}")

try:
    with open(file_name, "r", encoding=("utf-8")) as file:
        data = load(file)
        print(data["database"]["host"])
        print(data["api_keys"]["map_api"])
        print(data["debug_mode"])
except IOError as e:
    print(f"Error when reading file {e}")
except FileNotFoundError:
    print(f"File {file_name} not found")
except JSONDecodeError as e:
    print(f"Error decoding file {e}")
