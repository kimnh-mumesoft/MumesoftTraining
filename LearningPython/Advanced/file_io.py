# ex1

# file_name = "activity_log.txt"

# try:
#     with open(file_name, "a") as file:
#         file.write("2025-06-27 09:00: User 'admin' logged in\n")
#         file.write("2025-06-27 09:15: Item 'Laptop' added to cart\n")
#         file.write("2025-06-27 09:30: Order #123 processed successfully")
#         print("File logged successfully")
# except IOError:
#     print("Error logging file")
# except FileNotFoundError:
#     print("File not found")


# try:
#     with open(file_name, "r") as file:
#         print("Contents of the file: " + file_name)
#         for line in file:
#             print(line.strip())

# except IOError:
#     print("Error logging file")
# except FileNotFoundError:
#     print(f"file {file_name} not found")


file_name = "todo_list.txt"
tasks = ["Mua sữa", "Học Python", "Tập thể dục", "Viết báo cáo"]

try:
    with open(file_name, "w", encoding="utf-8") as file:
        for task in tasks:
            file.write(task + "\n")
        print(f"Task list saved to {file_name}")
except IOError as e:
    print(f"Error when logging file: {e}")
except UnicodeEncodeError as e:
    print("Error decoding file " + e)
except Exception as e:
    print(f"An error occurred: {e}")

try:
    with open(file_name, "r") as file:
        for index, line in enumerate(file):
            print(f"{index + 1}. {line.strip()}")

except FileNotFoundError:
    print(f"File {file_name} not found")
except UnicodeDecodeError as e:
    print("Error decoding file " + e)
except IOError as e:
    print(f"Error when reading file {e}")
