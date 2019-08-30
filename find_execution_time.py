import time
start=time.time()
def table():
    num=int(input("Enter number:"))
    for i in range(1,11):
        print(num*i)
table()
end=time.time()
tm=end-start
print("The execution time is :",tm)