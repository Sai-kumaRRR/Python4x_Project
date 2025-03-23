# Triangle classifier:

# write a program that classifies a triangle based on its sde lengths ,
# given three input values representing the lengths of the sides,
# determine if the triangle is equilateral (all side are equal)
# isosceles (exactly wo sides are equal) , or  scalene ( no sides are equal.
# use if else statement  to  classify the triangle .

def classify_triangle(a , b , c ):
    if a == b ==c :
        return "equilateral"
    elif a == b or b == c or a ==c :
         return "Isosceles"

    side1 = float(input("enter the first side :"))
    side2 = float(input("enter the second side :"))
    side3 = float(input("enter the third side :"))


    result = classify_triangle(side1 , side2 , side3)
    print(f"the triangle is classified as:{result}")