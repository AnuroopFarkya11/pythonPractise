class ClassA:
    def __init__(self):
        print("I am Class A")



class ClassB:
    def __init__(self):
        print("I am class B")



class childClass(ClassA,ClassB):
    pass


obj = childClass()