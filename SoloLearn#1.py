# Dictionary Functions

data = {
    'Singapore': 1,
    'Ireland': 6,
    'United Kingdom': 7,
    'Germany': 27,
    'Armenia': 34,
    'United States': 17,
    'Canada': 9,
    'Italy': 74
}

name = input()
i = 0
for key in data:
    if key == name:
        i += 1

if i == 1:
    print(data.get(name))
else:
    print("Not found")