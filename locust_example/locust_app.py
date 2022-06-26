from locust import HttpUser, task


class UserBehavior(HttpUser):
    # runs one time for each user
    def on_start(self):
        self.client.get("/")

    @task(2)
    def posts(self):
        self.client.get("/posts")

    @task(1)
    def comment(self):
        data = {
            "postId": 1,
            "name": "my comment",
            "email": "test@user.test",
            "body": "Some text. Hello world!"
        }
        self.client.post("/comments", data)


class WebsiteUser(HttpUser):
    task_set = UserBehavior
    min_wait = 1000
    max_wait = 2000
