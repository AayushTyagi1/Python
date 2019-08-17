n=int(input("enter number:"))
s=str("*")
for i in range(1,n):
    j=1
    while(j<=n-i):
        print(" ",end="")
        j=j+1
    print(s)
    s=s+"**"
