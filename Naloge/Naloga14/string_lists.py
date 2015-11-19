# Ask the user for a string and print out whether this string is a palindrome or not.

word = str(raw_input("Enter any string you want: "))
reversed_word = word[::-1]

if reversed_word == word:
    print(" YES! The string you entered is palindrome")
else:
    print("NOPE! this string is not palindrome")