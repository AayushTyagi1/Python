dict={0:'zero',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine'}
n=int(input("Enter number :"))
l=[]
while n!=0:
    l.append(n%10)
    n =int( n / 10)
l.reverse()
print(l)
for i in l:
    print(dict[i],end=' ')
