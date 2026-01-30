current_users = ['john', 'emma', 'alex', 'sarah', 'mike']
new_users = ['Emma', 'MIKE', 'david', 'lisa', 'peter']
current_users_lower = [user.lower() for user in current_users]
for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"Sorry, '{new_user}' is already taken. Please enter a new username.")
    else:
        print(f"'{new_user}' is available!")