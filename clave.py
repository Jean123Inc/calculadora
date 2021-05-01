password1 = 'conditional'

password = input('Digit a password: ')
count=1

while count<3:
    if password == password1:
        print('correct password')
        count=4
    else:
        password = input('Try again')
        count+=1


