from utils.api_client import APIClient

class ToDoClient(APIClient):

    ENDPOINT = "todos"

    def get_all_todos(self):
        return self.get(self.ENDPOINT)
    
    def get_todos_by_id(self, id):
        return self.get(f"{self.ENDPOINT}/{id}")
    
    def create_todo(self, user_id, title, completed=False):
        todo_data = {
            "userId": user_id,
            "title": title,
            "completed": completed
        }
        return self.post(self.ENDPOINT, todo_data)
    
    def update_todo(self, todo_id, **kwargs):
        return self.put(f"{self.ENDPOINT}/{todo_id}", kwargs)
    
    def partial_update_todo(self, todo_id, **kwargs):
        return self.patch(f"{self.ENDPOINT}/{todo_id}", kwargs)
    
    def delete_todo(self, todo_id):
        return self.delete(f"{self.ENDPOINT}/{todo_id}")
    
    def mark_todo_complete(self, todo_id):
        return self.patch(f'{self.ENDPOINT}/{todo_id}', {"completed": True})
    
    def mark_todo_incomplete(self, todo_id):
        return self.patch(f'{self.ENDPOINT}/{todo_id}', {"completed": False})
    