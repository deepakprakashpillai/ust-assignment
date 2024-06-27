fruits = ["apple", "banana", "orange"]
numbers = [1, 2, 3, 4]

print("Fruits List:", fruits)
print("Data type of fruits:", type(fruits))
print("Numbers List:", numbers)
print("Data type of numbers:", type(numbers))

print("First fruit:", fruits[0])
print("Last number:", numbers[-1])

numbers[2] = 5
numbers.append(6)
print("Modified Numbers List:", numbers)

numbers.insert(3, 4)
print("After inserting 4 at index 3:", numbers)

colors = ["red", "green", "blue", "yellow"]
print("Initial Colors List:", colors)

colors.remove("green")
print("After removing 'green':", colors)

popped_color = colors.pop(1)
print("List after pop operation:", colors)

del colors[-1]
print("After deleting last element:", colors)
