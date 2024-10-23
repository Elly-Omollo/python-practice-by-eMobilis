# Triangle Type Checker
# Write a Python program that takes the lengths of three sides of a triangle as input and
# determines if the triangle is:
# ● Equilateral (all sides are equal),
# ● Isosceles (two sides are equal), or
# ● Scalene (all sides are different).

def TriangleChecker(side1, side2, side3):
    if side1 == side2 == side3:
        return "Equalateral Triangle (all sides are equal)"
    elif (side1 == side2 ) or (side1 == side3) or (side2 == side3):
        return "Isosceles Triangle (two sides are equal)"
    else:
        return "Scalene Triangle (all sides are different)"


side1 = int(input("Enter the lengthh of the first side: \t"))
side2 = int(input("Enter the lengthh of the second side: \t"))
side3 = int(input("Enter the lengthh of the third side: \t"))

TypeOfTriangle = TriangleChecker(side1, side2, side3)
print(f"\n \t The triangle of sides   {side1}cm , {side2}cm and {side3}cm is: \n \t {TypeOfTriangle} \n")