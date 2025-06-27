import random
import uuid
from datetime import datetime, date, timedelta


class Task:
    def __init__(self, task_id, title, description, status, created_at):
        # SỬA ĐỔI: Gọi setter để kiểm tra hợp lệ ngay từ đầu cho các thuộc tính có setter
        self._task_id = str(task_id)  # Đảm bảo ID là chuỗi
        self.title = title  # Gọi setter
        self.description = description  # Gọi setter
        self.status = status  # Gọi setter
        self._created_at = created_at  # created_at thường không thay đổi sau khi tạo

    @property
    def task_id(self):
        return self._task_id

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if (
            not isinstance(value, str) or not value.strip()
        ):  # strip() để loại bỏ khoảng trắng thừa
            raise ValueError("Title cannot be empty.")
        self._title = value

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Description cannot be empty.")
        self._description = value

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        valid_statuses = {"Pending", "In Progress", "Completed"}
        if not isinstance(value, str) or value not in valid_statuses:
            raise ValueError(f"Status must be one of {valid_statuses}.")
        self._status = value

    @property
    def created_at(self):
        return self._created_at

    def display_task_details(self):
        print(f"Task ID: {self.task_id}")  # Dùng getter
        print(f"Title: {self.title}")  # Dùng getter
        print(f"Description: {self.description}")  # Dùng getter
        print(f"Status: {self.status}")  # Dùng getter
        print(f"Created At: {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}")

    @classmethod
    def create_new_task(cls, title, description):
        task_id = uuid.uuid4()  # uuid.uuid4() tạo đối tượng UUID, nên chuyển thành str
        created_at = datetime.now()
        # Đối với lớp Task, chúng ta gọi __init__ của Task
        return cls(str(task_id), title, description, "Pending", created_at)


class TimedTask(Task):
    def __init__(
        self, task_id, title, description, status, created_at, due_date, priority
    ):
        super().__init__(task_id, title, description, status, created_at)
        # SỬA ĐỔI: Gọi setter để kiểm tra hợp lệ ngay từ đầu cho due_date và priority
        self.due_date = due_date
        self.priority = priority

    @property
    def due_date(self):
        return self._due_date

    @due_date.setter
    def due_date(self, value):
        if not isinstance(value, (datetime, date)):
            raise ValueError("Due date must be a datetime or date object.")
        # SỬA ĐỔI: Kiểm tra ngày trong tương lai hoặc hôm nay
        if value.date() < date.today():
            raise ValueError("Due date cannot be in the past.")
        self._due_date = value

    @property
    def priority(self):
        return self._priority

    @priority.setter
    def priority(self, value):
        valid_priorities = {"Low", "Medium", "High"}
        if not isinstance(value, str) or value not in valid_priorities:
            raise ValueError(f"Priority must be one of {valid_priorities}.")
        self._priority = value

    @staticmethod
    def is_overdue(task_due_date):
        """Kiểm tra xem nhiệm vụ đã quá hạn chưa."""
        if not isinstance(task_due_date, (datetime, date)):
            # Nên raise lỗi hoặc trả về một giá trị rõ ràng thay vì True/False không rõ ràng cho invalid input
            raise TypeError("task_due_date must be a datetime or date object.")

        # SỬA ĐỔI: So sánh ngày tháng. Nếu ngày đến hạn nhỏ hơn ngày hiện tại, thì quá hạn.
        return task_due_date.date() < date.today()

    def display_task_details(self):
        super().display_task_details()
        # SỬA ĐỔI: Định dạng ngày tháng và dùng getter
        print(f"Due Date: {self.due_date.strftime('%Y-%m-%d')}")
        print(f"Priority: {self.priority}")

    @classmethod
    def create_new_task(cls, title, description, due_date, priority):
        # KHÔNG GỌI super().create_new_task ở đây nếu bạn muốn tạo TimedTask đầy đủ
        # Thay vào đó, tạo các thuộc tính của lớp cha và sau đó gọi __init__ của cls (TimedTask)
        task_id = str(uuid.uuid4())  # ID duy nhất
        created_at = datetime.now()

        # SỬA ĐỔI CHÍNH: Trực tiếp gọi constructor của lớp con (cls là TimedTask)
        # và truyền TẤT CẢ các đối số cần thiết, bao gồm cả của lớp cha và của lớp con.
        return cls(
            task_id, title, description, "Pending", created_at, due_date, priority
        )


# --- Thực hiện và kiểm tra ---

print("--- Kiểm tra lớp Task ---")
try:
    task_basic = Task.create_new_task("Mua sữa", "Mua 2 lít sữa tươi không đường.")
    task_basic.display_task_details()
    print("-" * 30)

    print("Cập nhật Task:")
    task_basic.title = "Mua sữa và bánh mì"
    task_basic.status = "In Progress"
    task_basic.display_task_details()
    print("-" * 30)

    print("Thử cập nhật trạng thái không hợp lệ:")
    try:
        task_basic.status = "Hoàn Thành"
    except ValueError as e:
        print(f"Lỗi khi cập nhật status: {e}")
    print("-" * 30)

    print("Thử cập nhật tiêu đề rỗng:")
    try:
        task_basic.title = ""
    except ValueError as e:
        print(f"Lỗi khi cập nhật title: {e}")
    print("-" * 30)

except ValueError as e:
    print(f"Lỗi Task cơ bản: {e}")

print("\n--- Kiểm tra lớp TimedTask ---")
try:
    future_date = datetime.now() + timedelta(days=7)
    timed_task = TimedTask.create_new_task(
        "Nộp báo cáo", "Hoàn thành báo cáo quý III.", future_date, "High"
    )
    timed_task.display_task_details()
    print("-" * 30)

    print("Cập nhật TimedTask:")
    timed_task.due_date = datetime.now() + timedelta(days=14)
    timed_task.priority = "Medium"
    timed_task.display_task_details()
    print("-" * 30)

    print("Kiểm tra quá hạn:")
    # Tạo một nhiệm vụ đã quá hạn để kiểm tra is_overdue
    overdue_task_date = date.today() - timedelta(days=1)
    overdue_task = TimedTask.create_new_task(
        "Nhiệm vụ quá hạn", "Đây là nhiệm vụ đã quá hạn.", overdue_task_date, "Low"
    )
    print(
        f"Nhiệm vụ '{timed_task.title}' quá hạn? {TimedTask.is_overdue(timed_task.due_date)}"
    )
    print(
        f"Nhiệm vụ '{overdue_task.title}' quá hạn? {TimedTask.is_overdue(overdue_task.due_date)}"
    )
    print("-" * 30)

    print("Thử cập nhật ngày quá hạn (quá khứ):")
    try:
        timed_task.due_date = datetime.now() - timedelta(days=1)
    except ValueError as e:
        print(f"Lỗi khi cập nhật due_date: {e}")
    print("-" * 30)

    print("Thử cập nhật độ ưu tiên không hợp lệ:")
    try:
        timed_task.priority = "Urgent"
    except ValueError as e:
        print(f"Lỗi khi cập nhật priority: {e}")
    print("-" * 30)

except ValueError as e:
    print(f"Lỗi TimedTask: {e}")
except Exception as e:
    print(f"Lỗi không mong muốn trong TimedTask: {e}")


print("\n--- Minh họa Đa hình ---")
all_tasks = [
    Task.create_new_task("Đi chợ", "Mua rau và thịt"),
    TimedTask.create_new_task(
        "Họp dự án", "Chuẩn bị slide", datetime.now() + timedelta(days=2), "High"
    ),
    Task.create_new_task("Đọc sách", "Chương 5 và 6"),
    TimedTask.create_new_task(
        "Viết blog", "Về Python OOP", datetime.now() + timedelta(days=5), "Medium"
    ),
]

for task in all_tasks:
    task.display_task_details()
    print("=" * 40)
