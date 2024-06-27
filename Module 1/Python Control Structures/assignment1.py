#1. Accessing and Updating
my_list = [1,2,3,4]
my_tuple = (1,2,3,4)
my_dict = {'first' : 1,
           'second' : 2,
           'third' : 3,
           'forth' : 4}
my_set = {1,2,3,4}

#Accessing elements
print("my_list[0] accessed",my_list[0])
print("my_tuple[1] accessed" , my_tuple[1])
print("my_dict['third'] accessed", my_dict['third'])
print("Checking if 1 is in the set",2 in my_set)

#Modifying
my_list[2] = 33
my_dict['third'] = 33
my_set.add(5)
my_set.remove(3)

print(f"The values after updating are my_list = {my_list} , my_dict = {my_dict}, my_set = {my_set}")


#2. Extracting Subsets
print("-------------------------------------------------------------------------------------------------------------------------")

grocery_list = ["apple","orange","banana","carrot","beetroot","grapes"]

print("Fruits from the list : ", grocery_list[:3] + grocery_list[5:])

#repalcing portions from list using  slicing
grocery_list[3:5] = ['potato', 'tomato']
print(grocery_list)
#removing portions from list using slicing
grocery_list[3:5] = []
print(grocery_list)


#3. Adding and Deleting Essentials: Dynamic Data Structures
print("-------------------------------------------------------------------------------------------------------------------------")

recipes = {'sambar' : ['potato','tomato','masala','water','salt'],
           'chicken curry' : ['chicken','masala','water','salt']}

print(f"Recipee of Chicken curry is : {recipes['chicken curry']}")

#Adding new elements
recipes["omlet"] = ["egg","salt","pepper"]

#Removing elements
del recipes['chicken curry']

print(f"After editing the recipes its : {recipes}")


#4. . Looping through Collections: The for Loop Magic 
print("-------------------------------------------------------------------------------------------------------------------------")

grades = {'Akhil' : 20, 'Yadhav': 30,'Arjun' : 40,'Albert' : 50}
sum = 0
for name,grade in grades.items():
    sum += grade
print("Average grade of all studnets : ", sum/len(grades))

#5.  Membership Check: Using the in Keyword 
print("-------------------------------------------------------------------------------------------------------------------------")

message = ['h','e','l','l','o']

def guess(ch):
    if ch in message:
        print(f"{ch} is in the message")
    else:
        print(f"{ch} is not in the message")

guess('e')
guess('t')