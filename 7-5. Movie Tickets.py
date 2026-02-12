prompt = "\nHow old are you?"
prompt += "\nEnter 'quit' to end the program. "

Asking = True

while Asking:
    age = input(prompt)

    if age == 'quit':
        Asking = False
    else:
        age = int(age)

        if age < 3:
            print("Your ticket is free!")
        elif age < 12:
            print("Your ticket is $10.")
        else:
            print("Your ticket is $15.")