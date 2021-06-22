# ----------------------------------------------------------
# List: Elenco eterogeneo, ordinato per posizione
# ----------------------------------------------------------
import sys

a = ["Roma", "Oslo", "Lisbona", "Reykjavik", 234, 'Roma']
print(type(a))
print(a)
# accedo agli elementi per posizione
print(a[0])
# Aggiungo un elemento in coda
a.append(34.67)
print(a[-1])

# Lista di numeri
print("=" * 79)
a = [1, 5, 733, 56]
print(max(a))
print(min(a))
# la funzione modifica direttamente la lista
a.reverse()
print(a)
# la funzione modifica direttamente la lista
a.sort()
print(a)

# ---------------------------------
# Tuple: Lista IMMUTAVOLE
# ---------------------------------
print("=" * 79)
a = (1, 5, 733, 56)
print(type(a))
print(a)
print(a[0])
print(a[-1])
print(max(a))

# ----------------------------------------------
# Set: Insieme => no ordine, no duplicati
# ----------------------------------------------
print("=" * 79)
a = {1, 5, 733, 56, 5}
print(type(a))
print(a)

# --------------------------------------------
# Dictionary, Map, Array Associativo
# --------------------------------------------
print("=" * 79)
a = {"f": "Flash", "t": "Tempesta", "h": "Hulk"}
print(type(a))
print(a)
# Elenco chiavi e Valori
print(a.keys())
print(a.values())

# get Value from keys
print(a["t"])

# Aggiunta/Cancellazione Elementi
a["s"] = "Superman"
del a["t"]
try:
    print(a["t"])
except KeyError:
    print("Chiave non presente nel Dictionary")
except:
    print("*" * 79)
    print("Error: ", sys.exc_info()[0], "occurred.")
    print("*" * 79)
