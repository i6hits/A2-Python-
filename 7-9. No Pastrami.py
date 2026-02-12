sandwich_orders = ['Peanut butter and Jam sandwich', 'Peanut butter sandwich', 'Jam sandwich', 'pastrami sandwich', 'pastrami sandwich', 'pastrami sandwich']
finished_sandwiches = []

print('We are out of Pastrami.')
while 'pastrami sandwich' in sandwich_orders:
    sandwich_orders.remove('pastrami sandwich')
    

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()

    print(f"I made your {current_sandwich}")
    finished_sandwiches.append(current_sandwich)

print("\nThe following sandwiches have been made:")
for sandwich in finished_sandwiches:
    print(sandwich.title())