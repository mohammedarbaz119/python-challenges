# 1
# def sum(a, b):
#     print(a+b)


# sum(10, 20)
from audioop import reverse
from cmath import pi
import math
from queue import Empty


# def area(r):
#     return pi*r*r


# print(area(10))


# def sum(*a):
#     s = 0
#     if(all(type(x) == int for x in a)):
#         print("cool")
#     for x in a:
#         if(type(x) != int):
#             return "not cool"
#         else:
#             s += x

#     return s


# print(sum(1, 2, 3, 4))


# def printl(l):
#     for x in l:
#         print(x)


# printl([1, 23, 4])

# def reversel(l):
#     for x in range(len(l)-1, -1, -1):
#         print(l[x])


# reversel([1, 2, 32, 4])

# def capitalize(l):
#     for x in l:
#         print(x.upper())

# def addit(l, c):
#     l.append(c)
#     print(l)


# addit([1, 2, 3, 4], 5)

# def remit(l, c):
#     l.remove(c)
#     print(l)


# remit([1, 2, 3, 4], 3)

# def sumofno(n):
#     s = 0
#     for i in range(0, n+1):
#         s += i
#     print(s)


# sumofno(100)

# def sumofodd(n):
#     s = 0
#     for i in range(0, n+1):
#         if(i % 2 != 0):
#             s += i
#     print(s)


# sumofodd(100)


# def sumofeven(n):
#     s = 0
#     for i in range(0, n+1):
#         if(i % 2 == 0):
#             s += i
#     print(s)


# sumofeven(100)

# level 2

# def evenandodds(n):
#     e = 0
#     o = 0
#     for i in range(0, n + 1):
#         if(i % 2 == 0):
#             e += 1
#         else:
#             o += 1
#     print(f"no forr evens {e}")
#     print(f"no of odds {o}")


# evenandodds(1010)

# def fact(n):
#     s = 1
#     for i in range(1, n+1):
#         s *= i
#     print(s)


# fact(6)

# def isempty(n):
#     if(not n):
#         return True
#     else:
#         return False


# print(isempty([1, 2]))

# def prime(n):
#     for i in range(2, round(math.sqrt(n))):
#         if(n % i == 0):
#             return False
#     return True


# print(prime(22))

# def isunique(n):
#     return len(set(n)) == len(n)


# print(isunique([1, 23, 3, 4, 4]))

# def checktype(n, typee):
#     return all(type(x) == typee for x in n)


# print(checktype([1, 2, 3, 4], int))

# def validvar(n):
#     return n.isidentifier()


# print(validvar("-truew"))
import day10
a = day10.country


# def most10(a):
#     a.sort(key=lambda a: a["population"], reverse=True)
#     return a[0:10]


# print(most10(a))
