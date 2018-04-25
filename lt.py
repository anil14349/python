from locust import Locust, task


class MyLocust(Locust):
    min_wait = 5000
    max_wait = 15000

    @task
    def my_task(self):
        print("executing task")
