class parent:
    a="I am a"
    b="I am b"
class child(parent):
    c="I am c"
obj=parent()
print(obj.a)
obj2=child()
print(obj2.b)
print(obj2.c)