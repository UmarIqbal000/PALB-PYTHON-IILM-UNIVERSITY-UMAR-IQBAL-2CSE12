# We have to create one class, that will count the number of objects created

class A:
    count = 0
    
    def __init__(self):
        A.count += 1
        
obj1 = A()
obj2 = A()
obj3 = A()

print(A.count)