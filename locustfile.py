import random
import time
from locust import HttpUser, task ,between

from csvReader import CsvRead

# api https://api.zippopotam.us/us/33162

class HelloWorldUser(HttpUser):
    
    @task
    def readcsv(self):
        test_data = CsvRead("temp.csv").read()
        print(test_data)
        url="/us/"+str(test_data['pincode'])
        self.client.get(url)


    @task
    def randomtest(self):   #this function check api is working or not on pincode numbers between 33160 to 33169 every time it take different pincode
        num=random.randint(33160,33169)
        print(num)
        self.client.get(f"/us/{num}",name='pincode')

    # @task
    # def method2(self):
    #     for item_id in range(10):
    #         self.client.get(f"/item?id={item_id}", name="/item")

    # In the method2 task we load 10 different URLs by using a variable query parameter. In order to not get 10 
    # separate entries in Locust’s statistics - since the stats is grouped on the URL - we use the name parameter to group 
    # all those requests under an entry named "/item" instead.
        