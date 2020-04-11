import random

def merge_sort(list_a):
    if len(list_a) > 1:
        middle = len(list_a) // 2
        left = list_a[:middle]
        right = list_a[middle:]
        print(left, '*' * 5, right)

        # llamada recursiva en cada mitad. Para dividir las listas en más pequeñas. Esto se ejecuta
        # Hasta tener listas de un solo tamaño
        merge_sort(left)
        merge_sort(right)

        # Iteradores para recorrer las dos sublistas
        i = 0
        j = 0
        # Iterador para la lista principal
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                list_a[k] = left[i]
                i += 1
            else:
                list_a[k] = right[j]
                j += 1

            k += 1

        while i < len(left):
            list_a[k] = left[i]
            i += 1
            k +=1

        while j < len(right):
            list_a[k] = right[j]
            j += 1
            k += 1
        
        print(f'Izquierda {left}, Derecha {right}')
        print(list_a)
        print('-' * 50)

    return list_a


if __name__ == '__main__':
    list_size = int(input('De que tamano sera la lista? '))

    list_a = [random.randint(0, 100) for i in range(list_size)]
    print(list_a)
    print('-' * 20)

    list_a_ordenada = merge_sort(list_a)
    print(list_a_ordenada)