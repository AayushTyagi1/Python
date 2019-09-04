for i in range(10):
    f=open("file.txt","a+")
    f.write("thsi is line %d\n"%(i+1))
    f.close()

