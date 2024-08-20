#dictionary is used to store multiple values in key value pairs
capital = {'Nepal': 'Kathmandu', 'India': 'Mumbai'}
print(capital)
print(type(capital))
print(len(capital))
#the length is calculated through the amount of keys
capital['Japan'] = 'Tokyo'#to add data in dictionary
print(capital)
print(capital.keys())
print(capital.values())
print(capital.items())#items give the key value pairs in tuple
capital.clear()
print(capital)
