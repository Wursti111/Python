#15. Benzin-Rechner: Eingabe: Literpreis Benzin, verbrauchte Liter,
#gefahrene Kilometer. Ausgabe: Verbrauch pro 100 km, Preis
#pro 100 km, Preis der Gesamtstrecke.

print("Bitte Literpreis Eingeben")
x= input()
litpreis = float(x)
print("wieviele Liter wurden verbraucht ?")
y = input()
verbrauchte = float(y)
print("wieviele Kilometer sind Sie gefahren ?")
z = input()
kilometer = float(z)
print("Sie haben an Geld verbraten:")
print(litpreis*verbrauchte)
verb100 = (verbrauchte/kilometer)*100
verb100 = round(verb100,2)
pr100 = verb100*litpreis
pr100 = round(pr100,2)

print("Der Verbrauch lag bei " + str(verb100) + "Liter auf 100 km im Schnitt")
print("Die Kosten liegen bei " + str(pr100) + "Euro pro 100 km")

      

      
      
