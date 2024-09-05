def divide_numbers(a, b):
    try:
        result = a / b
    except ZeroDivisionError as e:
        print(f"Error: {e}")
    else:
        print(f"Result: {result}")
    finally:
        print("Execution completed.")

divide_numbers(10, 2)
divide_numbers(10, 0) 
