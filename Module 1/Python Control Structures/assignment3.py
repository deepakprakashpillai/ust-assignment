my_list = list(range(10))

print(f"my_list = {my_list} and its length = {len(my_list)} and datatype of 1st element is {type(my_list[0])}")

print(f"First element as a string : {str(my_list[0])}")

val = "1"
print("1 converted to integer : ",int(val))

#2. Function Factory: Building Your Own Tools 
print("-------------------------------------------------------------------------------------------------------------------------")

def add(a,b):
    return a+b

print(add(2,3))

#3. Recursive Rollercoaster: Exploring Recursive Functions 
print("-------------------------------------------------------------------------------------------------------------------------")

def fact(num):
    if num == 1:
        return num
    else:
        return num * fact(num-1)
    
print(f"factorial of {4} = {fact(4)}")