#Good
d = {'a': '1', 'b': '2', 'c': '3'}
for key in d:
    print(key, end=' ')
print()
#Bad
for key in d.keys():
    print(key, end=' ')
print()

#Good
key = 'a'
if key in d:
    print(d[key])

#Метод словарей get
navs = {}