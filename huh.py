import math
from random import randint
from random import choice
from random import uniform
from functions import local_lapl
from functions import integr_lapl
from functions import discr_math_expectation
from functions import discr_dispersion
from functions import discr_standart_deviation
shift='\n'
def task_20():
    x=choice([4450,4500,4550])
    n1=30
    n2=22
    n3=28
    m1=60
    m2=48
    m3=56
    s1=6
    s2=12
    s3=9
    text=f'20. Состав содержит 30 полувагонов, 22 вагона и 28 хоппердозаторов. ' \
         f'Массы полувагонов распределены в диапазоне ' \
         f'(60{chr(0x000000B1)}6) т, массы вагонов — в диапазоне (48{chr(0x000000B1)}12) т, а ' \
         f'массы хоппердозаторов имеют распределение в диапазоне ' \
         f'(56{chr(0x000000B1)}9) т. Один локомотив способен везти состав массой' \
         f' не более {x} т, иначе необходим второй. Какова вероятность' \
         f' того, что второй локомотив не потребуется?{shift}'
    mx=n1*m1+n2*m2+n3*m3
    dx=n1*(s1/3)**2+n2*(s2/3)**2+n3*(s3/3)**2
    x1 = round((x-mx)/dx**0.5,2)
    x2 = round((0 - mx) / dx ** 0.5,2)
    answer=f'20. {round(integr_lapl(x1)-integr_lapl(x2),4)}'
    print(text,answer)
    return(text,answer)

def task_19():
    m=choice([70,80,90])
    s=choice([5,6,7])
    n=choice([85,90,95])
    text=f'19. Число вагонов в прибывающем на расформирование ' \
         f'составе — нормальная случайная величина с математическим' \
         f' ожиданием m = {m} и σ = {s}. Какова вероятность ' \
         f'того, что в очередном составе будет не менее {n} вагонов?{shift}'
    x2=1000000
    x1=round((n-m)/s,2)
    answer=f'19. {round(integr_lapl(x2)-integr_lapl(x1),6)}'
    print(text,answer)
    return text,answer

def task_18():
    m=randint(5,10)
    s=randint(1,10)
    text=f'18. Станок(автомат изготавливает ролики, контролируя' \
         f' их диаметр D. Считая, что величина D распределена ' \
         f'нормально (m = {m} см; σ = {s} мм), найти интервал, в который' \
         f' с вероятностью 0,9973 попадут диаметры роликов.{shift}'
    answer=f'18. [{m-3*s*0.01},{m+3*s*0.01}]'
    print(text,answer)
    return text,answer

def task_17():
    k=choice([0.001,0.002,0.003])
    h=randint(900,1100)
    text=f'17. Время T безотказной работы телевизора распределено' \
      f' по показательному закону с плотностью {shift}' \
      f'f(t) = {k}e^(–{k}t) (t > 0).{shift}' \
      f'Найти вероятность того, что телевизор проработает без ' \
      f'отказа не менее {h} ч.{shift}'
    answer=f'17. {round(1-(1-math.exp(-k* h)),4)}'
    print(text,answer)
    return text,answer

def task_16():
    task = "16. "

    a = choice([0.5,1,1.5])
    b = choice([2.25,2.5,2.75])

    f = "\t__________\n"
    f += "\t| 0\t\t, x≤0\t\tα = " + str(a) + "\n"
    f += "f(X) =\t| (3/20)x^2\t, 0<x≤2\tβ = " + str(b) + "\n"
    f += "\t| 3/5\t, 2<x≤3\n"
    f += "\t| 0\t\t, 3<x\n"
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
    F += "\t| 0\t\t, x≤0\n"
    F += "F(X) =\t| (1/20)x^3, 0<x≤2\n"
    F += "\t| (3/5)x\t, 2<x≤3\n"
    F += "\t| 1\t\t, 3<x\n"
    F += "\t‾‾‾‾‾‾‾‾‾‾\n"

    answer += "1) свойство выполняется\n"
    answer += "3) " + F
    answer += "4) P(" + str(a) + "<x<" + str(b) + ") = F(" + str(b) + ")-F(" + str(a) + ") = " + str(
        round(0.6*(b-2)+0.05*(8-a**3), 3)) + "\n"
    answer += "5) M(X) = 2.1\tD(X) = 0.35\tσ(X) = 0.59\n"

    print(task, answer)
    return task, answer

def task_15():
    task = "15. "

    a = randint(1, 5) / 10
    b = randint(6, 10) / 10

    F = "\t__________\n"
    F += "\t| 0\t\t, x≤0\t\tα = " + str(a) + "\n"
    F += "F(X) =| (x^2+x)/2\t, 0<x≤1\tβ = " + str(b) + "\n"
    F += "\t| 1\t\t, 1<x\n"
    F += "\t‾‾‾‾‾‾‾‾‾‾"

    task += "Дана функция распределения F(x) непрерывной случайной величины X.\nТребуется:\n"
    task += "\t1) найти плотность вероятности f(x);\n"
    task += "\t2) построить графики F(x) и f(x);\n"
    task += "\t3) найти M(X), D(X), σ(Х);\n"
    task += "\t4) найти Р(α < X < β) для данных α, β.\n"
    task += F

    answer = "15. "

    f = "\t__________\n"
    f += "\t| 0\t\t, x≤0\n"
    f += "f(X) =| x + 1/2\t, 0<x≤1\n"
    f += "\t| 0\t\t, 1<x\n"
    f += "\t‾‾‾‾‾‾‾‾‾‾\n"

    answer += "1)" + f
    answer += "3) M(x) = 7/12 или 0.58\tD(x) = 11/144 или 0.76\tσ(x) = 0.276\n"
    answer += "4) P(" + str(a) + "<x<" + str(b) + ") = F(" + str(b) + ")-F(" + str(a) + ") = " + str(
        round((b**2+b-a**2-a) / 2, 3)) + "\n"

    print(task,answer)
    return task,answer

def task_14():
    answer = '14. '
    text = f'14. Независимые случайные величины X и Y заданы таблицами ' \
           f'распределений.Найти:' \
           f'1) M(X), M(Y), D(X), D(Y);' \
           f'2) таблицы распределения случайных величин Z1 ' \
           f'= 2X+Y, Z2 = XY;' \
           f'3) M(Z1), M(Z2), D(Z1), D(Z2) непосредственно по таблицам ' \
           f'распределений и на основании свойств математического ' \
           f'ожидания и дисперсии.{shift}'
    mx = {1: 0.5, 2: 0.3, 3: 0.2}
    xi = []
    pxi = []
    my = {-1: 0.2, 4: 0.8}
    yi = []
    pyi = []
    for x, p in mx.items():
        xi.append(x)
        pxi.append(p)
    for x, p in my.items():
        yi.append(x)
        pyi.append(p)
    table = (f'X: {xi} \t\t Y: {yi} {shift}'
             f'px: {pxi} py: {pyi}{shift}')
    text += table
    MX = discr_math_expectation(mx)
    MY = discr_math_expectation(my)
    DX = discr_dispersion(mx)
    DY = discr_dispersion(my)
    answer += (f'MX={MX}, MY={MY}, DX={DX}, DY={DY}{shift}'
               f'       MZ1={2 * MX + MY}, MZ2={MX * MY}, DZ1={round(4 * DX + DY,2)}, DZ2={DX * DY + MX * MX * DY + MY * MY * DX}')
    print(text, answer)
    return text, answer

def task_13():
    n=choice([400,500,600])
    p=choice([0.0025,0.003,0.001,0.002])
    text=f'13. Книга содержит {n} страниц. Вероятность сделать ' \
         f'опечатку на одной странице равна {p}. Составить ' \
         f'ряд распределения числа опечаток на одной странице, если в книге ' \
         f'их 400. Найти M(X) числа опечаток на одной странице.{shift}'
    answer=f'13. MX={n*p}'
    print(text,answer)
    return text,answer

def task_12():
    k=randint(3,10)
    p=randint(10,20)/100
    pp=0.1
    q=0.9
    text=f'12. Партия, насчитывающая {round(p*1000)} швейных машин, содержит {round(p*100)} бракованных. Из всей' \
         f' партии с целью проверки качества случайным образом ' \
         f'отбирается {k} швейных машин. Составить ряд распределения ' \
         f'числа бракованных машин среди отобранных. ' \
         f'Найти M(X) и D(X) этой случайной величины.{shift}'
    answer=f'12. M(X)={round(k*pp,4)} D(X)={round(pp*k*q,4)}'
    print(text,answer)
    return text,answer

