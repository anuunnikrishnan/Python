# creating thread without extending thread class
from threading import *
import time
# time module is used to check multithreading.time.sleep
class Test:
    def m1(self):
        for i in range(10):
            time.sleep(5)
            print("inside Test")
obj=Test()
t=Thread(target=obj.m1)
# t=Thread(target=obj.m1())
# here in this case first thread goes waiting state..multithreading is not working
t.start()
for i in range(10):
    print("inside Main Thread")