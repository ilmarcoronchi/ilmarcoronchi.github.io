# ----------------------------------------------------
#  Operatori di Confronto + Operatori Booleani
# ----------------------------------------------------

startIntervallo = 10
endIntervallo = 35

iValue = float(input("Inserire un valore tra 10 e 35: "))

if iValue < startIntervallo or iValue > endIntervallo:
    print("Valore Esterno")
else:
    print("Valore Interno")
