import numpy as np

print("Ready to go")

# ---------- if
if 2**2 == 4:
    print("OK")


# ---------- for
for w in ('cool', 'powerful', 'readable'):
    print('Python is %s' % w)

for i in range(0, 10):
    print(i)

# ---------- while
z = 1 + 1j
while abs(z) < 100:
    z = z**2 + 1
print(z)

a = [1, 0, 2, 4]
for elt in a:
    if elt == 0:
        continue
    print(elt)

# 条件表达式 | 何为真，又何为假
one = 1
another_one = 1
if one == another_one: 
    print("one equals another_one")
if one is another_one:
    print("one and another_one are the same object to Python")
if id(one) == id(another_one):
    print("one and another_one are the same object to Python")

# int == float
if 1 == 1.0:
    print("1 equals 1.0")
    print("%s %s" % (type(1), type(1.0)))

if 1 in [1,2,3]:
    print("It's right, the list does contain 1")

if 'World' in 'Hello World':
    print("Yes, 'in' also workss for substring")

if 'one' in {'one': 1}:
    print("yes, 'in' works for dict")

# ---------- Iter
vowels = 'aeiouy'

for i in 'powerful':
    if i in vowels:
        print(i)

message = "Hello how are you"
for word in message.split():
    print(word)

words = ('cool', 'powerful', 'readable')
for i in range(0, len(words)):
    print((i, words[i]))

for index, item in enumerate(words):
    print((index, item))

d = {'a': 1, 'b': 2, 'c': 3}
for k in d:
    print((k, d[k]))
for k, v in d.items():
    print((k, v))

# dict doesn't have order, so we sort it by key to make sure the result is fixed
for k, v in sorted(d.items()):
    print((k, v))

[i**2 for i in range(4)]

# ---------- Exercise
# 计算 PI

result = 1
for i in range(1, 100000):
    result *= 4*i**2 / (4*i**2 - 1)
result *= 2
