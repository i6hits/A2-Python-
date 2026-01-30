name = 'Alice'
print("Equality: name == 'Alice' ->", name == 'Alice')
print("Inequality: name != 'Bob' ->", name != 'Bob')
print("\nCase-insensitive: name.lower() == 'alice' ->", name.lower() == 'alice')
print("Case-sensitive: name == 'alice' ->", name == 'alice')

number = 10
print("\nEquality: number == 10 ->", number == 10)
print("Inequality: number != 5 ->", number != 5)
print("Greater than: number > 5 ->", number > 5)
print("Less than: number < 5 ->", number < 5)
print("Greater than or equal: number >= 10 ->", number >= 10)
print("Less than or equal: number <= 5 ->", number <= 5)

print("\nAnd: number > 5 and number < 15 ->", number > 5 and number < 15)
print("Or: number < 5 or number > 15 ->", number < 5 or number > 15)

fruits = ['apple', 'banana', 'orange']
print("\nIn list: 'apple' in fruits ->", 'apple' in fruits)
print("Not in list: 'grape' in fruits ->", 'grape' in fruits)

print("\nNot in: 'grape' not in fruits ->", 'grape' not in fruits)