# synax
list = [1,2,3]
tuple = (1,2,3)

# list is mutable, tuple is not
list[1]=50
print(list)
# tuple[1]=50 --> TypeError: 'tuple' object does not support item assignment

# tuple can be used as a key in a dictionary
dict_tuple = {tuple: 1}
# dict_list = {list: 1} --> TypeError: unhashable type: 'list'

# more memomy for list, less for tuple

