import tkinter as tk
from PIL import Image, ImageTk

# Создание кнопок
def create_button(win, digit, size=(100, 100), position=(0, 0), padding=(5, 5), columnspan=1):
    original_image = Image.open(f'animation{digit}.gif')
    resized_image = original_image.resize(size)
    anim = ImageTk.PhotoImage(resized_image)

    original_image2 = Image.open(f'release{digit}.gif')
    resized_image2 = original_image2.resize(size)
    release = ImageTk.PhotoImage(resized_image2)

    button = tk.Button(win, image=anim, bd=0, highlightthickness=0, width=size[0], height=size[1], command=lambda: add_digit(str(digit)))
    button['bg'] = 'black'
    button['border'] = '0'
    button.grid(row=position[0], column=position[1], padx=padding[0], pady=padding[1], columnspan=columnspan)

    button.bind('<ButtonPress-1>', on_press(release))
    button.bind('<ButtonRelease-1>', on_release(anim))

#Функции изменения изображения

def on_press(image):
    def inner(event):
        event.widget.config(image=image)
    return inner

def on_release(image):
    def inner(event):
        event.widget.config(image=image)
    return inner


#Основные функции
x1 = ''
x2 = ''
x3 = ''
result = ''

def add_digit(digit):
    global x1, x2, x3
    if x2 == '':
        x1 += digit
        calc.delete(0, tk.END)
        calc.insert(0, x1.replace('.', ','))
    else:
        x3 += digit
        calc.delete(0, tk.END)
        calc.insert(0, x3.replace('.', ','))


def complete_operation(operation):
    global x2
    x2 = operation


def calculate():
    global x1, x2, x3
    global result
    if x2 == '+':
        if float(x1) % 1 == 0:
            result = int(x1) + int(x3)
        else:
            result = float(x1) + float(x3)
            if result % 1 == 0:
                result = int(result)
    elif x2 == '-':
        if float(x1) % 1 == 0:
            result = int(x1) - int(x3)
        else:
            result = float(x1) - float(x3)
            if result % 1 == 0:
                result = int(result)
    elif x2 == '/':
        result = int(x1) / int(x3)
        if result % 1 == 0.0:
            result = int(result)
        else:
            result = result
    elif x2 == '*':
        if float(x1) % 1 == 0:
            result = int(x1) * int(x3)
        else:
            result = float(x1) * float(x3)
            if result % 1 == 0:
                result = int(result)
    calc.delete(0, tk.END)
    if isinstance(result, float):
        disp_result = str(result).replace('.', ',')
    else:
        disp_result = result
    calc.insert(0, disp_result)
    x1 = result
    x2 = ''
    x3 = ''


def moment_operation(symb):
    global x1, x2, x3
    global result
    if symb == '%':
        result = int(x1) / 100
    elif symb == '+/-':
        result = int(x1) * -1
    calc.delete(0, tk.END)
    calc.insert(0, result)
    x1 = result
    x2 = ''
    x3 = ''

def comma_add(comma):
    global x1, x2, x3
    if x2 == '':
        if comma not in str(x1):
            x1 = str(x1) + '.'
            calc.delete(0, tk.END)
            calc.insert(0, x1.replace('.', ','))
    else:
        if comma not in str(x3):
            x3 = str(x3) + '.'
            calc.delete(0, tk.END)
            calc.insert(0, x3.replace('.', ','))



def clear():
    global x1, x2, x3
    x1 = ''
    x2 = ''
    x3 = ''
    calc.delete(0, tk.END)
    calc.insert(0, '0')


# База
win = tk.Tk()
win.geometry(f'440x800+70+10')
win['bg'] = '#000000'
win.title('Калькулятор')
icon = tk.PhotoImage(file='iconcalc.gif')
win.iconphoto(False, icon)

top_frame = tk.Frame(win, height=162, bg='#000000')
top_frame.grid(row =0, column = 0, columnspan = 4, stick = 'we')
top_frame.grid_propagate(False)
calc = tk.Entry(win, justify=tk.RIGHT, bd = 0, highlightthickness=0, font=('Helvetica Light', 50), width=10)
calc['bg'] = 'black'
calc['fg'] = 'white'
calc.insert(0, '0')
calc.grid(row=1, column=0, columnspan=4, stick='we', padx=35, pady=2)

# Создание кнопок для цифр и операций, размещение их на главном окне(уменьшение изображения)
create_button(win, '0', size=(200, 100), position=(6, 0), padding=(0, 0), columnspan=2)
create_button(win, '1', position=(5, 0))
create_button(win, '2', position=(5, 1))
create_button(win, '3', position=(5, 2))
create_button(win, '4', position=(4, 0))
create_button(win, '5', position=(4, 1))
create_button(win, '6', position=(4, 2))
create_button(win, '7', position=(3, 0))
create_button(win, '8', position=(3, 1))
create_button(win, '9', position=(3, 2))

# ЗАПЯТАЯ, ОПЕРАЦИИ т.д.
#button comma
original_image2 = Image.open('commarelease.gif')
resized_image2 = original_image2.resize((100, 100))
commarelease = ImageTk.PhotoImage(resized_image2)
original_image = Image.open('comma.gif')
resized_image = original_image.resize((100, 100))
commaimage = ImageTk.PhotoImage(resized_image)
commabutton = tk.Button(win, image=commaimage, bd=0, highlightthickness=0, width = 100, height = 100,
                        command=lambda: comma_add(','), relief='flat')
commabutton['bg'] = 'black'
commabutton['border'] = '0'
commabutton.grid(row=6, column=2, stick='', padx=5, pady=5)

commabutton.bind('<ButtonPress-1>', on_press(commarelease))
commabutton.bind('<ButtonRelease-1>',on_release(commaimage))

#button ac
original_image2 = Image.open('acrelease.gif')
resized_image2 = original_image2.resize((100, 100))
acrelease = ImageTk.PhotoImage(resized_image2)
original_image = Image.open('ac.gif')
resized_image = original_image.resize((100, 100))
acimage = ImageTk.PhotoImage(resized_image)
acbutton = tk.Button(win, image=acimage, bd=0, highlightthickness=0, width = 100, height = 100,
                     command=lambda: clear(), relief='flat')
acbutton['bg'] = 'black'
acbutton['border'] = '0'
acbutton.grid(row=2, column=0, stick='', padx=5, pady=5)

acbutton.bind('<ButtonPress-1>', on_press(acrelease))
acbutton.bind('<ButtonRelease-1>',on_release(acimage))

#button plus_minus
original_image2 = Image.open('plmirelease.gif')
resized_image2 = original_image2.resize((100, 100))
plmirelease = ImageTk.PhotoImage(resized_image2)
original_image = Image.open('plus_minus.gif')
resized_image = original_image.resize((100, 100))
plusminusimage = ImageTk.PhotoImage(resized_image)
plus_minus_button = tk.Button(win, image=plusminusimage, bd=0, highlightthickness=0, width = 100, height = 100,
                              command=lambda: moment_operation('+/-'), relief='flat')
plus_minus_button['bg'] = 'black'
plus_minus_button['border'] = '0'
plus_minus_button.grid(row=2, column=1, padx=5, pady=5)

plus_minus_button.bind('<ButtonPress-1>', on_press(plmirelease))
plus_minus_button.bind('<ButtonRelease-1>',on_release(plusminusimage))

#button procent
original_image2 = Image.open('procentrelease.gif')
resized_image2 = original_image2.resize((100, 100))
procentrelease = ImageTk.PhotoImage(resized_image2)
original_image = Image.open('procent.gif')
resized_image = original_image.resize((100, 100))
procentimage = ImageTk.PhotoImage(resized_image)
procentbutton = tk.Button(win, image=procentimage, bd=0, highlightthickness=0, width = 100, height = 100,
                          command=lambda: moment_operation('%'), relief='flat')
procentbutton['bg'] = 'black'
procentbutton['border'] = '0'
procentbutton.grid(row=2, column=2, stick='', padx=5, pady=5)

procentbutton.bind('<ButtonPress-1>', on_press(procentrelease))
procentbutton.bind('<ButtonRelease-1>',on_release(procentimage))

#button division
original_image2 = Image.open('divisionrelease.gif')
resized_image2 = original_image2.resize((100, 100))
divisionrelease = ImageTk.PhotoImage(resized_image2)
original_image = Image.open('division.gif')
resized_image = original_image.resize((100, 100))
divisionimage = ImageTk.PhotoImage(resized_image)
divisionbutton = tk.Button(win, image=divisionimage, bd=0, highlightthickness=0, width = 100, height = 100,
                           command=lambda: complete_operation('/'), relief='flat')
divisionbutton['bg'] = 'black'
divisionbutton['border'] = '0'
divisionbutton.grid(row=2, column=3, stick='', padx=5, pady=5)

divisionbutton.bind('<ButtonPress-1>', on_press(divisionrelease))
divisionbutton.bind('<ButtonRelease-1>',on_release(divisionimage))

#button multiplying
original_image2 = Image.open('multiplyingrelease.gif')
resized_image2 = original_image2.resize((100, 100))
multiplyingrelease = ImageTk.PhotoImage(resized_image2)
original_image = Image.open('multiplying.gif')
resized_image = original_image.resize((100, 100))
multiplyingimage = ImageTk.PhotoImage(resized_image)
multiplyingbutton = tk.Button(win, image=multiplyingimage, bd=0, highlightthickness=0, width = 100, height = 100,
                              command=lambda: complete_operation('*'), relief='flat')
multiplyingbutton['bg'] = 'black'
multiplyingbutton['border'] = '0'
multiplyingbutton.grid(row=3, column=3, stick='', padx=5, pady=5)

multiplyingbutton.bind('<ButtonPress-1>', on_press(multiplyingrelease))
multiplyingbutton.bind('<ButtonRelease-1>',on_release(multiplyingimage))

#button minus
original_image2 = Image.open('minusrelease.gif')
resized_image2 = original_image2.resize((100, 100))
minusrelease = ImageTk.PhotoImage(resized_image2)
original_image = Image.open('minus.gif')
resized_image = original_image.resize((100, 100))
minusimage = ImageTk.PhotoImage(resized_image)
minusbutton = tk.Button(win, image=minusimage, bd=0, highlightthickness=0, width = 100, height = 100,
                        command=lambda: complete_operation('-'), relief='flat')
minusbutton['bg'] = 'black'
minusbutton['border'] = '0'
minusbutton.grid(row=4, column=3, stick='', padx=5, pady=5)

minusbutton.bind('<ButtonPress-1>', on_press(minusrelease))
minusbutton.bind('<ButtonRelease-1>',on_release(minusimage))

#button plus
original_image2 = Image.open('plusrelease.gif')
resized_image2 = original_image2.resize((100, 100))
plusrelease = ImageTk.PhotoImage(resized_image2)
original_image = Image.open('plus.gif')
resized_image = original_image.resize((100, 100))
plusimage = ImageTk.PhotoImage(resized_image)
plusbutton = tk.Button(win, image=plusimage, bd=0, highlightthickness=0, width = 100, height = 100,
                       command=lambda: complete_operation('+'), relief='flat')
plusbutton['bg'] = 'black'
plusbutton['border'] = '0'
plusbutton.grid(row=5, column=3, stick='', padx=5, pady=5)

plusbutton.bind('<ButtonPress-1>', on_press(plusrelease))
plusbutton.bind('<ButtonRelease-1>',on_release(plusimage))
#button equals
original_image2 = Image.open('equalsrelease.gif')
resized_image2 = original_image2.resize((100, 100))
equalsrelease = ImageTk.PhotoImage(resized_image2)
original_image = Image.open('equals.gif')
resized_image = original_image.resize((100, 100))
equalsimage = ImageTk.PhotoImage(resized_image)
equalsbutton = tk.Button(win, image=equalsimage, bd=0, highlightthickness=0, width = 100, height = 100,
                         command=lambda: calculate(), relief='flat')
equalsbutton['bg'] = 'black'
equalsbutton['border'] = '0'
equalsbutton.grid(row=6, column=3, stick='', padx=5, pady=5)

equalsbutton.bind('<ButtonPress-1>', on_press(equalsrelease))
equalsbutton.bind('<ButtonRelease-1>',on_release(equalsimage))

win.mainloop()
