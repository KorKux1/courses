import time
import sys
def recursive_fibonacci(n):
    if n == 0 or n == 1:
        return 1
    
    return recursive_fibonacci(n-1) + recursive_fibonacci(n-2)

def dinamic_fibonacci(n, memory={}):
    if n == 0 or n == 1:
        return 1
    try:
        return memory[n]
    except KeyError:
        result = dinamic_fibonacci(n-1, memory) + dinamic_fibonacci(n-2 , memory)
        memory[n] = result
        return result
    
if __name__ == '__main__':
    sys.setrecursionlimit(10002)
    n = int(input('Escoge un número: '))
    start = time.time()
    result = recursive_fibonacci(n)
    end = time.time()
    print(f'[Algoritmo recursivo tradicional] Resultado: {result} tiempo: {end-start}')
    start = time.time()
    result = dinamic_fibonacci(n)
    end = time.time()
    print(f'[Algoritmo recursivo usando programación dinamica] Resultado: {result} tiempo: {end-start}')  
