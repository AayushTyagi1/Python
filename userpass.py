f=open("data.txt","a+")
for i in range(1,3):
    name=str(input("Enter name: "))
    pw=str(input("Enter password: "))
    a=hash(pw)
    f.write("%s"%(name))
    f.write("%s"%(a))
    f.write("\n")
f.close()
