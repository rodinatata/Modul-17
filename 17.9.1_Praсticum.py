def sort(array):  # сортировка пузырьком
    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array

def search_binary(list, p, left, right):  # бинарный поиск элемента p
    if left > right:
        return f'"Элемент отсутствует"'

    middle = (left + right) // 2

    # если list[middle] == p
        # возможно, это элемент n+1 а n - это нужный индекс
        # если middle > 0 и list[middle-1] < p
            # то успех (n = middle-1)
        # если нет - то искать дальше
    if list[middle] == p:
        if middle > 0 and list[middle - 1] < p:
            return f'Номер позиции искомого элемента: {middle - 1}'
        return f'"Числа в последовательности не соответствуют заданному условию"'

    # если list[middle] > p
        # возможно, это элемент n+1 а n - это нужный индекс
        # если middle > 0 и list[middle-1] < p
            # то успех  (n = middle-1)
        # если нет - то искать дальше
    if list[middle] > p:
        if middle > 0 and list[middle - 1] < p:
            return f'Номер позиции искомого элемента: {middle - 1}'
        return search_binary(list, p, left, middle - 1)

    # если list[middle] < p
        # возможно, это элемент n, а n+1 тогда должен быть больше
        # если middle < right и list[middle+1] > p
            # то успех (n = middle)
        # если нет - то искать дальше
    if middle < right and list[middle+1] >= p:
        return f'Номер позиции искомого элемента: {middle}'
    return search_binary(list, p, middle + 1, right)


sequence = input("Введите последовательность целых чисел через пробел:")  # получаем последовательность чисел
my_list = list(map(int, sequence.split()))  # превращаем последовательность в список
any_number = int(input("Введите любое целое число:"))  # получаем число для сравнения
sort_list = sort(my_list) # получаем отсортированный список
print(sort_list)
print(search_binary(sort_list, any_number, 0, len(sort_list) - 1))
