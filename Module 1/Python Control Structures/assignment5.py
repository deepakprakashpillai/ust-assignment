# 3. Data Type Detectives

person = {
    "name": "John Doe",
    "age": 30,
    "is_innocent": True,
}

expected_types = {
    "name": str,
    "age": int,
    "is_innocent": bool
}


all_clues_correct = True
for key in person:
    if not isinstance(person[key], expected_types[key]):
        print("Dataype does not match")
        all_clues_correct = False

if all_clues_correct:
    print("Datatypes match")

#4. Mad Libs with a Twist
# with the help of chatgpt for the story
print("-----------------------------------------------------------------------------------------------------------------------------------")


print("Welcome to the Fantasy Mad Libs Game!")

creature = input("Enter a magical creature: ")
item = input("Enter an enchanted item: ")
place = input("Enter a fantasy place: ")
name = input("Enter the name of an adventurer: ")
print("\nChoose the story's ending:")
print("1. A happy ending")
print("2. A lesson learned")
print("3. An ongoing adventure")
ending_choice = input("Enter the number of your choice: ")

story = (
    f"Once upon a time in a land far, far away, there was a magical creature called {creature}. "
    f"This creature had a special enchanted item: a {item}. "
    f"One day, while wandering through the {place}, the creature met a brave adventurer named {name}. "
    f"{name} had been searching for the {item} for many years. Together, they embarked on an epic journey. "
)

if ending_choice == "1":
    story += f"In the end, {name} and the {creature} used the {item} to bring peace to the entire kingdom. They were celebrated as heroes for all time."
elif ending_choice == "2":
    story += f"In the end, {name} discovered that the true magic of the {item} was the friendships formed along the way. {name} and the {creature} remained best friends, exploring new lands together forever."
elif ending_choice == "3":
    story += f"In the end, the {item} turned out to be cursed, and {name} and the {creature} had to find a way to break the curse. Their adventure continued as they faced new challenges."
else:
    story += "However, the story ended unexpectedly because the choice was unclear."

print("\nHere's your story:\n")
print(story)


# 5 : Operator Olympics
print("-----------------------------------------------------------------------------------------------------------------------------------")

num1 = 1
num2 = 2

print(f"Bitwise AND: {num1} & {num2} = {num1 & num2}")
print(f"Bitwise OR: {num1} | {num2} = {num1 | num2}")
print(f"Bitwise XOR: {num1} ^ {num2} = {num1 ^ num2}")



# 5 : Data Type Zoo
print("-----------------------------------------------------------------------------------------------------------------------------------")

num1, num2 = 10, 5
float1, float2 = 3.5, 2.0
str1, str2 = "Hello", "World"
bool1, bool2 = True, False
list1, list2 = [1, 2, 3], [4, 5, 6]
dict1 = {"name": "Ashique", "age": 20}

print(f"Integer Addition: {num1} + {num2} = {num1 + num2}")
print(f"Float Multiplication: {float1} * {float2} = {float1 * float2}")
print(f"String Concatenation: {str1} + {str2} = {str1 + str2}")
print(f"Boolean AND Operation: {bool1} and {bool2} = {bool1 and bool2}")
print(f"List Concatenation: {list1} + {list2} = {list1 + list2}")
new_key = "gender"
new_value = "M"
dict1[new_key] = new_value
print(f"Updated Dictionary: {dict1}")