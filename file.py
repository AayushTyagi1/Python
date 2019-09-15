n=int(input())
i=0
f=open("file.txt","w+")
while (i< n):
    un=str(input("Username"))
    p=str(input("Password"))
    h=hash(p)
    f.write("%s" %(un))
    f.write("%s"%(h))
    i+=1
f.close()
