import utilities.math_operations as math_ops
from utilities.string_operations.string_ops import reverse_string, capitalize_string


result_add = math_ops.add(2, 3)
print(f"Addition: {result_add}")

result_reverse = reverse_string("hello")
result_capitalize = capitalize_string("hello")
print(f"Reversed: {result_reverse}")
print(f"Capitalized: {result_capitalize}")
