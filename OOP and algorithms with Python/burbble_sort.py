import random


def burbble_sort(list_a):
    n = len(list_a)

    for i in range(n):
        for j in range(0, n - i - 1): # O(n) * O(n) = O(n * n) = O(n**2)

            if list_a[j] > list_a[j + 1]:
                list_a[j], list_a[j + 1] = list_a[j + 1], list_a[j]

    return list_a

if __name__ == '__main__':
    list_size = int(input('De que tamano sera la lista? '))

    list_a = [random.randint(0, 100) for i in range(list_size)]
    print(list_a)

    list_a_sorted = burbble_sort(list_a)
    print(list_a_sorted)