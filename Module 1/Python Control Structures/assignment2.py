#1. Operator Olympics: Mastering Calculations and Logic
print("--------------------------------------------------------------------------------------------------------------------------")

def calc_area(a,b):
    return a*b

def calc_volume(a,b,c):
    return a*b*c

area = calc_area(5,2)
volume = calc_volume(5,2,2)

print(f"Total calculated area = {area}, volume = {volume}")

if area%2 == 0:
    print("Area is even")
else:
    print("Area is odd")

if area%2 == 0 and volume%2 == 0:
    print("Both area and volume are even")
else:
    print("Both area and volume are odd")

#2. Conditional Crossroads: if, elif, and else
print("--------------------------------------------------------------------------------------------------------------------------")

age = int(input("Enter your age : "))

if age < 18:
    print("You still have  alot to study")
elif age < 35:
    print("Exciting adventures await!")
else:
    print("Wisdom and experience are your strengths!")

#3. Nesting for Complexity: Conditional Mazes
print("--------------------------------------------------------------------------------------------------------------------------")

color = input("Enter favorite color :  ")

if age < 18:
    if color == 'red':
        print("You will do good in studies")
    else:
        print("Good luck with studies")
elif age < 35:
    if color == 'red':
        print("You will do good in job")
    else:
        print("Good luck with job")
else:
    if color == 'red':
        print("You will do good in life")
    else:
        print("Good luck with life")