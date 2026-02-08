Kaushik = {'first_name': 'Kaushik',
           'last_name': 'Charodath Murukadason',
           'age': 18,
           'city': 'Berlin'}
Toyosi = {'first_name': 'Toyosi',
          'last_name': 'Somoye',
          'age': 17,
          'city': 'Ontario'}
Feyi = {'first_name': 'Feyi',
        'last_name': 'Oduwa',
        'age': 17,
        'city': 'Los Santos'}
people = [Kaushik, Toyosi, Feyi]
for person in people:
    print("\nFirst name:", person['first_name'])
    print("Last name:", person['last_name'])
    print("Age:", person['age'])
    print("City:", person['city'])