# scope
x=4 # global variable

def func():
    global x
    x=7 # local variable
    return x

def func2():
    print(x)
print(x)
print(func())
func2()

