# while True:
#     try:
#         num1 = int(input("Enter number 1: "))
#         num2 = int(input("Enter number 2: "))
#         result = num1 / num2
#     except ValueError:
#         print("Invalid input. Please enter an integer.")
#     except ZeroDivisionError:
#         print("Cannot divide by zero.")
#     else:
#         print("Result:", result)
#         break

#     finally:
#         print("Program completed.")

# import os

# print(f"Thư mục làm việc hiện tại: {os.getcwd()}")


# file_name = "test_file1.txt"
# try:
#     with open(file_name, "r") as file:
#         content = file.read()
#         print(content)
# except FileNotFoundError:
#     print(f"File '{file_name}' not found.")
# except Exception as e:
#     print(f"An error occurred: {e}")
# else:
#     print(f"File {file_name} read successfully.")
#     print("End of program.")

import os

file_name = "test_file.txt"
if os.path.exists(file_name):
    print(f"Tệp '{file_name}' TỒN TẠI ở đây.")
    try:
        with open(file_name, "r") as file:
            content = file.read()
            print(f"Nội dung: {content}")
    except Exception as e:
        print(f"Có lỗi khi cố gắng đọc tệp: {e}")
else:
    print(f"Tệp '{file_name}' KHÔNG TỒN TẠI ở thư mục này.")
