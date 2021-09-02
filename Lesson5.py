#1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.

my_list = []
while True:
    line = input("Enter anything: ")
    if line == '':
        print(my_list)
        exit()
    else:
        newline = line + '\n'
        my_list.append(newline)

    with open("test_1.txt", "w") as file_obj:
        file_obj.writelines(my_list)



#2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк, количества слов в каждой строке.

my_list = ['Hello\n', 'Chao\n', 'Hola\n']
with open("test_2.txt", 'w+') as file_obj:
    file_obj.writelines(my_list)
with open("test_2.txt") as file_obj:
    lines = 0
    letters = 0
    for line in file_obj:
        lines += line.count("\n")
        letters = len(line)-1
        print(f"{letters} letters in line")
    print(f"String count is {lines}")


#3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк). 
#Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. 
#Выполнить подсчет средней величины дохода сотрудников.
    
'''
firm = {'Black': 170, 'Smith': 210, 'Potter': 190, 'Green': 150}
try:
    file_obj = open("test_3.txt", 'w')
    for last_name, salary in firm.items():
        file_obj.write(last_name + ':' + str(salary) + "\n")
except IOError:
    print("Произошла ошибка ввода-вывода!")
finally:
    file_obj.close()
summa = 0
count = 0
persons = []
with open("test_3.txt", "r") as file_obj:
    for line in file_obj:
        print(line, end="")
        tokens = line.split(':')
        if int(tokens[1]) <= 200:
            persons.append(tokens[0])
        summa += int(tokens[1])
        count += 1
result = summa / count
print(f"persons: {persons}")
print(f"averate: {result}")


#4. Создать (не программно) текстовый файл со следующим содержимым:
#One — 1
#Two — 2
#Three — 3
#Four — 4
#Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские числительные должны заменяться на русские. 
#Новый блок строк должен записываться в новый текстовый файл.

translater = {'One': 'odin', 'Two': 'dva', 'Three': 'tri', 'Four': 'chetyre'}
my_list = []
result = []
try:
    file_obj = open("test_4_output.txt", 'r')
    for line in file_obj:
        tokens = line.split(" - ")
        print(tokens)
        if tokens[0] in translater:
            word = translater[tokens[0]]
            result.append(word +' - '+ tokens[1])
    print(result)
except IOError:
    print("Произошла ошибка ввода-вывода!")
finally:
    file_obj.close()

try:
    file_input = open("test_4_input.txt", "w")
    file_input.writelines(result)
except IOError:
    print("Произошла ошибка ввода-вывода!")
finally:
    file_input.close() 



