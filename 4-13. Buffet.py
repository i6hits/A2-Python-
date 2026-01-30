basic_food = ('pizza', 'burger', 'pasta', 'salad', 'soup')
for food in basic_food:
     print(food)

basic_food[2] = 'steak' # This will raise an error because tuples are immutable

print("\nOriginal basic food items:")
for food in basic_food:
    print(food)

new_basic_food = ('sushi', 'ramen', 'tempura', 'salad', 'soup')
print("\nNew basic food items:")
for food in new_basic_food:
     print(food)