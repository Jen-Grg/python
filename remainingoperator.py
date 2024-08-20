#identity operator - is, is not
x = 2
y= 2
print(id(x))
print(id(y))
x_list = [1,2,3,4]
y_list = [1,2,3,4]
print(id(x_list))
print(id(y_list))
#id of x and y maybe same but not of x_list and y_list even with same values
print(x is y)
print(x_list is y_list)
#value and id must be the same for x_list is y_list to have been true furing identity check


#in , not in => membership operator
text = 'agiegfiwgigru'
print('n' in text)
print('n' not in text)
z_list = ['football', 'vollyeball', 'basketball']
email = ['jengrg003@gmail.com','ram@gmail.com', 'abc@gmail.com']
print('volleyball' in z_list)
print('abc@gmail.com' in email)
