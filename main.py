import random

power = int(input('Введите степень: '))
koefs = {}
for i in range(power + 1):
    koefs[i] = random.randint(0, 100)

print(koefs)


def print_expression(k_1, i_1):
    if k_1 != 0:
        if k_1 == 1:
            return f'x**{i_1}'
        else:
            return f'{koefs[i_1]}*x**{i_1}'
    return None


expressions = []
for i in range(power, 1, - 1):
    e = print_expression(koefs[i], i)
    if e is not None:
        expressions.append(e)

if koefs[1] != 0:
    if koefs[1] == 1:
        expressions.append('x')
    else:
        expressions.append(f'{koefs[1]}*x')

if koefs[0] != 0:
    expressions.append(str(koefs[0]))

print(expressions)

string = expressions[0]
for i in range(1, len(expressions), 1):
    string += ' + ' + expressions[i]
string += ' = 0'

print(string)

with open("expression.txt", "w") as expressions_file:
    expressions_file.write(string)
