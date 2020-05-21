file = 'pi_million_digits.txt'

pi_string = ''

with open(file) as f:
    lines = f.readlines()
for line in lines:
    pi_string += line


birthday = input("Введите данные рождения день и месяц в формате DDMM")
if birthday in pi_string:
    print("Клево вы в чичле ПИ", " на ", pi_string.find(birthday), " месте")
else:
    print("вы не были избраны")