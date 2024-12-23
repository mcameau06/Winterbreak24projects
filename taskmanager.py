from task import Task
from typing import List

class TaskManager():
    def __init__(self, tasks: List[Task]):
        self.tasks= []

    def add_task(self,title: str, description: str, priority: str , due_date: str, completed: bool ) -> None:

        self.tasks.append(Task(title,description, priority, due_date, completed))

    def delete_task(self, task_name):
        for task in self.tasks:
            if task_name == task:
                self.tasks.pop(task)
    
    def filter_task_by_status(self):
        a = []
        for task in self.tasks:
            if task.completed:
                a.append(task)
        return a
    



    
    
       
    


