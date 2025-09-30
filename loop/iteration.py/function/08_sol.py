def print_kwargs(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}: {value}")



print_kwargs(name="Shaktimann",power="Lazer")
print_kwargs(name="Shaktimann")
print_kwargs(name="shaktimann", power="lazer",enemy="kaaaal")