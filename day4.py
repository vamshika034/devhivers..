#Defining Functions in Python
def greet():
    print("Hello, welcome to Python!")

greet()

#Functions with Parameters


def add(a, b):
    result = a + b
    print("Sum =", result)

add(5, 3)


#Functions with Return Values


def multiply(a, b):
    return a * b

result = multiply(4, 5)
print("Multiplication =", result)





#Reusable Function Example

def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact = fact * i
    return fact

print("Factorial =", factorial(5))



#Prime Number Check Using Function


def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

print(is_prime(7))


# local variable


def test():
    x = 10   # local variable
    print(x)

test()

# global variable


x = 20   # global variable

def show():
    print(x)

show()





#global Keyword Example


x = 5

def change():
    global x
    x = 10

change()
print(x)


















