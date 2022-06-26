from locust import HttpUser, task


class GetBooks(HttpUser):
    @task(2)
    def books(self):
        self.client.get("")


class SubmitBooks(HttpUser):
    @task(1)
    def books_post(self):
        data = {
            "book_input": "Anna Karenina",
            "book_author": "Tolstoy",
        }
        self.post = self.client.post("", data)
