# Exrcise with dict
import random

A = {1: 0,
     2: 0,
     3: 0,
     4: 0,
     5: 0,
     6: 0,
     }

for i in range(10):
    temp = random.randint(1, 6)
    A[temp] = A[temp] + 1
for key in A.keys():
    print(f"To {key} είχε εμφανιστεί {(A[key] / 1000000) * 100}%")
