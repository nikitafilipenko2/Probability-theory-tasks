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
ans='Ответ: '
shift='\n'
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

def task_4():
    prob_1=randint(4,9)/10
    unp_1=round(1-prob_1,1)
    prob_2=randint(4,9)/10
    while prob_2==prob_1:
        prob_2=randint(4,9)/10
    unp_2=round(1-prob_2)
    text=(f'Две россиянки участвуют в международном конкурсе '
     f'по мировой экономике. Успешно пройти тур первая девушка '
     f"может с вероятностью {prob_1}, вторая — {prob_2}. Вчера прошел "
     f"третий, последний тур соревнований. Какова вероятность "
     f'того, что у второй участницы успешно пройденных '
     f'туров больше, чем у первой? \n')
    answer=f'{ans} {unp_1}*{prob_2}+{prob_1}*{unp_1}*{prob_2}*{prob_2}+{prob_1}*{prob_1}*{unp_1}*{prob_2}*{prob_2}*{prob_2} или {unp_1*prob_2+prob_1*unp_1*prob_2*prob_2+prob_1*prob_1*unp_1*prob_2**3}'
    text+=answer
    print(text)

def task_5():
    text=(f'5. Из полного набора костей домино (28) наугад извлечена кость. Найти вероятность того, что вторую наугад'
f' взятую кость можно приставить к первой, если первая оказалась:{shift}'
f'а) дублем;{shift}'
f'б) не дублем.{shift}')
    answer=f'{ans} a) 6/27 или {round(6/27,2)}; б) 12/27 или {round(12/27,2)}'
    text+=answer
    print(text)



def task_6():
    prob_s=randint(4,9)/10
    prob_m=randint(1,3)/10
    print(prob_s,prob_m)
    prob_j=0
    uns=round(1-prob_s,1)
    unm=round(1-prob_m,1)
    unj=1
    text=f'Три брата посеяли пшеницу, однако «...в долгом времени  ' \
         f'аль вскоре приключилось с ними горе: кто-то в поле  ' \
         f'стал ходить да пшеницу шевелить. Наконец они смекнули  ' \
         f', чтоб стоять на карауле, хлеб ночами поберечь, злоговора  ' \
         f'подстеречь». В их деревне всем известно, что старший  ' \
         f'брат засыпает в дозоре с вероятностью {uns}, средний — {unm},  ' \
         f' а у младшего бессонница. Найти вероятность того, что  ' \
         f'в первую ночь удастся поймать вора, если очередность  ' \
         f' дежурства определяется жребием.{shift}'
    answer=f'{ans} {uns+unm+unj}/3 или {round((uns+unm+unj)/3,2)}'
    text+=answer
    print(text)
