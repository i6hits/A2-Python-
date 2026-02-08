cities = {'lagos': {'country': 'nigeria',
                    'population': 'over 15 million',
                    'fact': 'It is one of the fastest growing cities in Africa'},
        'london': {'country': 'united kingdom',
                   'population': 'about 9 million',
                   'fact': 'It has the oldest underground railway in the world'},
        'tokyo': {'country': 'japan',
                  'population': 'about 14 million',
                  'fact': 'It is the largest metropolitan area in the world'}}
for city, info in cities.items():
    print(f"\nCity: {city.title()}")
    print("Country:", info['country'].title())
    print("Population:", info['population'])
    print("Fact:", info['fact'])