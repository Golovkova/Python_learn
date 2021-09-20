#1.Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
#Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
def div(*args):

    try:
        arg1 = int(input("Введите Делитель "))
        arg2 = int(input("Введите Делитель "))
        res = arg1 / arg2
    except ValueError:
        return 'Ошибка значения'
    except ZeroDivisionError:
        return "На ноль делить нельзя!"

    return res

    if arg2 != 0:
        return arg1 / arg2
    else:
        print("Значение не может быть равно нулю")

print(f'result  {div()}')

#2.Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения,
#город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных
#о пользователе одной строкой.

name = input('enter name ')
surname = input('enter surname ')
year = int(input('enter year '))
city = input('enter city ')
email = input('enter email ')
telephone = input('input telephone ')

def my_func (name, surname, year, city, email, telephone):
     return ' '.join([name, surname, year, city, email, telephone])
print(my_func(surname = 'Семенцов', name = 'Антон', year = '1993', city = 'Санкт-Петербург', email = 'See21@mail.ru', telephone = '89999999999'))


#3.Реализовать функцию my_func(), которая принимает три позиционных
#аргумента, и возвращает сумму наибольших двух аргументов.
def my_func(arg1 , arg2, arg3):
    if arg1 >= arg3 and arg2 >= arg3:
        return arg1 + arg2
    elif arg1 > arg2 and arg1 < arg3:
        return arg1 + arg3
    else:
        return arg2 + arg3

print(f'Result - {my_func(int(input("enter first argument ")), int(input("enter second argument ")), int(input("enter third argument ")))}') 

#4.Программа принимает действительное положительное число x и целое отрицательное число y. Необходимо выполнить возведение
#числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y). При решении задания необходимо обойтись без встроенной
#функции возведения числа в степень.
def my_func(x, y):
    return 1 / x ** abs(y)
    #return x ** y
print(my_func(5, -8)) 

5.Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна выводиться сумма чисел.
Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter. Сумма вновь введенных чисел будет добавляться
к уже подсчитанной сумме. Но если вместо числа вводится специальный символ, выполнение программы завершается. Если специальный символ
введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.

def my_sum ():
    sum_res = 0
    ex = False
    while ex == False:
        number = input('Input numbers or Q for quit - ').split()

        res = 0
        for el in range(len(number)):
            if number[el] == 'q' or number[el] == 'Q':
                ex = True
                break
            else:
                res = res + int(number[el])
        sum_res = sum_res + res
        print(f'Current sum is {sum_res}')
    print(f'Your final sum is {sum_res}')
my_sum() 

