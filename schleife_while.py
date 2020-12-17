import random
random.seed()
summe = 0
while summe < 300            :
    zzahl = random.randint(1,8)
    summe = summe + zzahl
    print("Zahl: ", zzahl, "Zwischensumme: ", summe)
print ("Ende")        
