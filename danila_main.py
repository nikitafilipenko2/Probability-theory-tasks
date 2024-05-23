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

shift = '\n'


# work F
def task_1():
    answer = '1. '
    variants = ['первого', 'второго', 'третьего', 'четвертого']
    race_length = randint(90, 120)
    loser_place = variants[randint(0, len(variants) - 1)]
    first_place = variants[randint(0, len(variants) - 1)]
    variants.remove(first_place)
    second_place = variants[randint(0, len(variants) - 1)]
    variants.remove(second_place)
    third_place = variants[randint(0, len(variants) - 1)]
    text = (f'1. В финальном забеге на {race_length} м участвуют по'
            f'два студента с четырех курсов. Найти вероятность того, что:\n'
            f'а) Первым пробежит дистанцию студент {first_place} курса,'
            f'вторым - студент {second_place}  третьим - студент {third_place} курса;\n'
            f'б) В тройке призеров не будет студентов {loser_place} курса;\n')
    answer += f'а) 1/42 или {round((1 / 42), 4)}; б) 5/14 или {round((5 / 14), 4)}'
    print(text, answer)
    return text, answer


# work raz
def task_2():
    answer = '2. \n'
    numbers = ['ноль', 'одно', 'два', 'три', 'четыре', 'пять', 'шесть']
    types_number = randint(3, 6)
    student_choice_number = randint(3, 6)
    first_number = randint(2, types_number)
    second_number = randint(2, student_choice_number - 1)
    third_number = student_choice_number - second_number
    text = (f'2. В студенческой столовой на обед предлагается по {types_number} вида '
            f'салатов, первых и вторых блюд. Студент, как обычно, берет на обед '
            f'{student_choice_number} блюд. Найти вероятность того, что он взял:\n'
            f'а) {numbers[first_number]} салата; \n'
            f'б) {numbers[second_number]} первых и {numbers[third_number]} вторых блюда\n')
    calculation1 = 1
    n = 3 * types_number
    i = first_number
    j = n - i
    while i >= 1:
        calculation1 *= i / n
        i -= 1
        n -= 1
    while n > j:
        calculation1 *= j / n
        j -= 1
        n -= 1

    calculation2 = 1
    n = 3 * types_number
    i = second_number
    j = third_number
    for _ in range(student_choice_number):
        if i > 0:
            calculation2 *= i / n
            i -= 1
        else:
            calculation2 *= j / n
            j -= 1
        n -= 1

    answer += (f'а) {round(calculation1, 5)}\n'
               f'б) {round(calculation2, 5)}\n')
    print(text, answer)
    return text, answer




# work F
def task_3():
    answer = '3. '
    prob_1 = randint(4, 9) / 10
    prob_2 = randint(4, 9) / 10
    while prob_2 == prob_1:
        prob_2 = randint(4, 9) / 10
    text = (f'3. В поликлинике работают два психолога. Первый правильно определяет '
            f'профессиональные наклонности детей с вероятностей {prob_1}, второй - '
            f"с вероятностью {prob_2}. Для большей надежности мама с ребенком посетила"
            f"обоих психологов. Какова вероятность того, что\n"
            f'а) профессиональные наклонности ребенка оба специалиста определят правильно;\n'
            f'б) хотя бы один из них ошибется;\n'
            f'в) ошибочные рекомендации даст второй психолог?\n')
    answer += (f'а) {round(prob_1 * prob_2, 4)}; '
               f'б) {round((1 - prob_1) * (1 - prob_2) + (1 - prob_1) * prob_2 + prob_1 * (1 - prob_2), 4)}; '
               f'в) {round((1 - prob_1) * (1 - prob_2) + prob_1 * (1 - prob_2), 4)}')
    print(text, answer)
    return text, answer


# work F
def task_4():
    p1 = randint(4, 9) / 10
    p2 = randint(4, 9) / 10
    while p1 == p2:
        p2 = randint(4, 9) / 10
    z1 = randint(4, 9) / 10
    z2 = randint(4, 9) / 10
    while z1 == z2:
        z2 = randint(4, 9) / 10
    calculation = (1 - p1) * (1 - z1) * (p2 * (1 - z2) + (1 - p2) * z2 + p2 * z2) * (p1 * (1 - z1) + p1 * z1) * (
            p2 * z2)
    calculation = round(calculation, 4)
    answer = '4. '
    text = (f'4. Инженер-электронщик и киноартист пытаются пополнить ряды космонавтов.'
            f'С вероятностью {p1} и {p2} соответственно они успешно проходят тест по специальности,'
            f'с вероятностью {z1} и {z2} - по физической подготовке. Какова вероятность того, что'
            f'киноартист успешно пройдет тестов больше, чем инженер-электронщик?\n')
    answer += f'{calculation}'
    print(text, answer)
    return text, answer


# work F
def task_5():
    answer = '5. '
    all_cards = 36
    cards_quantity = randint(2, 4)
    text = (f'5. В колоде {all_cards} карт. Наугад извлекают {cards_quantity} карты. Найти вероятность того, что'
            f' вторым вынут туз, если первым тоже вытянут туз\n')
    answer += f'{cards_quantity}/{all_cards}'
    print(text, answer)
    return text, answer


# work F
def task_6():
    answer = '6. '
    part1 = randint(10, 51)
    part2 = randint(10, 41)
    part3 = 100 - part1 - part2
    nekach_prob1 = randint(1, 6) / 10
    nekach_prob2 = randint(1, 6) / 10
    nekach_prob3 = randint(1, 6) / 10
    text = (f'6. В фотоателье работают три оператора, каждый из которых печатает '
            f'соответственно {part1}, {part2}, {part3}% всей продукции. Вероятность того, что фотография'
            f' будет некачественной, для первого оператора равна {nekach_prob1}, для второго - {nekach_prob2},'
            f' для третьего - {nekach_prob3}. Вы не знаете, к какому из операторов попала ваша фотопленка'
            f'с портретом любимой бабушки. Какова вероятность того, что вы, получив снимок, узнаете на нем свою бабушку?\n'
            )
    part1 /= 100
    part2 /= 100
    part3 /= 100
    answer += f'{round(part1 * (1 - nekach_prob1) + part2 * (1 - nekach_prob2) + part3 * (1 - nekach_prob3), 4)}'
    print(text, answer)
    return text, answer


# work F
def task_7():
    answer = '7. '
    prob_1 = randint(1, 5) / 10
    prob_2 = randint(1, 4) / 10
    prob_3 = 1 - prob_1 - prob_2

    prob_4 = randint(1, 8) / 10
    prob_5 = randint(1, 8) / 10
    prob_6 = randint(1, 8) / 10

    variants = ['эпическим', 'любовным', 'лирическим']
    choice_number = randint(0, len(variants))
    otveti = [prob_3 * prob_6, prob_2 * prob_5, prob_1 * prob_4]
    text = (f'7. Студента Зевского на лекциях по математике посещают музы: Евтерпа(муза лирической поэзии) '
            f'- с вероятностью {prob_1}; Эрато(муза любовной поэзии) - с вероятностью {prob_2} и '
            f'Каллиопа(муза эпической поэзии) - с вроятностью {prob_3}. Извечтно, что после посещения '
            f'соответствующей музы Зевский лирические стихи сочиняет с вероятностью {prob_4}, любовные - '
            f'с вероятностью {prob_5} и эпические - с вероятностью {prob_6}. Какова вероятность того, что '
            f'написанное Зевским на очередной лекции стихотворение было {variants[choice_number]}?\n')
    answer += f'{round(otveti[choice_number], 4)}'
    print(text, answer)
    return text, answer


# work F
def task_8():
    answer = '8. '
    prob = choice([0.25, 0.3, 0.4, 0.2, 0.45, 0.5, 0.55, 0.6])
    shots_text = ['ноль', 'одно', 'два', 'три', 'четыре', 'пять', 'шесть']
    shots_number = randint(1, len(shots_text) - 1)
    popal_text = ['ноля', 'одного', 'двух', 'трех', 'четыреч', 'пяти', 'шести']
    popal_number = randint(1, shots_number)

    text = (f'8. Для стрелка, выполняющего упражнение в тире, вероятность попасть в "яблочко" при одном'
            f' выстреле не зависит от результатов предшествующих выстрелов и равна {prob}. Спортсмен '
            f'сделал {shots_text[shots_number]} выстрелов. Найти вероятность не менее {popal_text[popal_number]} попаданий.\n')
    answer += f'{round(combination(shots_number, popal_number)[1] * pow(prob, popal_number) * pow(1 - prob, shots_number - popal_number), 4)}'

    print(text, answer)
    return text, answer


# work
def task_9():
    answer = '9. '
    p = randint(70, 90)
    n = choice([100, 200, 300, 400, 500])
    prob_3 = randint(n - 60, n)
    prob_2 = randint(n - 70, prob_3 - 5)

    text = (f'9. Фабрика выпускает в среднем {p}% продукции первого сорта. Какова вероятность того, что '
            f'в партии из {n} изделий окажется:\n'
            f'а) не менее {prob_2} и не более {prob_3} изделий первого сорта;\n'
            f'б) ровно половина таких изделий?\n')

    p /= 100
    x_prob_2 = (prob_2 - n * p) / math.sqrt(n * p * (1 - p))
    x_prob_3 = (prob_3 - n * p) / math.sqrt(n * p * (1 - p))
    answer += (f'а) {round(integr_lapl(round(x_prob_3, 2)) - integr_lapl(round(x_prob_2, 2)), 5)} '
               f'б) {float(local_lapl((n / 2 - n * p) / math.sqrt(n * p * (1 - p)))) / math.sqrt(n * p * (1 - p))}')

    print(text, answer)
    return text, answer





# work F
def task_10():
    answer = '10. '
    p = randint(5, 30)
    n = randint(50, 100)
    k_text = ['ноль', 'один', 'два', 'три', 'четыре', 'пять', 'шесть']
    k = randint(2, len(k_text) - 1)

    text = (f'10. Известно, что в среднем {p}% носят очки. Какова вероятность того, что из {n} студентов '
            f'сидящих в аудитории, окажутся {k_text[k]} пользующихся очками?\n')
    p /= 100
    calc = local_lapl((k - n * p) / math.sqrt(n * p * (1 - p)))
    print(calc)
    answer += f'{round(float(calc) / math.sqrt(n * p * (1 - p)), 4)}'
    print(text, answer)
    return text, answer

def task_11():
    pass

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