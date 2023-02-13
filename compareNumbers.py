def compare_numbers(a,b):
    if type(a) == int and type(b) == int:
        if a == b:
            return "a and b are equal"
        elif a > b:
            return "a is greater than b"
        else:
            return "b is greater than a"
    else:
     return "Invalid input"
a = int(input("Enter number: "))
b = int(input("Enter another number: "))
print(compare_numbers(a,b))