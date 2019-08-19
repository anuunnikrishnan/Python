# here only main thread is executing
from threading import *
def display():
    for i in range(10):
        print(("child thread executing"))
    print(current_thread().getName())
for i in range(1,10):
    print("main thread executing")
print(current_thread().getName())
display()