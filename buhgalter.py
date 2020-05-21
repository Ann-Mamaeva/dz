print('укажите файл ')
filename = input()
with open(filename) as file:
    lines = file.readlines()
print("количество занчений ",len(lines))
s = 0
for line in lines:
    s = s+int(line)
print("сумма значений",s)
a = len(lines)
b = s
sr = b/a
print("среднее значение ",sr)

filename = 'program.txt'
with open(filename, 'w') as file:
    file.write("количество занчений "+str(len(lines)))
    file.write("сумма значений"+str(s))