import uuid
from datetime import datetime, date, timedelta
import re  # Để kiểm tra định dạng ISBN và email


class LibraryItem:
    def __init__(self, item_id, title, publication_year):
        self._item_id = str(item_id)
        self.title = title
        self.publication_year = publication_year

    @property
    def item_id(self):
        return self._item_id

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if not isinstance(title, str):
            raise TypeError("Title must be a string.")
        elif " " not in title.strip():
            raise ValueError("Title cannot be empty.")
        self._title = title

    @property
    def publication_year(self):
        return self._publication_year

    @publication_year.setter
    def publication_year(self, publication_year):
        if not isinstance(publication_year, int):
            raise TypeError("Publication year must be an integer.")
        elif publication_year > date.today().year:
            raise ValueError("Publication year cannot be in the future.")
        self._publication_year = publication_year

    def display_info(self):
        print(f"Item ID: {self.item_id}")
        print(f"Title: {self.title}")
        print(f"Publication Year: {self.publication_year}")


class Book(LibraryItem):
    def __init__(self, item_id, title, publication_year, author, isbn):
        super().__init__(item_id, title, publication_year)
        self.author = author
        self.isbn = isbn

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, author):
        if not isinstance(author, str):
            raise TypeError("Author must be a string.")
        elif " " not in author.strip():
            raise ValueError("Author name cannot be empty.")
        self._author = author

    @property
    def isbn(self):
        return self._isbn

    @isbn.setter
    def isbn(self, value):
        if not isinstance(value, str):
            raise TypeError("ISBN must be a string.")
        elif not re.fullmatch(r"^[0-9-]+$", value):
            raise ValueError("Invalid ISBN format.")
        self._isbn = value

    def display_info(self):
        super().display_info()
        print(f"Author: {self.author}")
        print(f"ISBN: {self.isbn}")

    @classmethod
    def create_book(cls, title, publication_year, author, isbn):
        return cls(str(uuid.uuid4()), title, publication_year, author, isbn)


class Borrower:
    def __init__(self, borrowed_id, name, email):
        self._borrowed_id = borrowed_id
        self.name = name
        self.email = email

    @property
    def borrower_id(self):
        return self._borrowed_id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be a string.")
        elif " " not in name.strip():
            raise ValueError("Name cannot be empty.")
        self._name = name

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        if not isinstance(email, str):
            raise TypeError("Email must be a string.")
        if "@" not in email or "." not in email:
            raise ValueError("Invalid email format.")
        self._email = email

    def display_info(self):
        print(f"  Borrower ID: {self.borrower_id}")
        print(f"  Name: {self.name}")
        print(f"  Email: {self.email}")

    @classmethod
    def register_borrower(cls, name, email):
        return cls(str(uuid.uuid4()), name, email)


class Loan:
    def __init__(self, item, borrower):
        if not isinstance(item, LibraryItem):
            raise TypeError("Item must be an instance of LibraryItem.")
        if not isinstance(borrower, Borrower):
            raise TypeError("Borrower must be an instance of Borrower.")

        self._loan_id = str(uuid.uuid4())
        self._item = item  # Lưu trữ đối tượng LibraryItem
        self._borrower = borrower  # Lưu trữ đối tượng Borrower
        self._loan_date = datetime.now()
        self._return_date = None

    @property
    def loan_id(self):
        return self._loan_id

    @property
    def item(self):
        return self._item

    @property
    def borrower(self):
        return self._borrower

    @property
    def loan_date(self):
        return self._loan_date

    @property
    def return_date(self):
        return self._return_date

    @return_date.setter
    def return_date(self, value):
        if self._return_date is not None:
            raise ValueError("Return date has already been set and cannot be changed.")
        if not isinstance(value, datetime):
            raise ValueError("Return date must be a datetime object.")
        if value < self._loan_date:
            raise ValueError("Return date cannot be earlier than loan date.")
        self._return_date = value

    def is_returned(self):
        return self._return_date is not None

    def display_loan_info(self):
        print(f"Loan ID: {self.loan_id}")
        print(f"Loan Date: {self.loan_date.strftime('%Y-%m-%d %H:%M:%S')}")

        print("\n--- Item Details ---")
        # Gọi phương thức display_info của đối tượng item
        self.item.display_info()

        # Lấy thông tin từ đối tượng borrower (Borrower)
        print("\n--- Borrower Details ---")
        self.borrower.display_info()

        if self.is_returned():
            print(f"Return Date: {self.return_date.strftime('%Y-%m-%d %H:%M:%S')}")
        else:
            print("Status: Not yet returned.")

    @staticmethod
    def calculate_loan_duration_days(loan_date, return_date):
        if not isinstance(loan_date, datetime):
            raise TypeError("loan_date must be a datetime object.")
        if return_date is None:
            return None  # Chưa trả thì không tính được thời gian mượn

        if not isinstance(return_date, datetime):
            raise TypeError("return_date must be a datetime object or None.")
        if return_date < loan_date:
            raise ValueError(
                "Return date cannot be earlier than loan date for duration calculation."
            )

        duration = return_date - loan_date
        return duration.days


# --- Bắt đầu kiểm tra ---

print("=" * 50)
print("--- TEST LibraryItem & Book ---")
print("=" * 50)

# 1. Tạo Book hợp lệ
try:
    book1 = Book.create_book(
        "Python Programming", 2023, "Alice Smith", "978-1234567890"
    )
    print("--- Book 1 (Hợp lệ) ---")
    book1.display_info()
    print("\nCập nhật tiêu đề:")
    book1.title = "Advanced Python"
    book1.display_info()
except ValueError as e:
    print(f"Lỗi tạo/cập nhật Book 1: {e}")
print("-" * 30)

# 2. Tạo Book không hợp lệ (Năm xuất bản trong tương lai)
try:
    book_invalid_year = Book.create_book(
        "Future Tech", datetime.now().year + 1, "Bob Johnson", "978-0000000000"
    )
    print("--- Book với năm xuất bản không hợp lệ (Không nên hiển thị) ---")
    book_invalid_year.display_info()
except ValueError as e:
    print(f"Lỗi tạo Book (năm xuất bản): {e}")
print("-" * 30)

# 3. Tạo Book không hợp lệ (ISBN sai định dạng)
try:
    book_invalid_isbn = Book.create_book(
        "Invalid ISBN Book", 2020, "Charlie Brown", "ABC-123"
    )
    print("--- Book với ISBN không hợp lệ (Không nên hiển thị) ---")
    book_invalid_isbn.display_info()
except ValueError as e:
    print(f"Lỗi tạo Book (ISBN): {e}")
print("-" * 30)


print("\n" + "=" * 50)
print("--- TEST Borrower ---")
print("=" * 50)

# 4. Tạo Borrower hợp lệ
try:
    borrower1 = Borrower.register_borrower("Nguyen Van A", "nguyenvana@example.com")
    print("--- Borrower 1 (Hợp lệ) ---")
    borrower1.display_info()
    print("\nCập nhật tên:")
    borrower1.name = "Nguyen Van An"
    borrower1.display_info()
except ValueError as e:
    print(f"Lỗi tạo/cập nhật Borrower 1: {e}")
print("-" * 30)

# 5. Tạo Borrower không hợp lệ (Email sai định dạng)
try:
    borrower_invalid_email = Borrower.register_borrower(
        "Le Thi B", "lethib@example"  # Thiếu .com
    )
    print("--- Borrower với email không hợp lệ (Không nên hiển thị) ---")
    borrower_invalid_email.display_info()
except ValueError as e:
    print(f"Lỗi tạo Borrower (email): {e}")
print("-" * 30)


print("\n" + "=" * 50)
print("--- TEST Loan ---")
print("=" * 50)

# Đảm bảo có các đối tượng hợp lệ để tạo Loan
try:
    # Nếu book1 và borrower1 không được tạo do lỗi trước đó, tạo lại ở đây
    book1_for_loan = Book.create_book(
        "Data Science Basics", 2021, "Emily White", "978-9999999999"
    )
    borrower1_for_loan = Borrower.register_borrower(
        "Tran Van C", "tranvanc@library.org"
    )

    # 6. Tạo Loan hợp lệ và trả sách
    print("--- Loan 1 (Mượn và trả sách) ---")
    loan1 = Loan(book1_for_loan, borrower1_for_loan)
    loan1.display_loan_info()
    print(f"Đã trả sách? {loan1.is_returned()}")
    print("\nĐang trả sách...")
    return_time = loan1.loan_date + timedelta(days=10)  # Trả sau 10 ngày
    loan1.return_date = return_time
    loan1.display_loan_info()
    print(f"Đã trả sách? {loan1.is_returned()}")
    print(
        f"Thời gian mượn: {Loan.calculate_loan_duration_days(loan1.loan_date, loan1.return_date)} ngày"
    )
except (ValueError, TypeError) as e:
    print(f"Lỗi Loan 1: {e}")
print("-" * 30)


# 7. Tạo Loan chưa trả
try:
    book2_for_loan = Book.create_book(
        "The Art of Debugging", 2019, "David Lee", "978-8888888888"
    )
    borrower2_for_loan = Borrower.register_borrower("Pham Thi D", "phamd@library.net")

    print("\n--- Loan 2 (Chưa trả) ---")
    loan2 = Loan(book2_for_loan, borrower2_for_loan)
    loan2.display_loan_info()
    print(f"Đã trả sách? {loan2.is_returned()}")
    print(
        f"Thời gian mượn (chưa trả): {Loan.calculate_loan_duration_days(loan2.loan_date, loan2.return_date)}"
    )
except (ValueError, TypeError) as e:
    print(f"Lỗi Loan 2: {e}")
print("-" * 30)


# 8. Thử gán return_date không hợp lệ (ngày quá khứ)
try:
    book3_for_loan = Book.create_book(
        "Clean Code", 2008, "Robert C. Martin", "978-0132350884"
    )
    borrower3_for_loan = Borrower.register_borrower("Hoang Van E", "hoange@library.com")
    loan3 = Loan(book3_for_loan, borrower3_for_loan)
    print("\n--- Loan 3 (Thử gán ngày trả quá khứ) ---")
    invalid_return_time = loan3.loan_date - timedelta(days=1)
    loan3.return_date = invalid_return_time  # Sẽ gây lỗi
except (ValueError, TypeError) as e:
    print(f"Lỗi Loan 3 (ngày trả quá khứ): {e}")
print("-" * 30)


# 9. Thử gán return_date lần thứ hai
try:
    book4_for_loan = Book.create_book(
        "The Pragmatic Programmer", 1999, "Andrew Hunt", "978-0201616224"
    )
    borrower4_for_loan = Borrower.register_borrower("Mai Thi F", "maif@library.org")
    loan4 = Loan(book4_for_loan, borrower4_for_loan)
    print("\n--- Loan 4 (Thử gán ngày trả lần 2) ---")
    loan4.return_date = loan4.loan_date + timedelta(days=5)
    print("Ngày trả lần 1 thành công.")
    loan4.return_date = loan4.loan_date + timedelta(days=7)  # Sẽ gây lỗi
except (ValueError, TypeError) as e:
    print(f"Lỗi Loan 4 (gán lần 2): {e}")
print("-" * 30)


print("\n" + "=" * 50)
print("--- Minh họa Đa hình với LibraryItem ---")
print("=" * 50)

# Tạo danh sách các LibraryItem (bao gồm cả Book)
# Đảm bảo các đối tượng này đã được tạo thành công
library_items = []
try:
    library_items.append(
        Book.create_book("Learning Python", 2013, "Mark Lutz", "978-1449355739")
    )
    library_items.append(
        Book.create_book("Fluent Python", 2015, "Luciano Ramalho", "978-1491946008")
    )
    # Giả sử có lớp Magazine kế thừa từ LibraryItem
    # class Magazine(LibraryItem): ...
    # library_items.append(Magazine.create_magazine("National Geographic", 2024, 5))
except ValueError as e:
    print(f"Lỗi khi tạo mục thư viện cho đa hình: {e}")

if library_items:
    for item in library_items:
        print(f"\n--- Thông tin mục thư viện ---")
        item.display_info()  # Phương thức display_info sẽ hoạt động khác nhau tùy loại item
        print("-" * 25)
else:
    print("Không có mục thư viện nào để hiển thị do lỗi khởi tạo.")

print("=" * 50)
print("--- Kiểm tra hoàn tất ---")
print("=" * 50)
