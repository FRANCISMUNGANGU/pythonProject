def calculator(c,d):
    if type(c) == int and type(d) == int:
        sum = c + d
        difference = c - d
        product = c * d
        if d == 0:
            return "Division by zero not allowed"
        else:
            division = c / d
            if c == d:
                return "c and d are equal\nsum: {}\ndifference: {}\nproduct: {}\ndivision: {}".format(sum,difference,product,division)
            else:
                return "c and d are not equal\nsum: {}\ndifference: {}\nproduct: {}\ndivision: {}".format(sum,difference,product,division)

    else:
        return "Invalid input"
c = int(input("Enter number c : "))
d = int(input("Enter number d : "))
print(calculator(c,d))