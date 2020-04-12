import  random

def linear_search(list_a, target):
    match = False

    for element in list_a:
        if element == target:
            match = True
            break
    return match


if __name__ == '__main__':
    list_size = int(input('De que tamaño será la lista? '))
    target = int(input('¿Qué número quieres encontrar? '))
    list_a = [random.randint(0,100) for i in range(list_size)]
    found = linear_search(list_a, target)
    
    print(list_a)
    print(f'El elemento {target} {"Esta" if found else "no esta"} en la lista')