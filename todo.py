import datetime

class Task:
    def __init__(self, title, description, status, creation_date):
        self.title = title
        self.description = description
        self.status = status
        self.creation_date = creation_date
    
    def mark_as_done(self):
        self.status = "выполнено"
    
    def mark_as_undone(self):
        self.status = "не выполнено"
    
    def edit_description(self, new_description):
        self.description = new_description
    
    def __str__(self):
        return f"Задание: {self.title}\nОписание: {self.description}\nСтатус: {self.status}\nСоздано: {self.creation_date}"


class TaskList:
    def __init__(self):
        self.tasks = []
    
    def create_task(self, title, description, status, creation_date):
        task = Task(title, description, status, creation_date)
        self.tasks.append(task)
    
    def get_task(self, index):
        if 0 <= index(self.tasks):
            return self.tasks[index]
        else:
            return None
    
    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
    
    def get_all_tasks(self):
        return self.tasks
    
    def __len__(self):
        return len(self.tasks)



'''если честно декоратор я взял из интернета и каюсь за это '''

def log_activity(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        arguments = ", ".join([str(arg) for arg in args] + [f"{key}={val}" for key, val in kwargs.items()])
        print(f"[{timestamp}] Выполнен метод {func.__name__} с аргументами: {arguments}")
        return result
    return wrapper


def main():
    task_list = TaskList()
    
    while True:
        print("1. Создать задачу")
        print("2. Вывести список задач")
        print("3. Выход")
        
        choice = input("Выберите действие: ")
        
        if choice == "1":
            title = input("Введите название задачи: ")
            description = input("Введите описание задачи: ")
            status = "не выполнено"
            creation_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            task_list.create_task(title, description, status, creation_date)
            print("Задача создана")
        elif choice == "2":
            tasks = task_list.get_all_tasks()
            for idx, task in enumerate(tasks):
                print(f"{idx + 1}. {task.title} ({task.status})")
        elif choice == "3":
            break
  
if __name__ == "__main__":
    main()

