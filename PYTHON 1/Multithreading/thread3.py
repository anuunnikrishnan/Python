# implementing usage of multithreading
from threading import *
import time
def doubles(numbers):
    for n in numbers:
        time.sleep(1)
        print("doble values=",2*n)
def squares(numbers):
    for n in numbers:
        time.sleep(1)
        print("square values=",n*n)
# -------------without creating thread
# numbers=[1,2,3,4,5]
# begintime=time.time()
# doubles(numbers)
# squares(numbers)
# endtime=time.time()
# print("Total time= ",endtime-begintime)
# -------------with thread
numbers=[1,2,3,4,5]
begintime=time.time()
t1=Thread(target=doubles,args=(numbers,))
t2=Thread(target=squares,args=(numbers,))
t1.start()
t2.start()
t1.join()
t2.join()
# join method is used to allign the order of execution..t1.join means t1 will execute first otherwise main thread
# join operation is controlled by main thread
endtime=time.time()
print("Total time taken",endtime-begintime)
# by using thread we can reduce the total time first case 10 second case 5