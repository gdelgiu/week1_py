variables = [42, "42", "QUARANTABUE", 42.0, True, [42], {"42": 42}, (42,), set()]

for var in variables:
    print(var, "has a type", type(var))

#(print(x, "has a type", type(x)) for x in [42, "42", "QUARANTABUE", 42.0, True, [42], {"42": 42}, (42,), set()])