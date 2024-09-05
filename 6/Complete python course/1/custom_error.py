class NegativeValueError(Exception):
    """Custom exception for negative values."""
    pass
def check_positive_custom(number):
    if number < 0:
        raise NegativeValueError("Negative value error: The number cannot be negative.")
    return number

try:
    print(check_positive_custom(-5))
except NegativeValueError as e:
    print(f"Caught an exception: {e}")
