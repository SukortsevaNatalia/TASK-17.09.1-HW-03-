import random


# Ввод последовательности чисел согласно условию
while True:
    entered_list = input("Введите числа через пробел: ")
    str_list = entered_list.replace(' ', '')

    if not str_list.isdigit():
        print("Ошибка при вводе последовательности\n"
              "Допускается ввод только чисел через пробел, строка не должна быть пустой")
    else:
        list_array = entered_list.split()
        break


# Ввод числа с клавиатуры
in_number: str = input("Введите число: ")
try:
    while in_number.isalpha() or int(in_number) < 0:
        in_number = input("Это не число, введите число: ")
except ValueError:
    in_number = input("Это не число, введите число: ")

number = int(in_number)


# Быстрая сортировка списка по возрастанию элементов
arr = [int(item) for item in list_array]

def qsort_random(arr, left, right):
    if len(arr) == 1:
        return arr
    p = random.choice(arr[left:right + 1])
    i, j = left, right
    while i <= j:
        while arr[i] < p:
            i += 1
        while arr[j] > p:
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1

    if j > left:
        qsort_random(arr, left, j)
    if right > i:
        qsort_random(arr, i, right)
    return qsort_random


qsort_random(arr, 0, len(arr) - 1)
print(f'Отсортированный по возрастанию список: {arr}')


# Устанавливается номер позиции элемента, который меньше введенного пользователем числа,
# а также следующий за ним больше или равен этому числу:
def binary_search(array, element, left, right):
    try:
        if left > right:  # если левая граница превысила правую,
            return False  # значит элемент отсутствует

        middle = (right + left) // 2  # находимо середину
        if array[middle] == element:  # если элемент в середине,
            return middle  # возвращаем этот индекс
        elif element < array[middle]:  # если элемент меньше элемента в середине
            # рекурсивно ищем в левой половине
            return binary_search(array, element, left, middle - 1)
        else:  # иначе в правой
            return binary_search(array, element, middle + 1, right)
    except IndexError:

        return -1


result = binary_search(arr, number, 0, len(arr))

if not binary_search(arr, number, 0, len(arr)):
    rI = min(arr, key=lambda x: (abs(x - number), x))
    ind = arr.index(rI)
    more_ind = ind + 1
    less_ind = ind - 1

    if rI < number:
        print(f'''В списке нет введенного элемента      
        Ближайший больший элемент: {arr[more_ind]} его индекс: {more_ind}
        Ближайший меньший элемент: {rI}, его индекс: {ind}''')
    elif arr.index(rI) == 0:
        if number == arr[0]:
            print(f'''Индекс введенного элемента: {ind}
            Ближайший больший элемент: {arr[more_ind]}, его индекс: {more_ind}
            Ближайший меньший элемент: отсутствует''')
        else:
            print(f'''В списке нет введенного элемента
            Ближайший больший элемент: {arr[0]}, его индекс: {ind}
            Ближайший меньший элемент: отсутствует''')
    elif less_ind < 0:
        print(less_ind)
        print(f'''В списке нет введенного элемента
        Ближайший больший элемент: {rI}, его индекс: {arr.index(rI)}
        В списке нет меньшего элемента''')
    elif rI > number:
        print(f'''В списке нет введенного элемента
        Ближайший больший элемент: {rI}, его индекс: {arr.index(rI)}
        Ближайший меньший элемент: {arr[less_ind]} его индекс: {less_ind}''')

else:
    if result == -1:
        print(f'''Число находится за правой границей списка, 
        Индекс введенного элемента: отсутствует
        Ближайший меньший элемент: {arr[-1]}, его индекс: {arr.index(arr[-1])} ''')
    else:
        print(f'''Индекс введенного элемента: {binary_search(arr, number, 0, len(arr))}
        Ближайший больший элемент: отсутствует
        Ближайший меньший элемент {arr[result - 1]}, его индекс {result - 1} ''')