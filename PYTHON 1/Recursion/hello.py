import sys
print(sys.getrecursionlimit())
sys.setrecursionlimit(1000)
def greet():
    print("hello")
    greet()
greet()
# greet() function is calling repeatedly within the same function