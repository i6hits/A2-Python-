invites = ["Luffy", "Zoro", "Nami"]
NotComing = "Zoro"
for invite in invites:
 messages = ["HELLO! " + invite + ", You are invited to join me for dinner. " "There will be meat, booze and tangerines for dessert."for invite in invites]
for message in messages:
 print(message)
print("\n")
print("Unfortunately, " + NotComing + " can't make it to dinner.\n")
del invites[1]    
invites.insert(1,"Sanji")
for invite in invites:
     messages = ["HELLO! " + invite + ", You are invited to join me for dinner. " "There will be meat, booze and tangerines for dessert."for invite in invites]
for message in messages:
 print(message)