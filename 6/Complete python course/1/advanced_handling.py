def process_numbers(numbers):
    try:
        total = sum(numbers)
        if not numbers:
            raise ValueError("The list is empty.")
        average = total / len(numbers)
    except TypeError as e:
        print(f"Type error: {e}")
    except ValueError as e:
        print(f"Value error: {e}")
    else:
        print(f"Total: {total}, Average: {average}")
    finally:
        print("Finished processing numbers.")


process_numbers([1, 2, 3])
process_numbers([])  
process_numbers([1, 'two', 3])  
