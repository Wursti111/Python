import random
random.seed()

a = random.randint(1,10)
b = random.randint(1,10)
c = a+b
print("Die Rechenaufgabe: ", a , "+", b)

print("Bitte eine Zahl eingeben")
z = input()
zahl = int(z)

print("Ihre Eingabe", z)
print("Das Ergebnis:", c)
