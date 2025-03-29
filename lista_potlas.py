# Listák
lista = [13, "almafa", 3.14, True, [1,2,3], 45, 12]
print(lista)

nevek = ["András", "Bence", "Cecil", "Dénes", "Elemér", "Ferenc"]
print(nevek)
print(len(nevek)) # 6
print(type(nevek)) # <class 'list'>
print(nevek[0]) # András
print(nevek[3]) # Dénes
print(nevek[len(nevek) - 1])
print(nevek[-1]) # Hátulról az első elem (Ferenc)
print(nevek[-3]) # Dénes

# A negatív indexelés mellett, intervallumos indexelést is tudunk használni
# Ennek az eredménye mindig egy lista lesz
print(nevek[2:5]) # [Cecil, Dénes, Elemér] 5. már nem lesz benne
print(nevek[2:-2]) # [Cecil, Dénes]
print(nevek[:3]) # A legelejétől a 3. elemig [András, Bence, Cecil]
print(nevek[4:]) # A 4. től a legvégéig [Elemér, Ferenc]
print(nevek[:]) # A teljes lista

print(nevek[1:5:2]) # Az 1. indextől az 5. ig 2esével menve [Bence, Dénes]
print(nevek[:4:2]) # Az elejétől a 4.ig 2 esével ['András', 'Cecil']
print(nevek[::-1]) # Megfordítja a listát

names = nevek
names[0] = "Andrew"
print("nevek:", nevek, id(nevek))
print("names:", names, id(names))

# Tapasztalat: mindkét lista megváltozott
# Ok: Amikor egy listának egy másik listát adunk meg értékül, akkor nem készül másolat a memóriában,
# hanem 2 különböző változóval fogunk ugyan arra a memóricímre hivatkozni
# Ez azt eredményezi, hogy a két lista egy és ugyan az, ha az egyiket módosítjuk, 
# akkor a másik is változni fog

nevek[0] = "András"

# Ahoz, hogy ezt a problémát elkerüljük, több megoldást is használhatunk
# Ilyenkor a memóriában is lemásolódnak az értékek
names = nevek[:]
names[0] = "Andrew"
print("nevek:", nevek, id(nevek))
print("names:", names, id(names))

# Egy másik megoldás:
names = nevek.copy()
names[0] = "Andrew"
print("nevek:", nevek, id(nevek))
print("names:", names, id(names))

del nevek[2] # A nevek listából töröljük a 2-es indexü elemet
print(nevek)

# Egy elem beszúrása egy adott indexre:
nevek.insert(2, "Csaba") # 2. indexre menjen a csaba, a 2. indextől, minden eggyel arrébb csúszik
print(nevek)
