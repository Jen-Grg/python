# loop denotes repetation or iteration
sports_list = ['football','volleyball','basketball']
#using range, in range it stops 1 step behind so if the range is (1,10) it gives till 9 only
for i in sports_list:
    print(i)
for i in range(1,10):
    print(i)
x = int(input('Enter the number: '))
print('The multiplication table of ', x, 'is:')
for i in range(1,11):
    print(x*i)
number = [1,2,3,4,5]
sum = 0
for i in number:
    sum += i
    print(sum)
