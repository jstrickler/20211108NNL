x = 100   # GLOBAL variable

def spam():
    m = 42  # LOCAL variable
    print("hello")
#    x = 50  # LOCAL variable   BAD IDEA

spam()

print("in main: x is", x)
print(ZeroDivisionError)
# print("in main: m is", m)  # INVALID

#  local  nonlocal global builtin

def foo(color):
    number = 42  # color and number are local to foo()

    def bar():  # closure
        print("color is", color)  # color is nonlocal to bar()
        print("number is", number)  # number is nonlocal to bar()

    return bar

b = foo("red")
b()

