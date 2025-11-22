import pytest
from utils.posts_client import PostsClient
from datetime import datetime
import json

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
    
    def test_get_posts_by_id(self):
        id = 1
        response = self.client.get_posts_by_id(id)
        assert response.status_code == 200, f"Get Posts By ID Response Code: {response.status_code}"
        print(f"Get Posts By ID Response Code: {response.status_code}")
        post = response.json()
        assert "userId" in post
        assert "title" in post
        assert "body" in post
        assert "id" in post
        assert post["id"] == id, f"ID Requested: {id}, Post ID returned is: {post["id"]}"
        print(f"ID Requested: {id}, Post ID returned is: {post["id"]}")

    def test_create_post(self):
        now = datetime.now().ctime()
        title = f"Test Title {now}"
        body = f"Test Body {now}"
        user_id = 123
        response = self.client.create_post(title, body, user_id)
        assert response.status_code == 201, f"Create Post Response code: {response.status_code}"
        print(f"Create Post Response code: {response.status_code}")
        post = response.json()
        assert post["userId"] == user_id, f'User ID Expected: {user_id}, User ID Returned: {post["userId"]}'
        print(f'User ID Expected: {user_id}, User ID Returned: {post["userId"]}')
        assert post["title"] == title, f'Title Expected: {title}, Title Returned: {post["title"]}'
        print(f'Title Expected: {title}, Title Returned: {post["title"]}')
        assert post["body"] == body, f'Body Expected: {body}, Body Returned: {post["body"]}'
        print(f'Body Expected: {body}, Body Returned: {post["body"]}')

    def test_update_post(self):
        now = datetime.now().ctime()
        post_id = 1
        post_title = f"Update Title {now}"
        post_body = f"Update Body {now}"
        post_user_id = 123
        response = self.client.update_post(post_id=post_id, title=post_title, body=post_body, userId=post_user_id)
        assert response.status_code == 200, f"Update Post Status Code: {response.status_code}"
        post = response.json()
        assert post["userId"] == post_user_id, f'User ID Expected: {post_user_id}, User ID Returned: {post["userId"]}'
        print(f'User ID Expected: {post_user_id}, User ID Returned: {post["userId"]}')
        assert post["title"] == post_title, f'Title Expected: {post_title}, Title Returned: {post["title"]}'
        print(f'Title Expected: {post_title}, Title Returned: {post["title"]}')
        assert post["body"] == post_body, f'Body Expected: {post_body}, Body Returned: {post["body"]}'
        print(f'Body Expected: {post_body}, Body Returned: {post["body"]}')
        assert post["id"] == post_id, f'Post ID Expected: {post_id}, Post ID Returned: {post["id"]}'
        print(f'Post ID Expected: {post_id}, Post ID Returned: {post["id"]}')
