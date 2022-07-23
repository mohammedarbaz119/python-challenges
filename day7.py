# set = {}
# set1 = set()
from pyrsistent import discard


it_companies = {'Facebook', 'Google', 'Microsoft',
                'Apple', 'IBM', 'Oracle', 'Amazon'}
a = {19, 22, 24, 20, 25, 26}
b = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
print(len(it_companies))
it_companies.add("twitter")
it_companies.update(["newcomapy", "mycpomapny", "new comaonty"])
it_companies.pop()
print(it_companies)
c = a.union(b)
print(c)
print(a.intersection(b))
print(a.issubset(b))
print(a.isdisjoint(b))
print(a.symmetric_difference(b))

del a
del b
agess = set(age)
print(len(age) > len(agess))
a = "I am a teacher and I love to inspire and teach people."
ab = set(a.split(' '))
print(len(ab))
