from locust import HttpLocust, TaskSet,task
from random import randint

#web接口测试
class UserBehavior(TaskSet):
    @task
    def user_sign(self):
        number=randint(1,3001)
        phone=1355555555+number
        str_phone=str(phone)
        self.client.post("/api/user_sign/",data={"eid":"1","phone":"str_phone"})

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 0
    max_wait = 0