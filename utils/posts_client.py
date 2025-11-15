from utils.api_client import APIClient

class PostsClient(APIClient):

    ENDPOINT = "posts"

    def get_all_posts(self):
        return self.get(self.ENDPOINT)
    
    def get_posts_by_id(self, id):
        return self.get(f"{self.ENDPOINT}/{id}")
    
    def create_post(self, title, body, user_id):
        post_data = {
            "title": title,
            "body": body,
            "userId": user_id
        }
        return self.post(self.ENDPOINT, post_data)
    
    def update_post(self, post_id, **kwargs):
        return self.put(f"{self.ENDPOINT}/{post_id}", kwargs)
    
    def partial_update_post(self, post_id, **kwargs):
        return self.patch(f"{self.ENDPOINT}/{post_id}", kwargs)
    
    def delete_post(self, post_id):
        return self.delete(f"{self.ENDPOINT}/{post_id}")
    
    def get_post_comments(self, post_id):
        return self.get(f"{self.ENDPOINT}/{post_id}/comments")
