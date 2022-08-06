# 1
# a = int(input("what ur age: "))
# if(a > 18):
#     print("good to drive")
# else:
#     print(f"you cant drive you need to wait {18-a} years to drive")

# 2
# my_age = 19
# a = int(input("what ur age: "))
# if(my_age > a):
#     print(f"you are {my_age-a} years younger than me ")
# else:
#     print(f"you ar {a-my_age} years older than mes")

# 3
# a = int(input("enter a : "))
# b = int(input("enter b : "))
# if(a > b):
#     print(f"{a} is grater then {b}")
# else:
#     print(f"{b} is graten than {a}")

# level 2

# 1
# a = int(input("enter a : "))
# if(a >= 90):
#     print("a")
# elif(a <= 89 and a >= 80):
#     print("B")
# elif(a >= 79 and a <= 70):
#     print("c")
# elif(a >= 69 and a <= 60):
#     print("d")
# elif(a >= 59 and a <= 50):
#     print("e")
# else:
#     print("f")

# 2
# fruits = ['banana', 'orange', 'mango', 'lemon']
# a = input("enter a fruit: ")
# if(a in fruits):
#     print("already there")
#     print(fruits)
# else:
#     fruits.append(a)
#     print(fruits)


# l3v3l 3


# 1
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
if("skills" in person):
    print(person['skills'][int(len(person['skills'])/2)])
if("skills" in person):
    if("Python" in person['skills']):
        print("Python" in person['skills'])
