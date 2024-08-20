path = 'demo.txt'
# # file is in read mode by default, if path cannot be found like this, we need to use root directory
# new_file = open(path)
# print(new_file)
# # checking if we can read and write the files
# print(new_file.readable())
# print(new_file.writable())

# print(new_file.read())
# print(new_file.close())#you need to always close the file after opening it, otherwise the data may be accessed in other places

# another_file = open(path,'r+')#specifying the mode of the file
# print(another_file)
# print(another_file.readable())
# print(another_file.writable())
# print(another_file.read())
# another_file.write("\n Another student name is Ram")
# print(another_file.seek(0))#.seek specifes from where to start reading the file
# print(another_file.read())
# another_file.close()

# w_file = open(path,'w+')#write garda sabai override hunxa, so as soon as you use write mode, the file overrides and becomes empty
# print(w_file)
# print(w_file.readable())
# print(w_file.writable())
# w_file.write("New student name is Sam \n")#only one write is printed as in write mode, the line gets replaced instead of stacked which occurs in r+ mode
# w_file.seek(0)
# print(w_file.read()) # you are not allowed to directly read in w+ mode, instead we use .seek
# w_file.close()


import shutil,os#these are inbuilt module, these can have classes, functions, various combinations from which we accessed methods such as .copy() and .move() 
# shutil.copy('demo.txt','c_demo.txt') #commenting the line otherwise a new copy will be made agin when the program is executed
# shutil.move('c_demo.txt','hello.txt')
# os.remove('hello.txt') 

#Learn about the a+ mode (append mode)
# (‘a+’): it is the mode to read and write the file aka append and read mode.
a_file = open(path,'a+')
print(a_file)
print(a_file.readable())
print(a_file.writable())
a_file.write("New student name is Harry \n")
a_file.seek(0)
print(a_file.read())
a_file.close()