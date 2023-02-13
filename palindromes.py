def palindrome_check(s):
    if type(s) == str:
        reverse = s[::-1]
        if s == reverse:
            return s + " is a palindrome"
        else:
            return s + " is not a palindrome"
    else:
        return "Invalid input"


s = str(input("Enter word: "))
print(palindrome_check(s))
