from collections import UserDict
from datetime import datetime, date
add something dawdwa dawdwada

class HandleExceptions:
    """Декоратор для обробки винятків."""
    def __call__(self, func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except ValueError as e:
                return f"Помилка: {e}"
            except KeyError as e:
                return f"Завдання не знайдено: {e}"
            except Exception as e:
                return f"Несподівана помилка: {e}"
        return wrapper

class Task:
    def __init__(self, name: str, description: str, deadline: str):
        self.name = name
        self.description = description
        try:
            self.deadline = datetime.strptime(deadline, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError("Некоректний формат дати. Використовуйте YYYY-MM-DD.")

    def __str__(self):
        return (f"Завдання: {self.name}\nОпис: {self.description}\n" 
                f"Дедлайн: {self.deadline.strftime('%Y-%m-%d')}")

class TaskManager(UserDict):
    @HandleExceptions()
    def add_task(self, task: Task) -> str:
        if task.name in self.data:
            raise ValueError("Завдання з такою назвою вже існує.")
        self.data[task.name] = task
        return f"Завдання '{task.name}' успішно додано."

    @HandleExceptions()
    def edit_task(self, name: str, new_task: Task) -> str:
        if name not in self.data:
            raise KeyError(name)
        self.data.pop(name)
        self.data[new_task.name] = new_task
        return f"Завдання '{name}' успішно змінено на '{new_task.name}'."

    @HandleExceptions()
    def delete_task(self, name: str) -> str:
        if name not in self.data:
            raise KeyError(name)
        self.data.pop(name)
        return f"Завдання '{name}' успішно видалено."

    @HandleExceptions()
    def view_task(self, name: str) -> str:
        if name not in self.data:
            raise KeyError(name)
        return str(self.data[name])

    @HandleExceptions()
    def search_tasks(self, keyword: str) -> list[Task]:
        results = [task for task in self.data.values() if keyword.lower() in task.name.lower() 
                   or keyword.lower() in task.description.lower()]
        return results

    def iterator(self, page_size: int):
        tasks = list(self.data.values())
        for i in range(0, len(tasks), page_size):
            yield tasks[i:i + page_size]

# Інтерактивна програма
if __name__ == "__main__":
    manager = TaskManager()
    while True:
        command = input("Введіть команду: ").strip().split()
        if not command:
            continue
        action = command[0]

        if action == "add" and len(command) >= 4:
            _, name, description, deadline = command[0], command[1], command[2], " ".join(command[3:])
            task = Task(name, description, deadline)
            print(manager.add_task(task))

        elif action == "edit" and len(command) >= 5:
            _, name, new_name, new_description, new_deadline = command[0], command[1], command[2], command[3], " ".join(command[4:])
            new_task = Task(new_name, new_description, new_deadline)
            print(manager.edit_task(name, new_task))

        elif action == "delete" and len(command) == 2:
            _, name = command
            print(manager.delete_task(name))

        elif action == "view" and len(command) == 2:
            _, name = command
            print(manager.view_task(name))

        elif action == "list" and len(command) == 2:
            _, page_size = command
            try:
                page_size = int(page_size)
                for page in manager.iterator(page_size):
                    print("\n--- Сторінка ---")
                    for task in page:
                        print(task)
            except ValueError:
                print("Некоректний розмір сторінки. Використовуйте число.")

        elif action == "search" and len(command) == 2:
            _, keyword = command
            results = manager.search_tasks(keyword)
            if results:
                print("\n--- Знайдені завдання ---")
                for task in results:
                    print(task)
            else:
                print("Нічого не знайдено.")

        elif action == "exit":
            print("Вихід з програми.")
            break

        else:
            print("Невідома команда. Спробуйте ще раз.")
