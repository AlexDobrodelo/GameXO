import os

def init_size_square(size_square):  # Функция генерации пустого игрового поля с номерами строк и столбцов
        result = []
        result = [['-' for i in range(size_square+1)] for j in range(size_square+1) ] # генерируем пустоеигровое поле
        result[0] =[' '] +  [i for i in range(1, size_square+1)]     # Записываем номера столбцов, первая ячейка " ", т.к находится над номерами строк
        for i in range(1, size_square+1):       # Проходимся по нулевым позициям строк
            result[i][0] = i                    # Записываем номера строк в нулевые ячейки
        return result

def print_pole(square):    # Печать игрового поля.
    os.system('cls')
    size = len(square)     # Игровое поле может быть различного размера.
    for i in range(size):  # В цикле печатаем игровое поле построчно.
        str_pole = ''
        for j in range(size):   # Форимуем строку игрового поля по ячейкам
            str_pole += ' ' + str(square[i][j]) + ' |'    # пробел перед значением ячейки и ' |' в конце
        print(str_pole)           # Печатаем сформированую строку
        print ('----' * size)     # печать гор.линии с учетом размерности поля
    return

def input_step(gamer): # ввод и проверка координат хода
    print(f'Игрок {gamer} введите координаты вашего хода')
    cell_no_busy = True
    while cell_no_busy:     # Бесконечный цикл пока не ввод не будет коректный
        x, y = map(int, input('Введите номер строки и через пробел номер столбца :>').split(" "))
        if not (0 < x < (len(game_square))  and 0 < y < (len(game_square))): # Проверка введеных координат
            print(f'{gamer}, вы ввели не верные координаты,"\n"' # на соответствие максимальных и минимальных диапазонов,
                  f'значения столбца и строки могут быть в '     # координаты не должны выходить на пределы игрового поля
                  f'диаразоне от 1 до {len(game_square)-1}.')
        elif game_square[x][y] != '-':   # Проверка свободной ячейки
            print(f'{gamer}, эта клетка занята, выберите другую.')
        else:
            cell_no_busy = False
            return x, y

def control(square):   # Проверка условий победы
    pattern_0 = ['O' for i in range(size_square)]  # Необходимое количество подряд O для игрока №1
    pattern_1 = ['X' for i in range(size_square)]  # Необходимое количество подряд X для игрока №2
    for i in range(1, size_square+1):   # Проверка по строкам и по столбцам
        if square[i][1:] == pattern_0 or [square[j][i] for j in range(1, size_square+1)] == pattern_0: # Проверка на 0
            game_end = True  # Конец игры
            winner = 0       # Выиграли 0 (игрок №1)
            return  game_end, winner
        elif square[i][1:] == pattern_1 or [square[j][i] for j in range(1, size_square+1)] == pattern_1: # Проверка на 1
            game_end = True   # Конец игры
            winner = 1        # Выиграли 1 (игрок №2)
            return  game_end, winner
        # Проверка по диагоналям на 0
    if [square[i][i] for i in range(1, size_square+1)] == pattern_0 \
            or [square[i][size_square + 1 - i] for i in range(1, size_square + 1)] == pattern_0:
        game_end = True       # Конец игры
        winner = 0            # Выиграли 0 (игрок №1)
        return  game_end, winner
        # Проверка по диагоналям на 1
    elif [square[i][i] for i in range(1, size_square+1)] == pattern_1 \
              or [square[i][size_square + 1 - i] for i in range(1, size_square + 1)] == pattern_1:
        game_end = True       # Конец игры
        winner = 1            # Выиграли 1 (игрок №1)
        return  game_end, winner
        # Иначе игра продолжается, победибеля нет
    else:
        game_end = False    # Игра продолжается
        winner = None       # Победителя нет
        return  game_end, winner



gamers = [1, 2]     # Список с и менами игроков. По умолчанию имена игроков  "1" и "2"

if str.lower(input('Для сохранения имен игроков введите "Y", иначе "N" :>')) == 'y':
    print()
    gamers[0] = str(input('Игрок №1 введите свое имя :>'))
    gamers[1] = str(input('Игрок №2 введите свое имя :>'))

size_square = int(input('''\nВведите размер игрового поля
3 для поля 3х3, 4 для поля 4х4, 5 для поля 5х5 и т.д.
поле неможет быть меньше 3 и больше 6 :>'''))

game_square = init_size_square(size_square) # Генерируем игровое поле

print_pole(game_square)  # Выводим пустое поле

for step in range(size_square ** 2):  # Запрашиываем ходы в цикле, максиммум шагов = количеству ячеек игрового поля
    if step % 2 == 0:
        id_gamer = 0      # Четные шаги выполняет игрок №1 
        gamer_char = 'O'  # Ходам игрока №1 присваиваем 'O'
    else:
        id_gamer = 1      # Нечетные шаги выполняет игрок №2,
        gamer_char = 'X'  # его ходам присваиваем 'X'

    x, y = input_step(gamers[id_gamer]) # получаем координаты хода текущего игрока
    game_square[x][y] = gamer_char        # записываем ход текущего игрока в соответствующую ячейку поля
    print_pole(game_square)             # выводим игровое поле после хода игрока
    game_stop, winner  = control(game_square)  # Проверяем выигрышные позиции
    if game_stop:
        print(f'Выиграл игрок {gamers[winner]}!')
        break
    if step == size_square ** 2:    # Если игровое поле полностью заполнено и цикл не прирвался, значит ничья
        print("Ничья!")