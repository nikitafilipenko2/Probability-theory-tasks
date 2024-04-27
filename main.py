import math
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
from functions import discr_math_expectation
from functions import discr_dispersion
from functions import discr_standart_deviation
from functions import integr_teor_dict
from functions import local_teor_list
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
    russian=randint(5,8)
    ukranian=randint(5,8)
    bolgarian=randint(5,8)
    invited=russian-1
    variants={'России':russian,'Украины':ukranian,'Болгарии':bolgarian}
    rand_country_1=choice(list(variants.keys()))
    from_rus=randint(1,2)
    from_bol=randint(1,2)
    sumof=russian+ukranian+bolgarian
    text=(f'2. В третий тур конкурса красоты прошли {russian} участниц '
        f'из России, {ukranian} — из Украины и {bolgarian} — из Болгарии. Для '
        f'представления участниц на сцену наугад приглашают {invited} девушек.' 
        f' Найти вероятность того, что среди приглашенных:\n'
        f'а) все девушки из {rand_country_1}; \n'
        f'б) {from_rus} девушки из России и {from_bol} — из Болгарии.\n')
    answer=(f'Ответ: а) C({variants[rand_country_1]},{invited})/C({sumof},{invited}); ' 
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
     f"третий, последний тур соревнований. Какова вероятность ")
    task_type=randint(0,1)
    if task_type==0:
        text+=(f'того, что у второй участницы успешно пройденных '
        f'туров больше, чем у первой? \n')
        answer=f'{ans} {unp_1}*{prob_2}+{prob_1}*{unp_1}*{prob_2}*{prob_2}+{prob_1}*{prob_1}*{unp_1}*{prob_2}*{prob_2}*{prob_2} или {unp_1*prob_2+prob_1*unp_1*prob_2*prob_2+prob_1*prob_1*unp_1*prob_2**3}'
    else:
        text += (f'того, что у первой участницы успешно пройденных '
                 f'туров больше, чем у второй? \n')
        answer = f'{ans} {unp_2}*{prob_1}+{prob_2}*{unp_2}*{prob_1}*{prob_1}+{prob_2}*{prob_2}*{unp_2}*{prob_1}*{prob_1}*{prob_1} или {unp_2 * prob_1 + prob_2 * unp_2 * prob_1 * prob_1 + prob_2 * prob_2 * unp_2 * prob_1 ** 3}'

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

    prob_j=0
    uns=round(1-prob_s,1)
    unm=round(1-prob_m,1)

    unj=1
    vars={'':uns+unm+unj,' не':prob_j+prob_m+prob_s}
    no=choice(list(vars.keys()))
    text=f'Три брата посеяли пшеницу, однако «...в долгом времени  ' \
         f'аль вскоре приключилось с ними горе: кто-то в поле  ' \
         f'стал ходить да пшеницу шевелить. Наконец они смекнули  ' \
         f', чтоб стоять на карауле, хлеб ночами поберечь, злоговора  ' \
         f'подстеречь». В их деревне всем известно, что старший  ' \
         f'брат засыпает в дозоре с вероятностью {prob_s}, средний — {prob_m},  ' \
         f' а у младшего бессонница. Найти вероятность того, что  ' \
         f'в первую ночь{no} удастся поймать вора, если очередность  ' \
         f' дежурства определяется жребием.{shift}'
    answer=f'{ans} {vars[no]}/3 или {round((vars[no])/3,2)}'
    text+=answer
    print(text)


def task_7():
    prob_1=randint(1,3)/10
    prob_2=randint(3,5)/10
    prob_3=round(1-prob_2-prob_1,1)
    sold_1=randint(1,4)/10
    sold_2=randint(2,7)/10
    sold_3=randint(5,9)/10
    sumof=round(prob_1*round((1-sold_1),1)+prob_2*round((1-sold_2),1)+prob_3*round((1-sold_3),1),1)
    vars={'в помещении театра':round(prob_1*round((1-sold_1),1),1),'на Тверской':round(prob_2*round((1-sold_2),1),1),'на «Пушкинской»':round(prob_3*round((1-sold_3),1),1)}
    rand_cash=choice(list(vars.keys()))
    text=f'Зритель с вероятностью {prob_1}, {prob_2} и {prob_3} соответственно ' \
         f'может обратиться за билетом в одну из трех театральных ' \
         f'касс Большого театра: в помещении театра, на Тверской  ' \
         f'и на станции метро «Пушкинская». Вероятность' \
         f'того, что к моменту прихода зрителя в кассе все билеты ' \
         f'будут проданы, соответственно равна {sold_1}, {sold_2} и {sold_3}.' \
         f'Поклонник Большого театра купил билет в одной из этих ' \
         f'трех касс. Какова вероятность того, что эта касса {rand_cash}?{shift}'
    answer=f'{ans} {vars[rand_cash]}/{sumof} или {round(vars[rand_cash]/sumof,2)}'
    text+=answer
    print(text)

def task_8():
    vars={'синий':5,'красный':45}
    vars_num={'три':3,'четыре':4,'два':2}
    kavo_num=choice(list(vars_num.keys()))
    kavo=choice(list(vars.keys()))
    text=f'В ящике имеется 5 синих и 45 красных шаров. Какова ' \
         f' вероятность того, что при десяти независимых выборах ' \
         f'с возвращением {kavo_num} раза будет выниматься {kavo} шар?{shift}'
    answer=f'{ans} C(10,3)*({vars[kavo]}/50)^{vars_num[kavo_num]}*({50-vars[kavo]}/50)^{10-vars_num[kavo_num]}'
    text+=answer
    print(text)

def task_9():
    prob=choice([0.25,0.3,0.4,0.2])
    km=randint(220,250)
    num=choice([50,60,70])

    x_num=(num-km*prob)/(math.sqrt(km*prob*(1-prob)))
    x_km=(km-km*prob)/(math.sqrt(km*prob*(1-prob)))
    x_0=(0-km*prob)/(math.sqrt(km*prob*(1-prob)))
    x_num=round(x_num,2)
    x_km=round(x_km,2)

    text=f'Вероятность переключения передач на каждом ' \
         f'километре трассы равна {prob}. Найти вероятность того, что ' \
         f'на {km}-километровом участке этой трассы переключение ' \
         f'передач произойдет: {shift}' \
         f'а) {num} раз;{shift}'
    task=randint(0,1)
    if task==0:
         text+=f'б) не более {num} раз.{shift}'

         answer=f'{ans} a){round((float(local_lapl(x_num))/math.sqrt(km*prob*(1-prob))),2)} б){round(integr_lapl(x_num)-integr_lapl(x_0),4)}'

    else:
         text+=f'б) не менее {num} раз.{shift}'
         answer = f'{ans} a){round(float(local_lapl(x_num)) / math.sqrt(km * prob * (1 - prob)), 2)} б){round(integr_lapl(x_km)-integr_lapl(x_num),4)}'

    text+=answer
    print(text)

def task_10():
    safety=choice([0.001,0.002,0.004])
    vars={'двух':2,'трех':3,'четырех':4}
    quantity=choice(list(vars.keys()))
    x_0=(0-100*safety)/math.sqrt(safety*(1-safety)*100)
    text=f'Вероятность выхода из строя во время испытания ' \
         f'на надежность любого из однотипных приборов равна ' \
         f'{safety}. Найти вероятность того, что в партии из 100 ' \
         f' приборов во время испытания выйдут из строя не более {quantity} ' \
         f'приборов.'
    num=vars[quantity]
    x_num=(num-safety*100)/math.sqrt(safety*(1-safety)*100)
    answer=f'{ans} {round(integr_lapl(round(x_num,2))-integr_lapl(round(x_0,2)),4)}'
    text+=answer
    print(text)

def task_11():
    p1=randint(2,4)/10
    p2=randint(4,6)/10
    p3=randint(6,8)/10
    q1=round(1-p1,1)
    q2=round(1-p2,1)
    q3=round(1-p3,1)
    print(q1)

    text=f'Производится три независимых выстрела. Вероятность ' \
         f' попадания при первом выстреле равна {p1}; при втором — {p2}; при третьем — {p3}. ' \
         f'Составить ряд распределения числа попаданий. Найти М(Х), D(X), (X), F(X) этой ' \
         f'случайной величины. Построить график F(X).{shift}'
    mx={0:q1*q2*q3,1:q1*q2*p3+q3*q2*p1+q1*q3*p2,2:p1*p2*q3+p1*p3*q2+p2*p3*q1,3:p1*p2*p3}
    MX=discr_math_expectation(mx)
    DX=discr_dispersion(mx)
    sigma=discr_standart_deviation(mx)
    values=list(mx.values())
    FX=(f'0, x<=0{shift}'
    f'{round(values[0],2)}, 0<x<=1{shift}'
    f'{round(values[0]+values[1],2)}, 1<x<=2{shift}'
    f'{round(values[2]+values[0]+values[1],2)}, 2<x<=3{shift}'
    f'{round(values[3]+values[0]+values[1]+values[2],2)}, x>3{shift}')
    answer=f'{ans} MX={MX}, DX={DX}, d={sigma},{shift} F(x)={FX}'
    text+=answer
    print(text)

def task_12():
    num=choice([4,5,6])
    p=choice([0.4,0.5,0.6])
    q=1-p
    mx=num*p
    dx=num*p*q

    text=f'Радиосигнал передан {num} раза. Вероятность приема одного из них равна {p}. Составить ряд распределения ' \
         f'числа передач, в которых сигнал будет принят. Найти ' \
         f'M(X) и D(X) этой случайной величины.{shift}'
    answer=f'{ans} MX={round(mx,2)}, DX={round(dx,2)}'
    text+=answer
    print(text)
def task_13():
    p=choice([0.01,0.02,0.03,0.04])
    n=choice([1000,800,2000])
    text=f'Вероятность выхода из строя электронной лампы,' \
         f'проработавшей t дней, равна 0,03. Аппаратура содержит ' \
         f'1000 ламп. Составить ряд распределения числа вышедших' \
         f'из строя ламп, проработавших t дней. Найти M(X) этой ' \
         f'случайной величины.{shift}'
    text+=f'{ans} MX={n*p}'
    print(text)

def task_14():
    text=f'Независимые случайные величины X и Y заданы таблицами ' \
         f'распределений.Найти:' \
         f'1) M(X), M(Y), D(X), D(Y);' \
         f'2) таблицы распределения случайных величин Z1 ' \
         f'= 2X+Y, Z2 = XY;' \
         f'3) M(Z1), M(Z2), D(Z1), D(Z2) непосредственно по таблицам ' \
         f'распределений и на основании свойств математического ' \
         f'ожидания и дисперсии.{shift}'
    mx={-1:0.1,1:0.5,2:0.4}
    xi=[]
    pxi=[]
    my={3:0.7,5:0.3}
    yi=[]
    pyi=[]
    for x,p in mx.items():
        xi.append(x)
        pxi.append(p)
    for x,p in my.items():
        yi.append(x)
        pyi.append(p)
    table=(f'{xi} {yi} {shift}'
           f'{pxi} {pyi}')
    text+=table
    MX=discr_math_expectation(mx)
    MY=discr_math_expectation(my)
    DX=discr_dispersion(mx)
    DY=discr_dispersion(my)
    answer=f'{ans} MX={MX}, MY={MY}, DX={DX}, DY={DY}{shift}{shift}'
    f'       MZ1={2*MX+MY}, MZ2={MX*MY}, DZ1={4*DX+DY}, DZ2={DX*DY+MX*MX*DY+MY*MY*DX}'
    text+=answer
    print(text)

