so_kiem_tra = 7
if so_kiem_tra % 2 == 0:
    print(f"{so_kiem_tra} la so chan")
else:
    print(f"{so_kiem_tra} la so le")


for number in range(10):
    print(number + 1)


input_number = int(input("Nhap mot so nguyen: "))
total = 0
current_number = 1
while current_number <= input_number:
    total = total + current_number
    current_number += 1

print(f"Tong cac so tu 1 den {input_number} la: {total}")
