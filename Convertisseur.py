'''
Introduction aux fonctions avec un convertisseur universel
'''

# Convertir des C° en Fahrenheit
def celcius_vers_fahrenheit(celcius):
    return (celcius * 1.8) + 32

# Convertir des kms en miles
def km_vers_miles(km):
    return km * 0.621371


# Tests pour celcius_vers_fahrenheit
if celcius_vers_fahrenheit(0) == 68:
    print("Test OK !")
elif celcius_vers_fahrenheit(20) == 68:
    print("Test OK !")
else:
    print("Test raté !")

# Tests pour km_vers_miles 
if round(km_vers_miles(1), 2) == 0.68:
     print("Test OK !")
elif round(km_vers_miles(5), 2) == 3.11:
    print("Test OK !")
else:
    print("Test raté !")
