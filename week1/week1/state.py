from sys import argv

if len(argv) > 2 or len(argv) < 2:
    exit()

states = {
"Oregon" : "OR",
"Alabama" : "AL",
"New Jersey": "NJ",
"Colorado" : "CO"
}
capital_cities = {
"OR": "Salem",
"AL": "Montgomery",
"NJ": "Trenton",
"CO": "Denver"
}

if not argv[1] in capital_cities.values():
    print("Unknown capital city")

for loc_1, city in capital_cities.items():
    if city == argv[1]:
        for state, loc_2 in states.items():
            if loc_1 == loc_2:
                print(state)
                exit(0)

