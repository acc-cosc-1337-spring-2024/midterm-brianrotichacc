import question_b as b

print("Celsius | Fahrenheit")
print("--------------------")
for celsius in range(0,21):
    fahrenheit = b.get_fahrenheit(celsius)
    print(f"{celsius:^7} | {fahrenheit:^11.2f}")