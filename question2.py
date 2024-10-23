# Odd or Even Checker
# Write a Python program that asks the user for a number and then prints whether the number is
# odd or even.


userNumber = int(input("Enter any number \t"))
print("\t The number entered was", userNumber)


if(userNumber%2 == 0):
    print('\t', userNumber,  ' is an Even Number')
else:
    print('\t', userNumber, ' an Odd Number')