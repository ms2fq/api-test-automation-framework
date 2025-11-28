import pytest
from utils.users_client import UsersClient
from datetime import datetime

class TestUsers:
    @pytest.fixture(autouse=True)
    def setup_users_client(self):
        self.client = UsersClient()

    def test_get_all_users(self):
        response = self.client.get_all_users()
        assert response.status_code == 200, f"Get All Users Response Code: {response.status_code}"
        print(f"Get All Users Response Code: {response.status_code}")
        users = response.json()
        assert len(users) > 0, f"Get All Users Length Greater Than 0: {len(users) > 0}"
        print(f"Get All Users Length Greater Than 0: {len(users) > 0}")
        first_user = users[0]
        assert "id" in first_user
        assert "name" in first_user
        assert "username" in first_user
        assert "email" in first_user
        assert "address" in first_user
        address = first_user["address"]
        assert "street" in address
        assert "suite" in address
        assert "city" in address
        assert "zipcode" in address
        assert "geo" in address
        geo = address["geo"]
        assert "lat" in geo
        assert "lng" in geo
        assert "phone" in first_user
        assert "website" in first_user
        assert "company" in first_user
        company = first_user["company"]
        assert "name" in company
        assert "catchPhrase" in company
        assert "bs" in company
    
    def test_get_users_by_id_valid(self):
        id = 1
        response = self.client.get_users_by_id(id)
        assert response.status_code == 200, f"Get Users By ID Response Code: {response.status_code}"
        print(f"Get Users By ID Response Code: {response.status_code}")
        user = response.json()
        assert "id" in user
        assert user["id"] == id, f"ID Requested: {id}, Username returned is: {user["id"]}"
        print(f"ID Requested: {id}, Username returned is: {user["id"]}")
        assert "name" in user
        assert "username" in user
        assert "email" in user
        assert "address" in user
        address = user["address"]
        assert "street" in address
        assert "suite" in address
        assert "city" in address
        assert "zipcode" in address
        assert "geo" in address
        geo = address["geo"]
        assert "lat" in geo
        assert "lng" in geo
        assert "phone" in user
        assert "website" in user
        assert "company" in user
        company = user["company"]
        assert "name" in company
        assert "catchPhrase" in company
        assert "bs" in company

    def test_get_users_by_id_invalid_negative_id(self):
        id = -1
        response = self.client.get_users_by_id(id)
        assert response.status_code == 404, f"Get Users By ID Response Code: {response.status_code}"
        print(f"Get Users By ID Response Code: {response.status_code}")

    def test_get_users_by_id_invalid_string_id(self):
        id = "abcd"
        response = self.client.get_users_by_id(id)
        assert response.status_code == 404, f"Get Users By ID Response Code: {response.status_code}"
        print(f"Get Users By ID Response Code: {response.status_code}")

    def test_create_user_valid(self):
        now = datetime.now().ctime()
        name = f"Test Name {now}"
        username = f"Test Username{now}"
        email = "abcd123@def.com"
        response = self.client.create_user(name, username, email)
        assert response.status_code == 201, f"Create User Response code: {response.status_code}"
        print(f"Create User Response code: {response.status_code}")
        user = response.json()
        assert user["username"] == username, f'Username Expected: {username}, Username Returned: {user["username"]}'
        print(f'Username Expected: {username}, Username Returned: {user["username"]}')
        assert user["name"] == name, f'Name Expected: {name}, Name Returned: {user["name"]}'
        print(f'Name Expected: {name}, Name Returned: {user["name"]}')
        assert user["email"] == email, f'Email Expected: {email}, Email Returned: {user["email"]}'
        print(f'Email Expected: {email}, Email Returned: {user["email"]}')

    def test_update_user(self):
        now = datetime.now().ctime()
        name = f"Update Name {now}"
        username = f"Update Name {now}"
        email = "a12bc@def.com"
        response = self.client.update_user(user_id=1, username=username, email=email, name=name)
        assert response.status_code == 200, f"Update User Status Code: {response.status_code}"
        print(f"Update User Status Code: {response.status_code}")
        user = response.json()
        assert user["username"] == username, f'Username Expected: {username}, Username Returned: {user["username"]}'
        print(f'Username Expected: {username}, Username Returned: {user["username"]}')
        assert user["name"] == name, f'Name Expected: {name}, Name Returned: {user["name"]}'
        print(f'Name Expected: {name}, Name Returned: {user["name"]}')
        assert user["email"] == email, f'Email Expected: {email}, Email Returned: {user["email"]}'
        print(f'Email Expected: {email}, Email Returned: {user["email"]}')

    def test_partial_update_user(self):
        username = "Partial Update Username"
        name = f"Partial Update Name"
        response = self.client.update_user(user_id=1, username=username, name=name)
        assert response.status_code == 200, f"Partial Update User Status Code: {response.status_code}"
        print(f"Partial Update User Status Code: {response.status_code}")
        user = response.json()
        assert user["username"] == username, f'Username Expected: {username}, Username Returned: {user["username"]}'
        print(f'Username Expected: {username}, Username Returned: {user["username"]}')
        assert user["name"] == name, f'Name Expected: {name}, Name Returned: {user["name"]}'
        print(f'Name Expected: {name}, Name Returned: {user["name"]}')
    
    def test_delete_user_valid_id(self):
        user_id = 1
        response = self.client.delete_user(user_id)
        assert response.status_code == 200, f"Delete User Status Code: {response.status_code}"
        print(f"Delete User Status Code: {response.status_code}")

    def test_get_user_posts(self):
        user_id = 1
        response = self.client.get_user_posts(user_id)
        assert response.status_code == 200, f"Get user posts status code: {response.status_code}"
        print(f"Get user posts status code: {response.status_code}")
        posts = response.json()
        assert len(posts) > 0, f"Posts Returned Length Greater Than 0: {len(posts) > 0}"
        print(f"Posts Returned Length Greater Than 0: {len(posts) > 0}")
        first_post = posts[0]
        assert "userId" in first_post
        assert "title" in first_post
        assert "body" in first_post
        assert "id" in first_post
        
    def test_get_user_todos(self):
        user_id = 1
        response = self.client.get_user_todos(user_id)
        assert response.status_code == 200, f"Get user todos status code: {response.status_code}"
        print(f"Get user toods status code: {response.status_code}")
        todos = response.json()
        assert len(todos) > 0, f"ToDos Returned Length Greater Than 0: {len(todos) > 0}"
        print(f"ToDos Returned Length Greater Than 0: {len(todos) > 0}")
        first_todo = todos[0]
        assert "userId" in first_todo
        assert "title" in first_todo
        assert "completed" in first_todo
        assert "id" in first_todo
