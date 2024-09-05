def check_positive(number):
    if number < 0:
        raise ValueError("Negative value error: The number cannot be negative.")
    return number

print(check_positive(10)) 
print(check_positive(-5)) 
