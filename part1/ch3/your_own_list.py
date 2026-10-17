motorcycles = ["Ducati", "BMW", "Moto Guzzi"]
messages = ["is super sexy", "is very pragamtic", "is a mix of both"]

for motorcycle, message in zip(motorcycles, messages):
    print(f"{motorcycle.title()} {message}.")