sandwich_orders = ['peanut butter and jelly', 'grilled cheese', 'turkey', 'pastrami']
finished_sandwich = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    
    print(f"I made your {current_sandwich} sandwich.")
    finished_sandwich.append(current_sandwich)
print("\nThe following sandwiches have been made:") 
for sandwich in finished_sandwich:
    print(f"- {sandwich.title()}")