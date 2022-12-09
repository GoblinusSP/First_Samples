from random import randint as rd
from time import sleep


print('Приветствую в игре Угадай число !')


def is_valid_x(x):
    return x.isdigit() ,int(x)

def input_x():
    global x 
    print('Введите допустимый диапазон случайного числа: ')      
    x = input()
    if is_valid_x(x):
        global n 
        n = rd(1, int(x))
        return n
    



def is_valid(num):
    "проверка вводимых данных"
    return num.isdigit() and 1 <= int(num) <= int(x)

def input_num():
    while True:       
        num = input(f'Угадайте загаданное системой число от 1 до {x}: ')
        if is_valid(num):
            return int(num)
        else:
            print(f'Может введем число от 1 до {x} ???')
        
def game_run():
    count = 0
    while n:
        num = input_num()
        if n < num:
            sleep(1)
            count += 1
            print('Ваше число больше загаданного. Попробуйте еще разок:')
        elif n > num:
            sleep(1)
            count += 1
            print('Ваше число меньше загаданного. Попробуйте еще разок:')
        elif n == num:
            sleep(1)
            print('Поздравляю !!! Вы угадали число !!!')
            sleep(1)
            print(f'Число было отгадано с {count} попытки. Спасибо за игру !!!')
            break
        


while True:
    print('Сыграем ?(Для начала игры наберите на клавиатуре (д) или (н) если не хотите)')
    gg = input().lower()
    
    if gg == 'д':
        input_x()
        game_run()
    elif gg == 'н':
        sleep(0.5)
        print('Довсидос !!!')
        break
    else:
        print('Введите корректные данные !!! да(д) или нет(н) ???')    