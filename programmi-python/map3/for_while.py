# ------------------------------------------------------------------------------------
# Le strutture di controllo while e for sono intercambiabili: al posto di
# una puoi usare l’altra e viceversa.
# Il for è più adatto a ripetere un blocco di codice un certo numero di volte e
#  per ogni elemento di un elenco,
# Il while si adatta meglio a situazioni in cui non si sa a priori
# quante volte verrà eseguito il ciclo.
# ------------------------------------------------------------------------------------


# ---------------------------------
# costrutto for
# ---------------------------------
print("=" * 79)
for i in range(5):
    print(i)

# ---------------------------------
# costrutto while
# ---------------------------------
print("=" * 79)
i = 0
while i < 5:
    print(i)
    i += 1  # i=i+1
