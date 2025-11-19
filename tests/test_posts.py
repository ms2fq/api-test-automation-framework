import pytest
from utils.posts_client import PostsClient

class TestPosts:
    @pytest.fixture(autouse=True)
    def setup_posts_client(self):
        self.client = PostsClient()

    def test_get_all_posts(self):
        response = self.client.get_all_posts()
        assert response.status_code == 200, f"Get All Posts Response Code: {response.status_code}"
        print(f"Get All Posts Response Code: {response.status_code}")
        posts = response.json()
        assert len(posts) > 0, f"Get All Posts Length Greater Than 0: {len(posts) > 0}"
        print(f"Get All Posts Length Greater Than 0: {len(posts) > 0}")
        first_post = posts[0]
        assert "userId" in first_post
        assert "title" in first_post
        assert "body" in first_post
        assert "id" in first_post
    