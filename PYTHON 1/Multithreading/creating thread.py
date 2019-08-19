from threading import *
def display():
    for i in range(10):
        print("child thread executing")
    print(current_thread().getName())
t=Thread(target=display())
# creating object t of thread class and job is display()
t.start()
for i in range(1,10):
    print("main thread is working")
print(current_thread().getName())
# here main thread and child thread exists.thread scheduler assigns work to main thread and child thread