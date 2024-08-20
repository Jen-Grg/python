# set is used to store multiple values which contain only unique element, data are stored in unstructed way and it is changable, it is denoted by {}
unique_id = {101,102,103,101,102,'python'}
print(unique_id)
# unable to store duplicate value, displays only the unique value and the position of data constantly changes
p_language = ('PHP','Python','Javascript','Python','Python')
unique_language = set(p_language)
print(unique_language)
unique_language.add('Java')
print(unique_language)
unique_language.update(unique_id) #to concate two sets
print(unique_language)
# you cannot remove using an index in set unlike in list
unique_language.remove('Java')
print(unique_language)
# pop removes a random value
pop_element = unique_language.pop()
print(pop_element)
print(unique_language)
# to copy set
copy_set = unique_language.copy()
print(copy_set)
copy_set.clear()#to clear all data from set
print(copy_set)
sports = [ ]#define empty list
empty_set = set()
empty_set.add('Ram')
print(empty_set)

#-------------Dictionary-----------
dictionary = {} #both set and dictionary use {} but set stores only data but dictionary stores in key value pair, an empty {} is always a dictionary as an empty set is denoted by set()
