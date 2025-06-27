from collections import defaultdict, Counter
from json import dump

all_transactions = []
total_overall_revenue = 0.0
product_quantity_sold = Counter()
product_revenue = defaultdict(float)
daily_revenue = defaultdict(float)

report_file_name = "sales_data.txt"
report_file = "sales_report.json"
try:
    with open(report_file_name, "r") as file:
        for line in file:
            parts = line.strip().split(",")
            date_str, product_name, price_str, quantity_str = parts
            price = float(price_str)
            quantity = int(quantity_str)
            transaction = {
                "sale_date": date_str,
                "product_name": product_name,
                "price": price,
                "quantity": quantity,
            }
            total_price = price * quantity
            transaction["total_price"] = total_price
            product_quantity_sold[product_name] += quantity
            product_revenue[product_name] += total_price
            daily_revenue[date_str] += total_price
            total_overall_revenue += total_price
            all_transactions.append(transaction)

except IOError:
    print("Error when reading file")
except FileNotFoundError:
    print(f"File {report_file_name} not found")


print("\n--- Phân tích dữ liệu bán hàng ---")
print(f"Tổng doanh thu chung: {total_overall_revenue:,.2f} VND")  # Định dạng tiền tệ
print(
    "Tổng số lượng sản phẩm đã bán của mỗi loại:",
    dict(product_quantity_sold),
)  # Chuyển Counter thành dict để in đẹp
print("Tổng doanh thu theo từng sản phẩm:", dict(product_revenue))
print("Doanh thu theo từng ngày:", dict(daily_revenue))

final_report = {
    "total_overall_revenue": total_overall_revenue,
    "product_quantity_sold": dict(),  # Chuyển Counter thành dict
    "product_revenue": dict(product_revenue),  # Chuyển defaultdict thành dict
    "daily_revenue": dict(daily_revenue),  # Chuyển defaultdict thành dict
}

try:
    with open(report_file, "w", encoding="utf-8") as f:
        dump(final_report, f, indent=4, ensure_ascii=False)
    print(f"\nĐã ghi báo cáo vào tệp '{report_file}'.")
except IOError as e:
    print(f"Lỗi khi ghi báo cáo vào tệp '{report_file}': {e}")
except Exception as e:
    print(f"Lỗi không xác định khi ghi báo cáo: {e}")
