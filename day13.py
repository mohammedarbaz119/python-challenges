# 1
# numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
# negandzero = [i for i in numbers if i<=0]
# print(negandzero)


# 2
list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flatlist = [
    val for sub in list_of_lists for subsub in sub for val in subsub]
print(flatlist)
countries = [[('Finland', 'Helsinki')], [
    ('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
flatcount = [" ".join(x) for sub in countries for x in sub]

print(flatcount)
countdict = [{'country': x, "city": y} for sub in countries for (x, y) in sub]
print(countdict)
def yinter(x, y, c): return c/y
