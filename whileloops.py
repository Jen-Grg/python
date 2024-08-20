x = 0
while (x<=10):
    x+=1
    if(x==5):
       continue
    print(x)
    
color = ['white','black','red','yellow']
sports = ['football','volleyball','basketball','cricket','hockey']
#at first outer loop ko one element performs action with all the inner loop's element and then jumps to another element in outer loop
#outer loop
for i in color:
    #inner loop
    for j in sports:
        print(i,j)

for i in range(1,11):
    j = 1
    while(j<=10):
        print("Multiplication of {0} and {1} is {2}".format(i,j,i*j))
        j+=1
#to check for even number: if the user gives odd number continue the loop and ask user to put the input. If user gives even numbe, break the loop and enter a thnakyou message
y=int(input('please enter an even number to break the loop: '))
while(y>0):
    if(y%2==0):
        print('Thank you')
        break
    else:
        y=int(input('please enter an even number to break the loop: '))
        continue
print('0 and lower than zero cannot be even nor odd.')




