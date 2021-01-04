import numpy as np

def game_core_v1(number):
    '''Просто угадываем на random, никак не используя информацию о больше
    или меньше. Функция принимает загаданное число и возвращает
    число попыток.'''
    # Счетчик попыток
    count = 0

    while True:
        count += 1
        predict = np.random.randint(1, 101)  # предполагаемое число
        if number == predict:
            return (count)  # выход из цикла, если угадали


def game_core_v2(number):
    '''Сначала устанавливаем любое random число, а потом уменьшаем или
    увеличиваем его в зависимости от того, больше оно или меньше нужного.
    Функция принимает загаданное число и возвращает число попыток.'''
    # Счетчик попыток
    count = 1
    predict = np.random.randint(1, 101)

    while number != predict:
        count += 1
        if number > predict:
            predict += 1
        elif number < predict:
            predict -= 1
    return (count)  # выход из цикла, если угадали


def half_devision(number):
    '''Начнем с 50 и далее в зависимости от того, меньше искомое число
    или больше, будем брать половину от "левого" отрезка или "правого",
    соответственно, постепенно сужая границы. Функция принимает загадан-
    ное число и возвращает число попыток.'''
    # Счетчик попыток
    count = 1

    # Левая и правая граница для поиска (шире на 1, чем диапазон)
    left_side = 0
    right_side = 101

    # Пытаемся угадать с первого раза -)
    predict = 50

    # Цикл повторяется, пока не будет угадано число
    while number != predict:
        # Если мы тут, значит не угадали. Увеличиваем счетчик на 1
        count += 1
        # Если искомое больше, левый край отрезка смещаем
        if number > predict:
            left_side = predict
            # Если искомое меньше, правый край отрезка смещаем
        elif number < predict:
            right_side = predict
        # Предсказываем число, взяв середину отрезка
        predict = left_side + int((right_side - left_side) / 2)
        # Две строки для отладки. Раскомментируйте для отражения параметров
        # print(f'{left_side} -left_side, {right_side} -right_side,
        # {(right_side-left_side)/2} -пополам, {predict} -прогноз')
    return (count)


def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро в среднем игра угадывает
    число'''
    count_ls = []
    np.random.seed(1)  # фиксируем генератор случ. чисел для объективности
    random_array = np.random.randint(1, 101, size=(1000))

    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return (score)

score_game(half_devision)