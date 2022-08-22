# closures decorators and higher order funxtions
# level 2

from pickletools import read_uint1


countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 1


# def upperc(a):
#     return a.upper()


# uppercaselist = list(map(upperc, countries))
# print(uppercaselist)

# def sq(a):
#     return a*a


# print(list(map(sq, numbers)))


# def contains(a: str):
#     return a.find('land') != -1


# print(list(filter(contains, countries)))

# def sixletters(a: str) -> bool:
#     return len(a) > 6


# print(list(filter(sixletters, countries)))
# def upp(a: str):
#     return a.upper()


# def sevenletter(a: str):
#     return len(a) >= 7


# print(list(map(upp, filter(sevenletter, countries))))
