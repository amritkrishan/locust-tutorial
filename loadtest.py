import locust
import requests

class BaseTaskSet(locust.TaskSet):
    """A simple base class to be used for initializing stuff
    """

    def on_start(self):
        # Called everytime when a simulated user starts executing TaskSet class
        self.headers = {
            'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3"
        }
        

class DefeatThanosTaskSequence(BaseTaskSet):
    """An example TaskSequence containing tasks to be executed sequentially
       Could be used to simulate a user behaviour or journey
    """

    @locust.seq_task(1)
    def call_captain_america(self):
        # First task
         response = self.client.get("/search?q=captain+america", headers=self.headers)

    @locust.seq_task(2)
    def call_ironman(self):
        # Second task
        response = self.client.get("/search?q=ironman", headers=self.headers)

    @locust.seq_task(3)
    def call_thor(self):
        # Third task
        response = self.client.get("/search?q=thor", headers=self.headers)

    @locust.seq_task(4)
    @locust.task(15)
    def call_hulk(self):
        # This last task will be executed 15 times
        # because hulk won't come out
        response = self.client.get("/search?q=hulk", headers=self.headers)


class DefeatThanosLocust(locust.HttpLocust):
    task_set = DefeatThanosTaskSequence

