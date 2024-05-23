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

shift='\n'
#work
def task_1():
    answer='1. '
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
    answer+=f'а) 1/64 или {round((1/64),4)}; б) 1/19 или {round((1/19),4)}'
    return text,answer


#work
def task_2():
    answer = '2. '
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
    answer+=(f'а) C({variants[rand_country_1]},{invited})/C({sumof},{invited}); ' 
           f'б) С({russian},{from_rus})*C({bolgarian},{from_bol})*C({ukranian},{invited-from_bol-from_rus})/C({sumof},{invited})')

    return text,answer

#work
def task_3():
    answer='3. '
    pol_probability=randint(4,8)/10
    rus_probability=randint(4,8)/10
    while rus_probability==pol_probability:
        rus_probability=randint(4,8)/10
    answer=f'Ответ: а) {round(pol_probability*rus_probability,2)}; б) {round(1-(1-rus_probability)*(1-pol_probability),2)}; '
    text=(f'3. Российская певица дает автограф с вероятностью '
f'{rus_probability}, а польская — с вероятностью {pol_probability}. Какова вероятность '
f'того, что завтра после концерта с участием обеих звезд: \n'
f'а) вам удастся получить оба автографа;\n'
f'б) удастся получить хотя бы один автограф;\n')
    rand_task=randint(0,1)
    if rand_task==0:
        text+=f'в) не удастся получить автограф у польской певицы?\n'
        answer+=f'в) {round(1-pol_probability,2)}'
    else:
        text += f'в) не удастся получить автограф у российской певицы?\n'
        answer += f'в) {round(1 - rus_probability,2)}'

    return text,answer
#work
def task_4():
    answer = '4. '
    prob_1=randint(4,9)/10
    unp_1=round(1-prob_1)
    prob_2=randint(4,9)/10
    while prob_2==prob_1:
        prob_2=randint(4,9)/10
    unp_2=round(1-prob_2)
    text=(f'4. Две россиянки участвуют в международном конкурсе '
     f'по мировой экономике. Успешно пройти тур первая девушка '
     f"может с вероятностью {prob_1}, вторая — {prob_2}. Вчера прошел "
     f"третий, последний тур соревнований. Какова вероятность ")
    task_type=randint(0,1)
    if task_type==0:
        text+=(f'того, что у второй участницы успешно пройденных '
        f'туров больше, чем у первой? \n')
        answer+=f' {unp_1}*{prob_2}+{prob_1}*{unp_1}*{prob_2}*{prob_2}+{prob_1}*{prob_1}*{unp_1}*{prob_2}*{prob_2}*{prob_2} или {unp_1*prob_2+prob_1*unp_1*prob_2*prob_2+prob_1*prob_1*unp_1*prob_2**3}'
    else:
        text += (f'того, что у первой участницы успешно пройденных '
                 f'туров больше, чем у второй? \n')
        answer+= f' {unp_2}*{prob_1}+{prob_2}*{unp_2}*{prob_1}*{prob_1}+{prob_2}*{prob_2}*{unp_2}*{prob_1}*{prob_1}*{prob_1} или {unp_2 * prob_1 + prob_2 * unp_2 * prob_1 * prob_1 + prob_2 * prob_2 * unp_2 * prob_1 ** 3}'


    return text,answer
#work
def task_5():
    answer = '5. '
    text=(f'5. Из полного набора костей домино (28) наугад извлечена кость. Найти вероятность того, что вторую наугад'
f' взятую кость можно приставить к первой, если первая оказалась:{shift}'
f'а) дублем;{shift}'
f'б) не дублем.{shift}')
    answer+=f'a) 6/27 или {round(6/27,2)}; б) 12/27 или {round(12/27,2)}'
    print(text,answer)
    return text,answer


#work
def task_6():
    answer = '6. '
    prob_s=randint(4,9)/10
    prob_m=randint(1,3)/10

    prob_j=0
    uns=round(1-prob_s,1)
    unm=round(1-prob_m,1)

    unj=1
    vars={'':uns+unm+unj,' не':prob_j+prob_m+prob_s}
    no=choice(list(vars.keys()))
    text=f'6. Три брата посеяли пшеницу, однако «...в долгом времени  ' \
         f'аль вскоре приключилось с ними горе: кто-то в поле  ' \
         f'стал ходить да пшеницу шевелить. Наконец они смекнули  ' \
         f', чтоб стоять на карауле, хлеб ночами поберечь, злоговора  ' \
         f'подстеречь». В их деревне всем известно, что старший  ' \
         f'брат засыпает в дозоре с вероятностью {prob_s}, средний — {prob_m},  ' \
         f' а у младшего бессонница. Найти вероятность того, что  ' \
         f'в первую ночь{no} удастся поймать вора, если очередность  ' \
         f' дежурства определяется жребием.{shift}'
    answer+=f'{round((vars[no])/3,3)}'
    print(text,answer)
    return text,answer

#work
def task_7():
    answer = '7. '
    prob_1=randint(1,3)/10
    prob_2=randint(3,5)/10
    prob_3=round(1-prob_2-prob_1,1)
    sold_1=randint(1,4)/10
    sold_2=randint(2,7)/10
    sold_3=randint(5,9)/10
    sumof=round(prob_1*round((1-sold_1),1)+prob_2*round((1-sold_2),1)+prob_3*round((1-sold_3),1),1)
    vars={'в помещении театра':round(prob_1*round((1-sold_1),1),1),'на Тверской':round(prob_2*round((1-sold_2),1),1),'на «Пушкинской»':round(prob_3*round((1-sold_3),1),1)}
    rand_cash=choice(list(vars.keys()))
    text=f'7. Зритель с вероятностью {prob_1}, {prob_2} и {prob_3} соответственно ' \
         f'может обратиться за билетом в одну из трех театральных ' \
         f'касс Большого театра: в помещении театра, на Тверской  ' \
         f'и на станции метро «Пушкинская». Вероятность' \
         f'того, что к моменту прихода зрителя в кассе все билеты ' \
         f'будут проданы, соответственно равна {sold_1}, {sold_2} и {sold_3}.' \
         f'Поклонник Большого театра купил билет в одной из этих ' \
         f'трех касс. Какова вероятность того, что эта касса {rand_cash}?{shift}'
    answer+=f'{round(vars[rand_cash]/sumof,3)}'
    print(text,answer)
    return text,answer
#work
def task_8():
    answer = '8. '
    vars={'синий':5,'красный':45}
    vars_num={'три':3,'четыре':4,'два':2}
    kavo_num=choice(list(vars_num.keys()))
    kavo=choice(list(vars.keys()))
    text=f'8. В ящике имеется 5 синих и 45 красных шаров. Какова ' \
         f' вероятность того, что при десяти независимых выборах ' \
         f'с возвращением {kavo_num} раза будет выниматься {kavo} шар?{shift}'
    answer+=f'C(10,3)*({vars[kavo]}/50)^{vars_num[kavo_num]}*({50-vars[kavo]}/50)^{10-vars_num[kavo_num]}'
    print(text,answer)
    return text,answer
#work
def task_9():
    answer = '9. '
    prob=choice([0.25,0.3,0.4,0.2])
    km=randint(220,250)
    num=choice([50,60,70])

    x_num=(num-km*prob)/(math.sqrt(km*prob*(1-prob)))
    x_km=(km-km*prob)/(math.sqrt(km*prob*(1-prob)))
    x_0=(0-km*prob)/(math.sqrt(km*prob*(1-prob)))
    x_num=round(x_num,2)
    x_km=round(x_km,2)

    text=f'9. Вероятность переключения передач на каждом ' \
         f'километре трассы равна {prob}. Найти вероятность того, что ' \
         f'на {km}-километровом участке этой трассы переключение ' \
         f'передач произойдет: {shift}' \
         f'а) {num} раз;{shift}'
    task=randint(0,1)
    if task==0:
         text+=f'б) не более {num} раз.{shift}'

         answer+=f'a){round((float(local_lapl(x_num))/math.sqrt(km*prob*(1-prob))),5)} б){round(integr_lapl(x_num)-integr_lapl(x_0),4)}'

    else:
         text+=f'б) не менее {num} раз.{shift}'
         answer+= f'a){round(float(local_lapl(x_num)) / math.sqrt(km * prob * (1 - prob)), 5)} б){round(integr_lapl(x_km)-integr_lapl(x_num),4)}'

    print(text,answer)
    return text,answer
#work
def task_10():
    answer = '10. '
    safety=choice([0.001,0.002,0.004])
    vars={'двух':2,'трех':3,'четырех':4}
    quantity=choice(list(vars.keys()))
    x_0=(0-100*safety)/math.sqrt(safety*(1-safety)*100)
    text=f'10. Вероятность выхода из строя во время испытания ' \
         f'на надежность любого из однотипных приборов равна ' \
         f'{safety}. Найти вероятность того, что в партии из 100 ' \
         f' приборов во время испытания выйдут из строя не более {quantity} ' \
         f'приборов.{shift}'
    num=vars[quantity]
    x_num=(num-safety*100)/math.sqrt(safety*(1-safety)*100)
    answer+=f'{round(integr_lapl(round(x_num,2))-integr_lapl(round(x_0,2)),4)}'

    print(text,answer)
    return text,answer
#work
def task_11():
    answer = '11. '
    p1=randint(2,4)/10
    p2=randint(4,6)/10
    p3=randint(6,8)/10
    q1=round(1-p1,1)
    q2=round(1-p2,1)
    q3=round(1-p3,1)
    print(q1)

    text=f'11. Производится три независимых выстрела. Вероятность ' \
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
    answer+=f'MX={MX}, DX={DX}, d={sigma},{shift} F(x)={FX}'
    print(text,answer)
    return text,answer
#work
def task_12():
    answer = '12. '
    num=choice([4,5,6])
    p=choice([0.4,0.5,0.6])
    q=1-p
    mx=num*p
    dx=num*p*q

    text=f'12. Радиосигнал передан {num} раза. Вероятность приема одного из них равна {p}. Составить ряд распределения ' \
         f'числа передач, в которых сигнал будет принят. Найти ' \
         f'M(X) и D(X) этой случайной величины.{shift}'
    answer+=f'MX={round(mx,2)}, DX={round(dx,2)}'
    print(text,answer)
    return text,answer
#work
def task_13():
    answer = '13. '
    p=choice([0.01,0.02,0.03,0.04])
    n=choice([1000,800,2000])
    text=f'13. Вероятность выхода из строя электронной лампы,' \
         f'проработавшей t дней, равна {p}. Аппаратура содержит ' \
         f'{n} ламп. Составить ряд распределения числа вышедших' \
         f'из строя ламп, проработавших t дней. Найти M(X) этой ' \
         f'случайной величины.{shift}'
    answer+=f'MX={n*p}'
    print(text,answer)
    return text,answer

#work
def task_14():
    answer = '14. '
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
    table=(f'X: {xi} \t\t Y: {yi} {shift}'
           f'px: {pxi} py: {pyi}')
    text+=table
    MX=discr_math_expectation(mx)
    MY=discr_math_expectation(my)
    DX=discr_dispersion(mx)
    DY=discr_dispersion(my)
    answer+=(f'MX={MX}, MY={MY}, DX={DX}, DY={DY}{shift}' 
    f'       MZ1={2*MX+MY}, MZ2={MX*MY}, DZ1={4*DX+DY}, DZ2={DX*DY+MX*MX*DY+MY*MY*DX}')
    print(text,answer)
    return text,answer


#INTEGRALCHIKI
#work
def task_15():
    task = "15. "

    a = -randint(7, 10) / 10
    b = randint(6, 10) / 10

    F = "\t__________\n"
    F += "\t| 0\t\t, x≤-2\t\tα = " + str(a) + "\n"
    F += "F(X) =| x/4+1/2\t, -2<x≤2\tβ = " + str(b) + "\n"
    F += "\t| 1\t\t, 2<x\n"
    F += "\t‾‾‾‾‾‾‾‾‾‾"

    task += "Дана функция распределения F(x) непрерывной случайной величины X.\nТребуется:\n"
    task += "\t1) найти плотность вероятности f(x);\n"
    task += "\t2) построить графики F(x) и f(x);\n"
    task += "\t3) найти M(X), D(X), σ(Х);\n"
    task += "\t4) найти Р(α < X < β) для данных α, β.\n"
    task += F

    answer = "15. "

    f = "\t__________\n"
    f += "\t| 0\t\t, x≤1\n"
    f += "f(X) =| 1/4\t, 1<x≤2\n"
    f += "\t| 0\t\t, 2<x\n"
    f += "\t‾‾‾‾‾‾‾‾‾‾\n"

    answer += "1)" + f
    answer += "3) M(x) = 0\tD(x) = 1.34\tσ(x) = 1.15\n"
    answer += "4) P(" + str(a) + "<x<" + str(b) + ") = F(" + str(b) + ")-F(" + str(a) + ") = " + str(
        round((b-a) / 4, 3)) + "\n"

    print(task,answer)
    return task,answer

#work
def task_16():
    task = "16. "

    a = randint(-7,0)
    b = randint(5,7)

    f = "\t__________\n"
    f += "\t| 0\t\t, x≤1\t\tα = " + str(a) + "\n"
    f += "f(X) =\t| 2 / 9\t, 1<x≤4\tβ = " + str(b) + "\n"
    f += "\t| 2(7-x)/27\t, 4<x≤7\n"
    f += "\t| 0\t\t, 7<x\n"
    f += "\t‾‾‾‾‾‾‾‾‾‾\n"

    task += "Дана плотность вероятности f(x) непрерывной случайной величины X, имеющая две ненулевые составляющие формулы.\nТребуется:\n"
    task += "\t1) проверить свойство: интеграл f(x) на промежутке (-∞,+∞) = 1 ;\n"
    task += "\t2) построить график f(x);\n"
    task += "\t3) найти функцию распределения F(x)\n"
    task += "\t4) найти Р(α < X < β) для данных α, β.\n"
    task += "\t5) найти М(Х), D(X), σ(X).\n"
    task += f

    answer = "16. "

    F = "\t__________\n"
    F += "\t| 0\t\t, x≤1\n"
    F += "F(X) =\t| (x^2+12x+36)/18, 1<x≤4\n"
    F += "\t| (14x-7x^2)/27\t, 4<x≤7\n"
    F += "\t| 1\t\t, 7<x\n"
    F += "\t‾‾‾‾‾‾‾‾‾‾\n"

    answer += "1) свойство выполняется\n"
    answer += "3) " + F
    answer += "4) P(" + str(a) + "<x<" + str(b) + ") = F(" + str(b) + ")-F(" + str(a) + ") = " + str(
        round(2/3+(14*(b-4)-b*b+16)/27, 3)) + "\n"
    answer += "5) M(X) = 5.8\tD(X) = 7.36\tσ(X) = 2.71\n"

    print(task,answer)
    return task,answer

#work
#CHAPTER 7
def task_17():
    answer = '17. '
    MX=choice([60,50,40])
    DX=choice([250,160,360])
    text=f'17. Случайная величина X имеет нормальный закон ' \
         f'распределения (MX = {MX}; DX = {DX}). Найти вероятность ' \
         f'события X ∈ (10, 60).{shift}'
    num_ans=integr_lapl(round((60-MX)/math.sqrt(DX),2))-integr_lapl(round((10-MX)/math.sqrt(DX),2))

    answer+=f'{round(num_ans,2)}'
    print(text,answer)
    return text,answer
#work
def task_18():
    answer = '18. '
    mist=[0.01,0.02,0.03,0.04]
    m=choice(mist)
    print(m)
    text=f'18. Цена деления шкалы амперметра равна 0,1 А. ' \
         f'Показания определяют с точностью до ближайшего деления. ' \
         f'Найти вероятность того, что при отсчете будет сделана ' \
         f'ошибка \u03B5, превышающая {m} А.{shift}'
    answer+=f'{round(10*(0.1-2*m),2)}'
    print(text,answer)
    return text,answer
#work
def task_19():
    answer = '19. '
    MX = choice([10, 15, 20])
    d=choice([1.5,2.0,3.0])
    wait=choice([12,16,20])
    text=f'Период накопления состава на сортировочной станции ' \
         f' имеет нормальное распределение с параметрами:' \
         f'm = {MX} ч и  = {d} ч. С какой вероятностью период  ' \
         f'накопления очередного состава окажется более {wait} ч?{shift}'
    num_ans=round(0.5-integr_lapl(round((wait-MX)/d,2)),4)
    answer+=f' {num_ans}'
    print(text,answer)
    return text,answer
#work
#Chapter 8
def task_20():
    answer = '20. '
    amper=randint(20,30)
    hour=choice([200,190,210])
    text=f'20. Батарея состоит из 70 аккумуляторов, заряд Qi каждого ' \
         f'из них, измеряемый в ампер-часах, имеет «треугольное» ' \
         f' распределение с плотностью вероятности: {shift}' \
         f'\tf(q)= -q/1250+2/25 при 50<q<100{shift}' \
         f'и не зависит от других аккумуляторов. Выполнить грубую ' \
         f'оценку вероятности того, что батарея способна обеспечить' \
         f' ток {amper} А в течение {hour} ч. Каков средний заряд отдельного аккумулятора?{shift}'
    sr=amper*hour/70
    print(sr)
    answer+=f'MX=66.7 P={round((-10000/2500+2*100/25)-(-sr*sr/2500+2*sr/25),2)}'
    print(text,answer)
    return text,answer


