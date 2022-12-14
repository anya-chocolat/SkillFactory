# Вариант игры "Угадай число" с рекурсией
import numpy as np


# Объявляем функцию с изначальными значениями минимума и максимума
# и пустым счётчиком попыток по умолчанию
def game_core_v4(num, low=1, high=101, count=0):
    count += 1  # Каждую попытку добавляем в счётчик
    guess = (low + high) // 2  # Угадываем с середины
    if guess == num:  # Условие для остановки рекурсии - если число угадано,
        return count  # то получаем количество попыток, использованное в этой игре
    elif guess < num:  # Если же наше число меньше угаданного,
        # То запускаем эту же функцию с нашим числом в качестве минимума и с текущим счётчиком попыток
        return game_core_v4(num, guess, high, count)
    # В противном случае запускаем эту же функцию с нашим числом в качестве максимума и с текущим счётчиком попыток
    else:
        return game_core_v4(num, low, guess, count)


# Проверка скорости угадывания на 1000 игр
def score_game(game_core):
    count_ls = []
    np.random.seed(2)
    random_array = np.random.randint(1, 101, size=10)
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    return score


# Запускаем функцию тестирования с функцией game_core_v4 в качестве аргумента и печатаем результат
print(f"Ваш алгоритм угадывает число в среднем за {score_game(game_core_v4)} попыток.")
# Ваш алгоритм угадывает число в среднем за 5 попыток.
