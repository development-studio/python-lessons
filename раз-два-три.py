a1 = int(input())
a2 = int(input())
a3 = int(input())
if a1 < a2:
    a1, a2 = a2, a1
if a2 < a3:
    a2, a3, = a3, a2
if a1 < a2:
    a1, a2 = a2, a1
print(a1)
print(a2)
print(a3)