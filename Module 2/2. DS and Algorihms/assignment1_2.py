class TaskScheduler:
    def __init__(self):
        self.tasks = {}

    def add_task(self, task, priority):
        if priority not in self.tasks:
            self.tasks[priority] = []
        self.tasks[priority].append(task)
        print(f"'{task}' added with priority {priority}.")

    def execute_tasks(self):
        if not self.tasks:
            print("No tasks to execute.")
            return
        sorted_priorities = sorted(self.tasks.keys())
        
        priorities_to_remove = []
        for priority in sorted_priorities:
            while self.tasks[priority]:
                task = self.tasks[priority].pop(0)
                print(f"Executing '{task}' with priority {priority}")
            if not self.tasks[priority]:
                priorities_to_remove.append(priority)

        for priority in priorities_to_remove:
            del self.tasks[priority]


scheduler = TaskScheduler()

scheduler.add_task("Task 1", 2)
scheduler.add_task("Task 2", 1)
scheduler.add_task("Task 3", 3)
scheduler.add_task("Task 4", 2)

scheduler.execute_tasks()

