print("--------------------------Question 1---------------------------")

def add(a,b):
    sum = a+b
    return sum

def sub(a,b):
    diff = a-b
    return diff

print(add(1,2))
print(sub(3,4))
print("--------------------------Question 2---------------------------")

def factorial(num):
    if num == 1 or num == 0:
        return 1
    else:
        return num * factorial(num - 1)

print(factorial(5))
print("--------------------------Question 3---------------------------")

def fun(type,a,b):
    value=0
    if type =='add':
        value = a+b
    elif type =='sub':
        value = a-b
    elif type == 'mul':
        value = a*b
    else:
        print("enter correct method")

    return value

print(fun('add',1,2))
print(fun('mul',5,6))

print("--------------------------Question 4---------------------------")

def fibbonaci(num):
    a,b = 0,1
    if num == 1:
        print(a)
    else:
        print(a)
        print(b)
        for i in range(2,num):
            c = a + b
            a = b
            b = c
            print(c)
print("fibbonaci for 5")
fibbonaci(5)
print("fibbonaci for 7")
fibbonaci(7)

print("--------------------------Question 5---------------------------")


def pascal_triangle(num):
    for i in range(num):

        for k in range(num - 1, i, -1):
            print(end=" ")

        for k in range(i + 1):
            val = int(factorial(i) / (factorial(k) * factorial(i - k)))
            print(val, end=" ")
        print()


pascal_triangle(5)
pascal_triangle(6)


