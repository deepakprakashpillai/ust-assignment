def add(x, y):
    """Add two numbers and return the result."""
    return x + y

def subtract(x, y):
    """Subtract the second number from the first and return the result."""
    return x - y

def multiply(x, y):
    """Multiply two numbers and return the result."""
    return x * y

def divide(x, y):
    """Divide the first number by the second and return the result.

    Raises:
        ValueError: If the second number (y) is zero.
    """
    if y != 0:
        return x / y
    else:
        raise ValueError("Cannot divide by zero")

def main():
    """Main function to test the module's functions."""
    print("Testing math_operations module...")
    print("Add:", add(10, 5))
    print("Subtract:", subtract(10, 5))
    print("Multiply:", multiply(10, 5))
    print("Divide:", divide(10, 5))

if __name__ == "__main__":
    main()

