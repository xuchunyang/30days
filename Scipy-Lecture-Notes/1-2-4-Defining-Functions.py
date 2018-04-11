# ---------- Define

def test():
    print("a test")

test()

# ---------- Return

def disk_area(radius):
    return 3.14 * radius**2

disk_area(1.5)

def double_it(x):
    return x * 2

double_it(2)

# ---------- Change arguments

def try_to_modify(x, y, z):
    x = 23
    y.append(42)
    z = [99]                    # new reference
    print(x)
    print(y)
    print(z)

a = 77
b = [99]
c = [28]
try_to_modify(a, b, c)

# ---------- Global variables
x = 5
def addx(y):
    return x + y

assert addx(1) == 6

# function can't change global variable
def setx(y):
    x = y
    print('x is', x)

setx(10)
assert x == 5

# but declaring it with global can
def setx2(y):
    global x
    x = y
    print("x is", x)

setx2(10); assert x == 10

# ---------- Varaible args
def variable_args(*args, **kargs):
    print(args)                 # tuple
    print(kargs)                # dict

variable_args('one', 'two', x=1, y=2, z=3)

# ---------- Docstring

def hi(name='Python'):
    """Say hi"""
    print("Hi, ", name)

assert hi.__doc__== 'Say hi'

# ---------- Functions as object
va = variable_args
va(1, one=1, two=2)

# ---------- Methods 是指 Object 上的 Function
assert 'hello'.upper() == str.upper('hello')

# ---------- Exercise

def fib(n):
    """打印前 N 个 Fibonaci 数列."""
    if not n > 0: return
    print(0)
    a, b = 0, 1
    while n > 0:
        print(b)
        a, b = b, a+b
        n -= 1

def quicksort(array):
    """快排"""
    less = []
    pivots = []
    greater = []
    if len(array) < 2:
        return array
    else:
        pivot = array.pop()
        for x in array:
            if x < pivot:
                less.append(x)
            else:
                greater.append(x)
        pivots.append(pivot)
        return quicksort(less) + pivots + quicksort(greater)
