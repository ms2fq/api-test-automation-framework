import pytest
from utils.todos_client import ToDoClient
from datetime import datetime

class TestToDos:
    @pytest.fixture(autouse=True)
    def setup_todo_client(self):
        self.client = ToDoClient()

    def test_get_all_todos(self):
        response = self.client.get_all_todos()
        assert response.status_code == 200, f"Get All ToDos Response Code: {response.status_code}"
        print(f"Get All ToDos Response Code: {response.status_code}")
        todos = response.json()
        assert len(todos) > 0, f"Get All ToDos Length Greater Than 0: {len(todos) > 0}"
        print(f"Get All ToDos Length Greater Than 0: {len(todos) > 0}")
        first_todo = todos[0]
        assert "userId" in first_todo
        assert "title" in first_todo
        assert "completed" in first_todo
        assert "id" in first_todo
    
    def test_get_todos_by_id_valid(self):
        id = 1
        response = self.client.get_todos_by_id(id)
        assert response.status_code == 200, f"Get ToDos By ID Response Code: {response.status_code}"
        print(f"Get ToDos By ID Response Code: {response.status_code}")
        todo = response.json()
        assert "userId" in todo
        assert "title" in todo
        assert "completed" in todo
        assert "id" in todo
        assert todo["id"] == id, f"ID Requested: {id}, ToDo ID returned is: {todo["id"]}"
        print(f"ID Requested: {id}, ToDo ID returned is: {todo["id"]}")

    def test_get_todos_by_id_invalid_negative_id(self):
        id = -1
        response = self.client.get_todos_by_id(id)
        assert response.status_code == 404, f"Get ToDos By ID Response Code: {response.status_code}"
        print(f"Get ToDos By ID Response Code: {response.status_code}")

    def test_get_todos_by_id_invalid_string_id(self):
        id = "abcd"
        response = self.client.get_todos_by_id(id)
        assert response.status_code == 404, f"Get ToDos By ID Response Code: {response.status_code}"
        print(f"Get ToDos By ID Response Code: {response.status_code}")

    def test_create_todo_valid(self):
        now = datetime.now().ctime()
        title = f"Test Title {now}"
        user_id = 123
        response = self.client.create_todo(user_id, title)
        assert response.status_code == 201, f"Create ToDo Response code: {response.status_code}"
        print(f"Create ToDo Response code: {response.status_code}")
        todo = response.json()
        assert todo["userId"] == user_id, f'User ID Expected: {user_id}, User ID Returned: {todo["userId"]}'
        print(f'User ID Expected: {user_id}, User ID Returned: {todo["userId"]}')
        assert todo["title"] == title, f'Title Expected: {title}, Title Returned: {todo["title"]}'
        print(f'Title Expected: {title}, Title Returned: {todo["title"]}')
        assert todo["completed"] == False, f'Completed Expected: {False}, Completed Returned: {todo["completed"]}'
        print(f'Completed Expected: {False}, Completed Returned: {todo["completed"]}')

    def test_update_todo(self):
        now = datetime.now().ctime()
        todo_id = 1
        todo_title = f"Update Title {now}"
        todo_completed = True
        todo_user_id = 123
        response = self.client.update_todo(todo_id=todo_id, title=todo_title, completed=todo_completed, userId=todo_user_id)
        assert response.status_code == 200, f"Update ToDo Status Code: {response.status_code}"
        print(f"Update ToDo Status Code: {response.status_code}")
        todo = response.json()
        assert todo["userId"] == todo_user_id, f'User ID Expected: {todo_user_id}, User ID Returned: {todo["userId"]}'
        print(f'User ID Expected: {todo_user_id}, User ID Returned: {todo["userId"]}')
        assert todo["title"] == todo_title, f'Title Expected: {todo_title}, Title Returned: {todo["title"]}'
        print(f'Title Expected: {todo_title}, Title Returned: {todo["title"]}')
        assert todo["completed"] == todo_completed, f'Completed Expected: {todo_completed}, Completed Returned: {todo["completed"]}'
        print(f'Completed Expected: {todo_completed}, Completed Returned: {todo["completed"]}')
        assert todo["id"] == todo_id, f'ToDo ID Expected: {todo_id}, ToDo ID Returned: {todo["id"]}'
        print(f'ToDo ID Expected: {todo_id}, ToDo ID Returned: {todo["id"]}')

    def test_partial_update_todo(self):
        now = datetime.now().ctime()
        todo_id = 1
        todo_title = f"Partial Update Title {now}"
        todo_user_id = 123
        response = self.client.update_todo(todo_id=todo_id, title=todo_title, userId=todo_user_id)
        assert response.status_code == 200, f"Partial Update ToDo Status Code: {response.status_code}"
        print(f"Partial Update ToDo Status Code: {response.status_code}")
        todo = response.json()
        assert todo["userId"] == todo_user_id, f'User ID Expected: {todo_user_id}, User ID Returned: {todo["userId"]}'
        print(f'User ID Expected: {todo_user_id}, User ID Returned: {todo["userId"]}')
        assert todo["title"] == todo_title, f'Title Expected: {todo_title}, Title Returned: {todo["title"]}'
        print(f'Title Expected: {todo_title}, Title Returned: {todo["title"]}')
        assert todo["id"] == todo_id, f'ToDo ID Expected: {todo_id}, ToDo ID Returned: {todo["id"]}'
        print(f'ToDo ID Expected: {todo_id}, ToDo ID Returned: {todo["id"]}')
    
    def test_delete_todo_valid_id(self):
        todo_id = 1
        response = self.client.delete_todo(todo_id)
        assert response.status_code == 200, f"Delete ToDo Status Code: {response.status_code}"
        print(f"Delete ToDo Status Code: {response.status_code}")

    def test_mark_todo_complete(self):
        todo_id = 1
        response = self.client.mark_todo_complete(todo_id)
        assert response.status_code == 200, f"Mark todo complete status code: {response.status_code}"
        print(f"Mark todo complete status code: {response.status_code}")
        
    def test_mark_todo_incomplete(self):
        todo_id = 1
        response = self.client.mark_todo_incomplete(todo_id)
        assert response.status_code == 200, f"Mark todo incomplete status code: {response.status_code}"
        print(f"Mark todo incomplete status code: {response.status_code}")
