class Employee:
    """Базовый класс сотрудника."""

    def init(self, name: str, employee_id: str, salary: float):
        self._name = name
        self._employee_id = employee_id
        self._salary = salary
        self._bonus = 0.0

    @property
    def name(self) -> str:
        return self._name

    @property
    def employee_id(self) -> str:
        return self._employee_id

    @property
    def salary(self) -> float:
        return self._salary

    @salary.setter
    def salary(self, value: float) -> None:
        if value <= 0:
            raise ValueError("Зарплата должна быть положительной")
        self._salary = value

    @property
    def bonus(self) -> float:
        return self._bonus

    @bonus.setter
    def bonus(self, value: float) -> None:
        if value < 0:
            raise ValueError("Бонус не может быть отрицательным")
        self._bonus = value

    def calculate_total_compensation(self) -> float:
        """Рассчитать общую компенсацию (зарплата + бонус)."""
        return self._salary + self._bonus

    def work(self) -> str:
        """Выполнять работу."""
        return f"{self._name} выполняет свои обязанности"

    def str(self) -> str:
        return f"Сотрудник: {self._name} (ID: {self._employee_id})"

    def repr(self) -> str:
        return f"Employee(name={self._name!r}, employee_id={self._employee_id!r}, salary={self._salary})"


class Manager(Employee):
    """Класс менеджера."""

    def init(self, name: str, employee_id: str, salary: float, team_size: int = 0):
        super().init(name, employee_id, salary)
        self._team_size = team_size
        self._department = "Общий"

    @property
    def team_size(self) -> int:
        return self._team_size

    @team_size.setter
    def team_size(self, value: int) -> None:
        if value < 0:
            raise ValueError("Размер команды не может быть отрицательным")
        self._team_size = value

    @property
    def department(self) -> str:
        return self._department

    @department.setter
    def department(self, value: str) -> None:
        if not value or not isinstance(value, str):
            raise ValueError("Название отдела должно быть непустой строкой")
        self._department = value

    def work(self) -> str:
        """Перегруженный метод для менеджера.

        Причина перегрузки: Менеджеры не просто выполняют работу,
        а также управляют командой и координируют процессы.
        """
        return f"{self._name} управляет командой из {self._team_size} человек в отделе {self._department}"

    def calculate_total_compensation(self) -> float:
        """Перегруженный метод расчета компенсации для менеджера.

        Причина перегрузки: Менеджеры получают дополнительный бонус за управление командой.
        """
        management_bonus = self._team_size * 1000
        return super().calculate_total_compensation() + management_bonus

    def hold_meeting(self) -> str:
        """Провести собрание."""
        return f"{self._name} проводит собрание в отделе {self._department}"

    def str(self) -> str:
        return f"Менеджер: {self._name}, отдел: {self._department}, команда: {self._team_size} чел."

    def repr(self) -> str:
        return f"Manager(name={self._name!r}, employee_id={self._employee_id!r}, salary={self._salary}, team_size={self._team_size})"


class Developer(Employee):
    """Класс разработчика."""

    VALID_LANGUAGES = ["Python", "Java", "JavaScript", "C++", "C#", "Ruby", "Go"]

    def init(self, name: str, employee_id: str, salary: float, programming_language: str = "Python"):
        super().init(name, employee_id, salary)
        Наталия, [09.03.2026 23: 07]
        if programming_language not in self.VALID_LANGUAGES:
            raise ValueError(f"Язык должен быть одним из: {self.VALID_LANGUAGES}")
        self._programming_language = programming_language
        self._projects = []

    @property
    def programming_language(self) -> str:
        return self._programming_language

    @programming_language.setter
    def programming_language(self, value: str) -> None:
        if value not in self.VALID_LANGUAGES:
            raise ValueError(f"Язык должен быть одним из: {self.VALID_LANGUAGES}")
        self._programming_language = value

    @property
    def projects(self) -> list:
        return self._projects.copy()

    def add_project(self, project_name: str) -> None:
        """Добавить проект."""
        if project_name and isinstance(project_name, str):
            self._projects.append(project_name)

    def work(self) -> str:
        """Перегруженный метод для разработчика.

        Причина перегрузки: Разработчики пишут код, а не просто выполняют общую работу.
        """
        project_text = f" над проектами: {', '.join(self._projects)}" if self._projects else ""
        return f"{self._name} пишет код на {self._programming_language}{project_text}"

    def calculate_total_compensation(self) -> float:
        """Перегруженный метод расчета компенсации для разработчика.

        Причина перегрузки: Разработчики получают бонус за каждый завершенный проект.
        """
        project_bonus = len(self._projects) * 5000
        return super().calculate_total_compensation() + project_bonus

    def code_review(self) -> str:
        """Провести ревью кода."""
        return f"{self._name} проводит ревью кода на {self._programming_language}"

    def str(self) -> str:
        return f"Разработчик: {self._name}, язык: {self._programming_language}, проектов: {len(self._projects)}"

    def repr(self) -> str:
        return f"Developer(name={self._name!r}, employee_id={self._employee_id!r}, salary={self._salary}, programming_language={self._programming_language!r})"


class Intern(Employee):
    """Класс стажера."""

    def init(self, name: str, employee_id: str, salary: float = 30000, mentor: str = None):
        super().init(name, employee_id, salary)
        self._mentor = mentor
        self._tasks_completed = 0

    @property
    def mentor(self) -> str:
        return self._mentor

    @mentor.setter
    def mentor(self, value: str) -> None:
        self._mentor = value

    @property
    def tasks_completed(self) -> int:
        return self._tasks_completed

    def complete_task(self) -> None:
        """Завершить задачу."""
        self._tasks_completed += 1

    def work(self) -> str:
        """Перегруженный метод для стажера.

        Причина перегрузки: Стажеры учатся и выполняют простые задачи под руководством.
        """
        mentor_info = f" под руководством {self._mentor}" if self._mentor else ""
        return f"{self._name} выполняет задачи стажера{mentor_info}. Выполнено задач: {self._tasks_completed}"

    def calculate_total_compensation(self) -> float:
        """Перегруженный метод расчета компенсации для стажера.

        Причина перегрузки: У стажеров фиксированная стипендия, бонусы не начисляются.
        """
        return self._salary  # Стажеры не получают бонусов

    def str(self) -> str:
        mentor_info = f", ментор: {self._mentor}" if self._mentor else ""
        return f"Стажер: {self._name}, задач выполнено: {self._tasks_completed}{mentor_info}"

    def repr(self) -> str:
        return f"Intern(name={self._name!r}, employee_id={self._employee_id!r}, salary={self._salary}, mentor={self._mentor!r})"


Наталия, [09.03.2026 23: 07]
if name == "main":
    emp = Employee("Иван Петров", "E001", 50000)
    emp.bonus = 5000
    print(emp)
    print(emp.work())
    print(f"Компенсация: {emp.calculate_total_compensation()}")
    print(repr(emp))

    print("\n" + "-" * 50 + "\n")

    manager = Manager("Анна Смирнова", "M001", 80000, team_size=5)
    manager.department = "Разработка"
    manager.bonus = 10000
    print(manager)
    print(manager.work())
    print(f"Компенсация: {manager.calculate_total_compensation()}")
    print(manager.hold_meeting())
    print(repr(manager))

    print("\n" + "-" * 50 + "\n")

    dev = Developer("Петр Сидоров", "D001", 70000, "Python")
    dev.add_project("CRM System")
    dev.add_project("Mobile App")
    dev.bonus = 8000
    print(dev)
    print(dev.work())
    print(f"Компенсация: {dev.calculate_total_compensation()}")
    print(dev.code_review())
    print(repr(dev))

    print("\n" + "-" * 50 + "\n")

    intern = Intern("Мария Иванова", "I001", mentor="Анна Смирнова")
    intern.complete_task()
    intern.complete_task()
    intern.complete_task()
    print(intern)
    print(intern.work())
    print(f"Компенсация: {intern.calculate_total_compensation()}")
    print(repr(intern))
`