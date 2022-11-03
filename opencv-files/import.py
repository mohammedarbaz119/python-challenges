n = int(input("enter a n: "))
f = 1
for i in range(2, (n//2)+1):
    if(n % i == 0):
        f = 0
    else:
        f = 1
if(f):
    print("prime")
else:
    print("not ")

a = [21, 123, 132, 312, 123, 21, 321]
