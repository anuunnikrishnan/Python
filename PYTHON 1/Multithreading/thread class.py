# creating thread using thread class
from threading import *
# here we use inheritance MyThread class inherits base class Thread
class MyThread(Thread):
    def run(self):
        for i in range(10):
            print("Inside Mythread run method")
t=MyThread()
t.run()
# t.start()
# start and run are inbuilt methods in Thread class.here when we call run()
# it will check whether it will be in main class and override the same with MyThread
for i in range(10):
    print("inside main thread")
