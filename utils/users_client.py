from utils.api_client import APIClient

class UsersClient(APIClient):

    ENDPOINT = "users"

    def get_all_users(self):
        return self.get(self.ENDPOINT)
    
    def get_users_by_id(self, id):
        return self.get(f"{self.ENDPOINT}/{id}")
    
    def create_user(self, name, username, email, **kwargs):
        user_data = {
            "name": name,
            "username": username,
            "email": email,
            **kwargs
        }
        return self.post(self.ENDPOINT, user_data)
    
    def update_user(self, user_id, **kwargs):
        return self.put(f"{self.ENDPOINT}/{user_id}", kwargs)
    
    def partial_update_user(self, user_id, **kwargs):
        return self.patch(f"{self.ENDPOINT}/{user_id}", kwargs)
    
    def delete_user(self, user_id):
        return self.delete(f"{self.ENDPOINT}/{user_id}")
    
    def get_user_posts(self, user_id):
        return self.get(f"{self.ENDPOINT}/{user_id}/posts")
    
    def get_user_todos(self, user_id):
        return self.get(f"{self.ENDPOINT}/{user_id}/todos")
    