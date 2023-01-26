# enumerate - returns a tuple containing a count and the values
fruits = ['apple', 'banana', 'orange', 'strawberry']

num = 1
for element in fruits:
    print(num, element)
    num +=1

print('--------')

for n, element in enumerate(fruits):
    print(n,element)

print('--------')

for n, element in enumerate(fruits,1):
    print(n,element)

print('xxxxxxxx')

print(list(enumerate(fruits)))
print(enumerate(fruits))


