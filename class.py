class A:
    eyes="Black"
    age=22
    hair=""
    def feature(self):
        return 'Black eyes and age 22'
print(A)
obj=A()
print(obj.age)
print(obj.eyes)
print(obj.feature())
obj.hair="Brown"
print(obj.hair)