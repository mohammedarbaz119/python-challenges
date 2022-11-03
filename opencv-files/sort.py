a = [2, 0, 2, 1, 1, 2, 0, 1, 1, 0, 0, 0, 1, 2, 1]
c0 = 0
c2 = 0
for i in range(len(a)):
    if(a[i] == 0):
        c0 += 1
    if(a[i] == 2):
        c2 += 1
for _ in range(c0):
    a.remove(0)

for _ in range(c2):
    a.remove(2)

for _ in range(c0):
    a.insert(0, 0)

for _ in range(c2):
    a.append(2)
print(a)
