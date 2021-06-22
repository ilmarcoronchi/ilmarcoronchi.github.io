# built-in function
from dateutil.utils import *

print('Hello World!!!')

# ---------------------------------
# Data Types
# ---------------------------------
print("=" * 79)
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
# costrutto if-else
# ---------------------------------
print("=" * 79)
n = 10
if n > 10:
    print("n e' > di 10")
else:
    print("n e' <= di 10")

# ---------------------------------
# costrutto if-elif-else
# ---------------------------------
print("=" * 79)
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
print("=" * 79)
listaAmici = ["Carlo", "Andrea", "Barbara"]
for amico in listaAmici:
    print(amico.upper())

# ---------------------------------
# List Comprehensions
# ---------------------------------
print("=" * 79)
foo = [1, 5, 89]
bar = [x * 2 for x in foo]
print(bar)

# ---------------------------------
# List Comprehensions
# ---------------------------------
print("=" * 79)
bar = [x for x in listaAmici if x.endswith("a")]
print(bar)
