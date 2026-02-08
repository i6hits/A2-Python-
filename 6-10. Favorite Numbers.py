favourite_numbers = {'Feyi': [67],
                     'Sam': [7],
                     'Toyosi': [8],
                     'Daniel': [69],
                     'Banjo': [420]}
for name, numbers in favourite_numbers.items():
    print(f"\n{name}'s favourite numbers are:")
    for number in numbers:
        print(number)