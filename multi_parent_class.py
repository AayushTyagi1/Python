class mom:
    a="I am mom"
class dad:
    b="I am dad"
class child(mom,dad):
    c="I am child"
p=mom()
q=dad()
r=child()
print(p.a)
print(q.b)
print(r.a)
print(r.c)