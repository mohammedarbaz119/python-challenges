from turtle import update


l = {}
# l = dict()
print(len(l))
cat = {}
cat['name'] = "puchi"
print(cat)
person = {
    "firstname": "arbaz",
    "lastname": "uddin",
    "maritalstatus": False,
    "gender": "male",
    "age": 20,
    "skills": ["c", "c++", "python", "java", "html", "css", "js"],
    "country": "india",
    "city": "hyderabad"

}
print(len(person))
print(person["skills"], type(person["skills"]))
person["skills"].append("new")
print(person)
print(person.keys())
print(person.values())
persontiup = person.items()
print(persontiup)
del person["country"]
print(person)
person.pop('city')
print(person)
person.clear()
del person
