from locust import HttpUser, task


class LoadTesting(HttpUser):
    @task
    def hello_world(self):
        """ Just for testing the application """
        self.client.post("/api/v1/hello", json={})
