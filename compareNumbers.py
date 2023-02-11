def compare_numbers(a,b):
    try:
        a = int(a)
        b = int(b)
    except ValueError:
        return "Invalid input"
    if a == b:
        return "a and b are equal"
    elif a > b:
        return "a is greater than b"
    else:
        return "b is greater than a"
a = input("Enter number: ")
b = input("Enter another number: ")
print(compare_numbers(a,b))