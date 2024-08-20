#list is used to store multiple value which is ordered, changeable and allow duplicates. It is denoted by square bracket
laptops = ['Dell', 'Mac', 'Lenovo', 'Hp']
print(len(laptops)) #to know the length, length is 4, index is 3
print(type(laptops))#To know the types
#to access the value through index
print(laptops[0][1])#gives the character index of e from Dell
print(laptops.index('Lenovo'))
laptops.append('Acer')
print(laptops)
# insert() is to add element in mentioned index 
laptops.insert(3,'Dell')
print(laptops)
#count() is to count the element in list
print(laptops.count('Dell'))
#pop()- to remove element from the last index of list as well as return the removed element, you can also remove elemenyt from mentioned index such as laptop.pop(2)
pop_element = laptops.pop()
print(pop_element)
print(laptops)
#extends()
p_language = ['HTML','CSS','PHP']
laptops.extend(p_language)
print(laptops)
#sort()- sorts in ascending order
laptops.sort()
print(laptops)
laptops.sort(reverse = True)
print(laptops)
#reverse()- reverses the order of indexed elements
laptops.reverse()
print(laptops)
#remove()- same as pop but doesnt return the element
laptops.remove('CSS')
print(laptops)

