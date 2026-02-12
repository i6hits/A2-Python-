prompt = "\nWhat toppings would you like on your pizza? (Enter 'quit' to finish) "
prompt += "\nType'quit' to end the program. "

Decorating = True
while Decorating:
    message = input(prompt)

    if message == 'quit':
        Decorating = False
    else:   
        print(f"Adding {message} to your pizza.")
