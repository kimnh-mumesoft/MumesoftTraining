employee_records = [
    {"id": 101, "name": "Alice Smith", "department": "HR", "salary": 60000},
    {"id": 102, "name": "Bob Johnson", "department": "IT", "salary": 75000},
    {"id": 103, "name": "Charlie Brown", "department": "Finance", "salary": 62000},
]

new_employee = {"id": 104, "name": "David Lee", "department": "IT", "salary": 80000}
employee_records.append(new_employee)
print(employee_records)

# for employee in employee_records:
#     if employee["id"] == 102:
#         employee["salary"] = 85000

#     if employee["id"] == 103:
#         employee["status"] = "Active"

#     if employee["id"] == 1031:
#         employee_records.remove(employee)


id_to_remove = 101
# Tạo một list mới chỉ bao gồm những employee CÓ ID KHÁC với ID cần xóa
employee_records = [
    employee["name"] for employee in employee_records if employee["id"] != id_to_remove
]

print(employee_records)
