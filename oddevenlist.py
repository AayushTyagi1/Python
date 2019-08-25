# To separate odd and even numbers from a list of numbers into a new list
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
le=[]
lo=[]
for i in l:
    if(i%2==0):
        le.append(i)
    else:
        lo.append(i)
print(le)
print(lo)