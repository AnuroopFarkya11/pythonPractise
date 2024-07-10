class ClassWithDefaultConstructor:

    # Default Constructor
    def __init__(self):
        print("Hii I am default constructor")




class ClassWithParamaterizedCOnstructor:
    # Para constructor 
    def __init__(self,data):
        print("Hii I am para constructor " + data)

class ClassWithPass:
    pass
obj1 = ClassWithDefaultConstructor()
obj2 = ClassWithParamaterizedCOnstructor("Hanumanji")
