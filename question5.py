# 5. Simple Age Checker
# Write a Python program that asks the user for their age and tells them whether they are a minor
# (under 18), an adult (18-65), or a senior (over 65).

def myAgeChecker(age):
    if 0 <= age < 18:
        return "a Minor"
    elif 18<= age <= 65:
        return " an Adult, start looking for a wife"
    elif age > 65:
        return "a Senior"
    else:
        return "Invalid age"
    
age = int(input("Enter your age: \t"))
ageInfo = myAgeChecker(age)
print("\t",  f'A person of {age}yrs old is  {ageInfo}')

