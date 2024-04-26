from random import randint
from random import choice
from random import uniform
from functions import local_lapl
from functions import integr_lapl
from functions import transposition
from functions import transposition_with_repeat
from functions import combination
from functions import combination_with_repeat
from functions import placement
from functions import placement_with_repeat

def task_1():
    answer=''
    first_number=randint(1,9)
    second_number=randint(1,9)
    third_number=randint(1,9)
    points=randint(90,120)
    while second_number==first_number:
        second_number=randint(1,9)
    text=(f'1. Спортивный комментатор забыл счет баскетбольного ' 
         f'матча, но помнит, что каждая команда набрала меньше ' 
         f'{points} очков. Какова вероятность того, что, объявляя счет наугад' 
         f', комментатор правильно назовет число очков, набранных' 
         f' первой командой, если ему подсказали, что это число:\n'
         f'а) не содержит цифр {first_number} и {second_number};\n'
         f'б) содержит цифру {third_number}?\n')
    answer=f'Ответ: а) 1/64 или {round((1/64),4)}; б) 1/19 или {round((1/19),4)}'
    text+=answer
    print(text)

def task_2():
    russian=randint(6,8)
    ukranian=randint(5,7)
    bolgarian=randint(4,6)
    invited=russian-1
    variants=['России','Украины','Болгарии']
    rand_country_1=choice(variants)
    from_rus=randint(1,2)
    from_bol=randint(1,2)
    sumof=russian+ukranian+bolgarian
    text=(f'2. В третий тур конкурса красоты прошли {russian} участниц '
        f'из России, {ukranian} — из Украины и {bolgarian} — из Болгарии. Для '
        f'представления участниц на сцену наугад приглашают {invited} девушек.' 
        f' Найти вероятность того, что среди приглашенных:\n'
        f'а) все девушки из Poccии; \n'
        f'б) {from_rus} девушки из России и {from_bol} — из Болгарии.\n')
    answer=(f'Ответ: а) C({russian},{invited})/C({sumof},{invited}); ' 
           f'б) С({russian},{from_rus})*C({bolgarian},{from_bol})*C({ukranian},{invited-from_bol-from_rus})/C({sumof},{invited})')
    text+=answer
    print(text)


def task_3():
    answer=''
    pol_probability=randint(4,8)/10
    rus_probability=randint(4,8)/10
    while rus_probability==pol_probability:
        rus_probability=randint(4,8)
    answer=f'Ответ: а) {pol_probability*rus_probability}; б) {1-(1-rus_probability)*(1-pol_probability)}; '
    text=(f'Российская певица дает автограф с вероятностью '
f'{rus_probability}, а польская — с вероятностью {pol_probability}. Какова вероятность '
f'того, что завтра после концерта с участием обеих звезд: \n'
f'а) вам удастся получить оба автографа;\n'
f'б) удастся получить хотя бы один автограф;\n')
    rand_task=randint(0,1)
    if rand_task==0:
        text+=f'в) не удастся получить автограф у польской певицы?\n'
        answer+=f'в) {1-pol_probability}'
    else:
        text += f'в) не удастся получить автограф у российской певицы?\n'
        answer += f'в) {1 - rus_probability}'
    text+=answer
    print(text)


