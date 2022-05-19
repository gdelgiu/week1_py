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

if not argv[1] in states:
    print("Unknown state")
    exit()

for state in states:
    if state == argv[1]:
        for location in capital_cities:
            if states[state] == location:
                print(capital_cities[location])
                exit()