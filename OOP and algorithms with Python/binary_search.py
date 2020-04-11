import random

def binary_search(list_a, start, end, target):
    print(f'buscando {target} entre {list_a[start]} y {list_a[end - 1]}')
    if start > end:
        return False

    middle = (start + end) // 2

    if list_a[middle] == target:
        return True
    elif list_a[middle] < target:
        return binary_search(list_a, middle + 1, end, target)
    else:
        return binary_search(list_a, start, middle - 1, target)


if __name__ == '__main__':
    list_size = int(input('De que tamano es la list? '))
    target = int(input('Que numero quieres encontrar? '))

    list_a = sorted([random.randint(0, 100) for i in range(list_size)])

    found = binary_search(list_a, 0, len(list_a), target)

    print(list_a)
    print(f'El elemento {target} {"esta" if found else "no esta"} en la lista')