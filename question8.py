# . Day of the Week Checker
# Write a Python program that asks the user to enter a number (1 to 7) and prints the
# corresponding day of the week. If the number is outside the 1-7 rang

def WeekChecker(day):
    match day:
        case 1:
            return "MONDAY"
        case 2:
            return "TUESDAY"
        case 3:
            return "WEDNESDAY"
        case 4:
            return "THURSDAY"
        case 5:
            return "FRIDAY"
        case 6:
            return "SATURDAY"
        case 7:
            return "SUNDAY"
        case _:
            return "Invalid day of the week"
        

day = int(input("Enter the number: \t"))
weekDay = WeekChecker(day)
print(f"The number {day} represents a \n \t {weekDay}")


