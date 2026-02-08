favorite_places = {'Charles': ['paris', 'london', 'rome'],
                   'Lewis': ['new york', 'toronto'],
                   'Nobara': ['tokyo']}
for person, places in favorite_places.items():
    print(f"\n{person.title()}'s favorite places are:")
    for place in places:
        print("-", place.title())