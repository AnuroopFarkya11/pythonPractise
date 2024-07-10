# Defining a function 
def myFunc():
    print("Hello From myfunc")


# Paasing arguments to a function 

def func1(data):
    print("Data", data)
    print(type(data))

func1(1)

# Arbitrary Arguments 

def func2(*data):
    for x in data:
        print("Data : ", x)


func2("a","b")

data = 11
 
# Prove pass by reference 
def func3(data):
    data = 77
    print(data)


func3(data)
print(data)
