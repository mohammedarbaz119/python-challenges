# l = []
# nl = list()
# list of fruits



fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage',
              'Onion', 'Carrot']      # list of vegetables
animal_products = ['milk', 'meat', 'butter',
                   'yoghurt']             # list of animal products
web_techs = ['HTML', 'CSS', 'JS', 'React', 'Redux',
             'Node', 'MongDB']  # list of web technologies
countries = ['Finland', 'Estonia', 'Denmark', 'Sweden', 'Norway']
# list containing different data types
lst = ['Asabeneh', 250, True, {'country': 'Finland', 'city': 'Helsinki'}]
# challenges
l = []
l5 = [1, 2, 3, 4, 5]
print(len(l5))
print(f"{l5[0]} {l5[int((0+len(l5))/2)]} {l5[len(l5)-1]}")
comapnies = ["Facebook", "Google", "Microsoft",
             "Apple", "IBM", "Oracle", "Amazon"]
print(
    f"{comapnies[0]} {comapnies[int((0+len(comapnies))/2)]} {comapnies[len(comapnies)-1]}")
print(len(comapnies))
comapnies[2] = "new comapny"
print(comapnies)
comapnies.append("anene")
print(comapnies)
comapnies[0] = comapnies[0].upper()
print(comapnies)
print('# '.join(comapnies))
comapnies.sort()
comapnies.reverse()
print(comapnies)
print(comapnies[0:3])
print('\n')
print(comapnies[-3:])
comapnies.pop(0)
print(comapnies)
comapnies.clear()
del comapnies
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
third = front_end+back_end
print(third)
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
print(max(ages))
a = '10.0'
print(int(a))

