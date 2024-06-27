# Part 1

num = int(input("Enter a number : "))
for i in range(num):
    print("* " * (i+1))
print("-------------------------------------------------------------------------------------------------------------------------")
def greet(name,msg = "Hello"):
    print(f"{msg}, {name}! Have a nice day!")

greet("Anil")
greet("Ambani","Hi")

# Part 2
print("-------------------------------------------------------------------------------------------------------------------------")
def calc_average(*nums):
    return(sum(nums)/len(nums))

print(calc_average(1,2,3,4))
print(calc_average(1,2,3,4,5,6))

print("-------------------------------------------------------------------------------------------------------------------------")
def log_message(level, message, **kwargs):
    log = f"[{level.upper()}] {message}"
    for key, value in kwargs.items():
        log += f" | {key}: {value}"
    return log


print(log_message("info", "This is an info message"))
print(log_message("warning", "This is a warning message", timestamp="2024-06-21 12:00:00"))
print(log_message("error", "This is an error message", timestamp="2024-06-21 12:05:00", user_id=12345))
print(log_message("debug", "Debugging message", user_id=67890, file="example.py", line=42))


# Part 3
print("-------------------------------------------------------------------------------------------------------------------------")
def is_even(num):
    if num%2 == 0:
        return True
    else:
        return False
    
print(is_even(2))
print(is_even(3))

print("-------------------------------------------------------------------------------------------------------------------------")
calculate_area = lambda length, width: length * width

print(calculate_area(5,2))
print(calculate_area(5,3))

