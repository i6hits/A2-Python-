dog = {'kind': 'dog',
       'owner': 'Daniel'}
cat = {'kind': 'cat',
       'owner': 'Alex'}
parrot = {'kind': 'parrot',
          'owner': 'Victor'}
pets = [dog, cat, parrot]
for pet in pets:
    print("Kind:", pet['kind'].title())
    print("Owner:", pet['owner'].title())