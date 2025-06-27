import requests
import json

try:
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    response.raise_for_status()
    if response.status_code == 200 or response.ok:
        users = response.json()
        for i, user in enumerate(users[:3]):  # Lặp qua 3 người dùng đầu tiên
            print(f"- Tên: {user['name']}, Email: {user['email']}")
except requests.exceptions.HTTPError as errh:
    print(f"Lỗi HTTP: {errh}")
except requests.exceptions.ConnectionError as errc:
    print(f"Lỗi kết nối: {errc}")
except requests.exceptions.Timeout as errt:
    print(f"Lỗi timeout: {errt}")
except requests.exceptions.RequestException as err:  # Bắt mọi lỗi khác của requests
    print(f"Lỗi requests: {err}")
except json.JSONDecodeError:
    print("Lỗi: Phản hồi không phải là JSON hợp lệ.")
except Exception as e:
    print(f"Một lỗi không mong muốn xảy ra: {e}")


post_url = "https://jsonplaceholder.typicode.com/posts"
new_post_data = {
    "title": "Bài viết mới của tôi",
    "body": "Nội dung bài viết được tạo từ Python.",
    "userId": 5,
}

try:
    response = requests.post(post_url, json=new_post_data)
    response.raise_for_status()
    if response.status_code == 201:
        new_post = response.json()
        print(f"Bài viết mới được tạo: {new_post}")
except requests.exceptions.RequestException as e:
    print(f"Lỗi requests: {e}")
except json.JSONDecodeError:
    print("Lỗi: Phản hồi không phải là JSON hợp lệ.")
except Exception as e:
    print(f"Một lỗi không mong muốn xảy ra: {e}")
