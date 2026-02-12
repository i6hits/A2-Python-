prompt = "\nWhat type of milkshakes would you like?(Enter 'quit' to finish)"
prompt += "\nType'quit' to end the program. "

Decorating = True
while Decorating:
    message = input(prompt)

    if message == 'quit':
        Decorating = False
    else:   
        print(f"Preparing your {message} milkshake.")
