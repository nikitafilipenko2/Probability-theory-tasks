from random import randint
from random import uniform
# inuform(начало, конец) - возрщает рандомное вещественное в диапазоне включая концы
# randint(начало, конец) - возрщает рандомное целое в диапазоне включая концы

import Nikita
import danila_main

import sys
import os

from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Checkbutton
import subprocess
output = subprocess.check_output(r'powershell -command "[Environment]::GetFolderPath(\"Desktop\")"')
path = output.decode().strip()
def select_all_tasks():
    for check in check_list:
        check.set(chk_all.get())

def clicked():
    global variants_count
    global tasks_num_list
    if txt.get() != '':
        variants_count = int(txt.get())
    else:
        variants_count = 1
    if chk_all.get():
        for i in range(1, 22):
            tasks_num_list.append(i)
    else:
        number = 1
        for i in check_list:
            if i.get():
                tasks_num_list.append(number)
            number += 1
    mess = messagebox.showinfo("Подтверждение", "Файл с заданиями обновится после нажатия на кнопку ОК!")
    if mess == 'ok':
        save_files()
        window.after(1000, window.destroy)


def save_files():


    # Пример сохранения файлов (замените содержимое файла своим)
    with open(path+'/задания.doc', 'w', encoding='utf-8') as tasks:
        with open(path+'/ответы.doc', 'w', encoding='utf-8') as answers:
            for i in range(0, variants_count):
                tasks.write(f'ВАРИАНТ {i + 1}\n')
                answers.write(f'ВАРИАНТ {i + 1}\n')
                for task in tasks_num_list:  # идем по списку с номерами заданий
                    if task == 1:  # если номер = 1, то пишем его
                        coin_flip = randint(1, 2)
                        if coin_flip == 1:
                            text, answer = Nikita.task_1()
                        elif coin_flip == 2:
                            text, answer = danila_main.task_1()

                        tasks.write(text + '\n')
                        answers.write(answer + '\n')
                        continue

                    if task == 2:
                        coin_flip = randint(1, 2)
                        if coin_flip == 1:
                            text, answer = Nikita.task_2()

                        elif coin_flip == 2:
                            text, answer = danila_main.task_2()

                        tasks.write(text + '\n')
                        answers.write(answer + '\n')
                        continue

                    if task == 3:
                        coin_flip = randint(1, 2)
                        if coin_flip == 1:
                            text, answer = Nikita.task_3()

                        elif coin_flip == 2:
                            text, answer = danila_main.task_3()

                        tasks.write(text + '\n')
                        answers.write(answer + '\n')
                        continue

                    if task == 4:
                        coin_flip = randint(1, 2)
                        if coin_flip == 1:
                            text, answer = Nikita.task_4()

                        elif coin_flip == 2:
                            text, answer = danila_main.task_4()

                        tasks.write(text + '\n')
                        answers.write(answer + '\n')
                        continue

                    if task == 5:
                        coin_flip = randint(1, 2)
                        if coin_flip == 1:
                            text, answer = Nikita.task_4()
                        elif coin_flip == 2:
                            text, answer = danila_main.task_5()

                        tasks.write(text + '\n')
                        answers.write(answer + '\n')
                        continue

                    if task == 6:
                        coin_flip = randint(1, 2)
                        if coin_flip == 1:  # задание Егора
                            text, answer = Nikita.task_6()
                        elif coin_flip == 2:
                            text, answer = danila_main.task_6()

                        tasks.write(text + '\n')
                        answers.write(answer + '\n')
                        continue

                    if task == 7:
                        coin_flip = randint(1, 2)
                        if coin_flip == 1:
                            text, answer = Nikita.task_7()

                        elif coin_flip == 2:
                            text, answer = Nikita.task_7()

                        tasks.write(text + '\n')
                        answers.write(answer + '\n')
                        continue

                    if task == 8:
                        coin_flip = randint(1, 2)
                        if coin_flip == 1:
                            text, answer = Nikita.task_8()

                        elif coin_flip == 2:
                            text, answer = danila_main.task_8()

                        tasks.write(text + '\n')
                        answers.write(answer + '\n')
                        continue

                    if task == 9:
                        coin_flip = randint(1, 2)
                        if coin_flip == 1:
                            text, answer = Nikita.task_9()

                        elif coin_flip == 2:
                            text, answer = danila_main.task_9()

                        tasks.write(text + '\n')
                        answers.write(answer + '\n')
                        continue

                    if task == 10:
                        coin_flip = randint(1, 2)
                        if coin_flip == 1:
                            text, answer = Nikita.task_10()

                        elif coin_flip == 2:
                            text, answer = danila_main.task_10()

                        tasks.write(text + '\n')
                        answers.write(answer + '\n')
                        continue

                    if task == 11:
                        coin_flip = randint(1, 2)
                        if coin_flip == 1:
                            text, answer = Nikita.task_11()

                        elif coin_flip == 2:
                            text, answer = Nikita.task_11()

                        tasks.write(text + '\n')
                        answers.write(answer + '\n')
                        continue

                    if task == 12:
                        coin_flip = randint(1, 2)
                        if coin_flip == 1:
                            text, answer = Nikita.task_12()

                        elif coin_flip == 2:
                            text, answer = danila_main.task_12()

                        tasks.write(text + '\n')
                        answers.write(answer + '\n')
                        continue

                    if task == 13:
                        coin_flip = randint(1, 2)
                        if coin_flip == 1:
                            text, answer = Nikita.task_13()

                        elif coin_flip == 2:
                            text, answer = danila_main.task_13()

                        tasks.write(text + '\n')
                        answers.write(answer + '\n')
                        continue

                    if task == 14:
                        coin_flip = randint(1, 2)
                        if coin_flip == 1:
                            text, answer = Nikita.task_14()

                        elif coin_flip == 2:
                            text, answer = danila_main.task_14()

                        tasks.write(text + '\n')
                        answers.write(answer + '\n')
                        continue

                    if task == 15:
                        coin_flip = randint(1, 2)
                        if coin_flip == 1:
                            text, answer = Nikita.task_15()

                        elif coin_flip == 2:
                            text, answer = danila_main.task_15()

                        tasks.write(text + '\n')
                        answers.write(answer + '\n')
                        continue

                    if task == 16:
                        coin_flip = randint(1, 2)
                        if coin_flip == 1:
                            text, answer = Nikita.task_16()
                        elif coin_flip == 2:
                            text, answer = danila_main.task_16()

                        tasks.write(text + '\n')
                        answers.write(answer + '\n')
                        continue

                    if task == 17:
                        coin_flip = randint(1, 2)
                        if coin_flip == 1:
                            text, answer = Nikita.task_17()

                        elif coin_flip == 2:
                            text, answer = danila_main.task_17()

                        tasks.write(text + '\n')
                        answers.write(answer + '\n')
                        continue

                    if task == 18:
                        coin_flip = randint(1, 2)
                        if coin_flip == 1:
                            text, answer = Nikita.task_18()

                        elif coin_flip == 2:
                            text, answer = danila_main.task_18()

                        tasks.write(text + '\n')
                        answers.write(answer + '\n')
                        continue

                    if task == 19:
                        coin_flip = randint(1, 2)
                        if coin_flip == 1:
                            text, answer = Nikita.task_19()

                        elif coin_flip == 2:
                            text, answer = danila_main.task_19()

                        tasks.write(text + '\n')
                        answers.write(answer + '\n')
                        continue

                    if task == 20:
                        coin_flip = randint(1, 2)
                        if coin_flip == 1:
                            text, answer = Nikita.task_20()

                        elif coin_flip == 2:
                            text, answer = danila_main.task_20()

                        tasks.write(text + '\n')
                        answers.write(answer + '\n')
                        continue

                tasks.write('\f\n\n')
                answers.write('\f\n\n')

            tasks.close()
            answers.close()


    messagebox.showinfo("Сохранено", f"Файлы успешно сохранены на рабочем столе")

variants_count = 0
tasks_num_list = []  # множество заданий, которые нужно сгенерировать

window = Tk()
window.geometry('400x600')

window.title('Генератор заданий')
count_var_label = Label(window, text='        Введите количество вариантов: ', font=("Times New Roman", 12, "bold"))
count_var_label.grid(column=0, row=0)

txt = Entry(window, width=10)
txt.grid(column=1, row=0)
txt.focus()

chk_all = BooleanVar()
chk_all.set(False)  # задайте проверку состояния чекбокса
chk_all.trace_add('write', lambda *args: select_all_tasks())
all_tasks_check = Checkbutton(window, text='Все задания', var=chk_all)
all_tasks_check.grid(column=0, row=2)

check_list = []
for i in range(0, 21):
    check_list.append(BooleanVar())
    check_list[i].set(False)

for i in range(0, 20):

    if i < 9:
        task_check1 = Checkbutton(window, text=f'0{i + 1}', var=check_list[i], width=10)
        task_check1.grid(column=0, row=i + 4)
    elif i==9:
        task_check1 = Checkbutton(window, text=f'{i + 1}', var=check_list[i], width=10)
        task_check1.grid(column=0, row=i + 4)
    else:
        task_check2 = Checkbutton(window, text=f'{i + 1}', var=check_list[i], width=10)
        task_check2.grid(column=1, row=i-10 + 4)

btn = Button(window, text='Создать документ', bg='orange', fg='black', command=clicked)
btn.grid(row=27)

window.mainloop()
N = 20  # сколько всего задач в варианте




