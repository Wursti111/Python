import fractions
import math

x = 3.141592653589793
print("Zahl:", x)

# als Bruch
b3 = fractions.Fraction(x)
print("Fraction:", b3)

#approximiert
b4 = b3.limit_denominator(10000)
print("Approx auf Nenner = 100:", b4   )

#Genauigkeit
wert = b4.numerator/b4.denominator
print("Wert: ", wert)
print(" rel. Fehler:", abs((x-wert)/x))

print("""Diese Zeichenkette steht
      in mehreren
      Zeilen""")
      
