# try:
#     name = input("enter your name: ")
#     yearborn = input("enter age: ")
#     age = 2022-yearborn
# except Exception as e:
#     print(e)
# finally:
#     print("i always run")


# unpacking tuples or spreading
# def sum_of_five_nums(a, b, c, d, e):
#     return a + b + c + d + e


# lst = [1, 2, 3, 4, 5]
# print(sum_of_five_nums(*lst))  # 15

# countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
# fin, sw, nor, *rest = countries
# print(fin, sw, nor, rest)   # Finland Sweden Norway ['Denmark', 'Iceland']
# numbers = [1, 2, 3, 4, 5, 6, 7]
# one, *middle, last = numbers
# print(one, middle, last)  # 1 [2, 3, 4, 5, 6] 7

# first, *last = numbers

# print(first, *last)

names = ['Finland', 'Sweden', 'Norway',
         'Denmark', 'Iceland', 'Estonia', 'Russia']
*nordic_countries, es, ru = names
print(nordic_countries, es, ru)
