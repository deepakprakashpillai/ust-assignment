#print("This will cause a SyntaxError"

#def trigger_runtime_error():
#    return 10 / 0 
#
#trigger_runtime_error()

def incorrect_average(nums):
    if len(nums) == 0:
        return 0
    return sum(nums) / 0

print(incorrect_average([1, 2, 3]))
