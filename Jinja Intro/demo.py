n = 1234321
dummy = str(n)[::-1]

if int(dummy) == n:
    print("This is a palindrome")
else:
    print("NOT")
