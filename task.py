class Task:

    def __init__(self, title: str, description: str, priority: str , due_date: str, completed = False):
        self.title= title
        self.description= description
        self.priority= priority
        self.priority= priority
        self.due_date= due_date
        self.completed= completed

    def mark_complete(self):
        return self.completed == True
    



    def __str__(self):
        return self.title
        



    
