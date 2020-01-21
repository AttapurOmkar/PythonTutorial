def func1():
    print("function 1")
func1()

def func2(x):
    """This is doc string and this is used for writing code description"""
    return x*2

result=func2(2)
print(result)

# Arguments and keyword_Arguments
def func3(*args):
    """This function will accept 'n' number of parameters"""
    print(args)
    return (sum(args))*2

func3_Val=func3(2,3,4)
print(func3_Val)
print('Keyword Arguments')
def func4(**kwargs):
    print(kwargs)
    if 'John' in kwargs:
        print(f'My name is {kwargs["Mohsin"]}')
    else:
        print('These is no code name')

func4(Mohsin='cat',John='Has dog')