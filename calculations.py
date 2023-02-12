def sum(a, b):
    try:
        a = int(a)
        b = int(b)
    except ValueError:
        return "Invalid input"
    message = "The sum is : "
    result = a + b
    print(message + str(result))
    if a == b:
        return "a is equal to b"
    else:
        return "a and b are not equal"
def difference(a, b):
    try:
        a = int(a)
        b = int(b)
    except ValueError:
        return "Invalid input"
    message = "The difference is : "
    result = a - b
    print(message + str(result))
    if a == b:
        return "a is equal to b"
    else:
        return "a and b are not equal"
def product(a, b):
    try:
        a = int(a)
        b = int(b)
    except ValueError:
        return "Invalid input"
    message = "The product is : "
    result = a * b
    print(message + str(result))
    if a == b:
        return "a is equal to b"
    else:
        return "a and b are not equal"


def division(a, b):
    try:
        a = int(a)
        b = int(b)
        result = a / b
    except ValueError:
        return "Invalid input"
    except ZeroDivisionError:
        return "Division by zero"
    message = "The quotient is : "
    print(message + str(result))
    if a == b:
        return "a is equal to b"
    else:
        return "a and b are not equal"
a = input("Enter number: ")
b = input("Enter another number: ")
print(sum(a, b))
print(difference(a, b))
print(product(a, b))
print(division(a, b))
