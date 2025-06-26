product_list = ["Laptop", "Mouse", "Keyboard", "Monitor", "Mouse"]
print(product_list[0])
print(product_list[-1])
product_list[1] = "Webcam"
print(product_list)
product_list.append("Printer")
print(product_list)
product_list.remove("Keyboard")
print(product_list)


student_infos = {
    "code": "SV001",
    "name": "Nguyen Van B",
    "age": 20,
    "major": "Khoa hoc may tinh",
}
print(student_infos)
student_infos["age"] = 21
print(student_infos)
student_infos["avg_score"] = 8.5
print(student_infos)
del student_infos["major"]
print(student_infos)


number_list = [1, 5, 2, 8, 3, 5, 1, 9, 2]
number_list = set(number_list)
print(number_list)
