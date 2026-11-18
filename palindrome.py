# Palindrome checker (ignores letter case)
value = input("Enter a string: ").strip()
if value.lower() == value.lower()[::-1]:
    print("The given string is a Palindrome")
else:
    print("The given string is Not a Palindrome")
