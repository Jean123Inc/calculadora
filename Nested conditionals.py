age = int(input('Digit your age: '))

if age>0 and age<100:
    print('Correct age')
    if age>=18:
        print('Coming of age')
else:
    print('Incorrect age')

print('End of the programme')