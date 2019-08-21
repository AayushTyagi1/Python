class parent:
    a="I am a"
    b="I am b"
class child(parent):
    b="I am no more b"
p=parent()
q=child()
print(p.b)
print(q.b)