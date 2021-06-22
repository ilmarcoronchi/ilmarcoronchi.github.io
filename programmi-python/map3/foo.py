# built-in function
from dateutil.utils import *

print('Hello World!!!')

# ---------------------------------
# Data Types
# ---------------------------------
print("=" * 29 + " DATA TYPES "+"=" * 29)
a = 10
print(type(a))
a = 10.0
print(type(a))
a = "Sarah"
print(type(a))
a = True
print(type(a))
a = today()
print(type(a))
print(a)

# ---------------------------------
# espressioni
# ---------------------------------
print("=" * 29 + " ESPRESSIONI "+"=" * 29)
a = 8 + 9
print(a)
print(type(a))

a = 8.0 + 9.0
print(a)
print(type(a))


a = 10 > 9
print(a)
print(type(a))



# ---------------------------------
# costrutto if-else
# ---------------------------------
print("=" * 29 + " COSTRUTTO IF-ELSE "+"=" * 29)
n = 10
if n > 10:
    print("n e' > di 10")
else:
    print("n e' <= di 10")

# ---------------------------------
# costrutto if-elif-else
# ---------------------------------
print("=" * 29 + " COSTRUTTO IF-ELIF-ELSE "+"=" * 29)
n = 10
if n > 10:
    print("n e' > di 10")
elif n < 10:
    print("n e' < di 10")
else:
    print("n e' = 10")

# ---------------------------------
# iterate over list
# ---------------------------------
print("=" * 29 + " ITERATE OVER LIST "+"=" * 29)
listaAmici = ["Carlo", "Andrea", "Barbara"]
for amico in listaAmici:
    print(amico.upper())

# ---------------------------------
# List Comprehensions
# ---------------------------------
print("=" * 29 + " LIST COMPREHENSIONS (I) "+"=" * 29)
foo = [1, 5, 89]
bar = [x * 2 for x in foo]
print(bar)

# ---------------------------------
# List Comprehensions
# ---------------------------------
print("=" * 29 + " LIST COMPREHENSIONS (II) "+"=" * 29)
bar = [x for x in listaAmici if x.endswith("a")]
print(bar)
