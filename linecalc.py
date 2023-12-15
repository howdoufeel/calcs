lang = 'EN'
lang_opt = input('Enter L to change language or other key to continue>>')
while lang_opt == 'L':
    if lang == 'RU':
        lang = 'EN'
        lang_opt = input('Enter L to change language or other key to continue>>')
    else:
        lang = 'RU'
        lang_opt = input('Введите L, чтобы сменить язык, или другую любую клавишу, чтобы продолжить>>')

if lang == 'EN':
    f = 'Enter first number>> '
    o = 'Enter operation(sign)>> '
    s = 'Enter second number>>'
    r = 'Result>> '
    e = 'Operation not defined'
    p = 'Enter "ph" to continue and other key to finish>> '

if lang == 'RU':
    f = 'Введите первое число>> '
    o = 'Выберите операцию(знак)>> '
    s = 'Введите второе число>>'
    r = 'Результат>> '
    e = 'Операция не поределена'
    p = 'Для продолжения введите \'ph\', для завершения любую клавишу>>'

c = 'ph'
while c == 'ph':
    a = float(input(f))
    action = input(o)
    b = float(input(s))

    if action == '+':
        print(r, a + b)
    elif action == '-':
        print(r, a - b)
    elif action == '*':
        print(r, a * b)
    elif action == "/":
        print(r, a / b)
    else:
        print(e)
    c = input(p)