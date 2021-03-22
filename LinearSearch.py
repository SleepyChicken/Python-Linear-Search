'''
        Written by SleepyChicken
'''

number = []
position = []
count = 0

X = None

print('Please enter your number')

while X != 'e' :
    X = input("") 
    if X.isdigit() == True :
        number.append(int(X))
    elif X == 'e' :
        print('You entered '+ str(len(number)) +' number')
        print(number)

searchNum = int(input('what number you want to search : '))

for i in number : 
    if i == searchNum :
        position.append(str('Found at position number ') +str(count+1))
    count = count + 1

if len(position) == 0 :
    print('Not found')
else :
    for i in position :
        print(i)
