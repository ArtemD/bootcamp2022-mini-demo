#Int
print(type(7))

# float
print(type(7.0))

# string
print(type('artem is tired and wants weekend to start soon :)'))

# list
lista = ["string", 2.00, [1, 2, 3]]
print(type(lista))

lista[0]="new value"

print(lista[0])

# tuple
tuple = ("string", 2.00, [1, 2, 3])
print(type(tuple))

# dict
dict = {'key1': 'value1', 'key2': 'value2'}
print(list(dict.values())[0])
print(dict['key1'])
print(type(dict))

# set
set = {1, 2, 3}
print(set)

# bool
boo = False
print(type(boo))

# none
none = None
print(type(none))


if boo==True:
    print("boo is true")
else:
    print("boo is false")

for l in lista:
    print(l)

while boo==False:
    print("boo is false")
    boo=True


test = 77
test2 = test +1
test = test + test2
print(test)


text = "Artem"
txt = 'Hello {} World {}'.format(text, [66, 77])
print(txt)