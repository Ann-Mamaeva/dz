import re
filename = 'program.txt'
with open(filename, 'w') as file:
    file.write('')
while True:
    print('Укажите почту')
    email = input()
    a = '\w+@\w+.\w+'  #регулярное выражение, что совпадает с почтой вида test@gmail.com
    if re.match(r'\w+@\w+.\w+',email):
        with open(filename, 'a') as file:
            file.write(str(email)+'\n')
    else:
        print('Введите почту вида: test@gmail.com')
