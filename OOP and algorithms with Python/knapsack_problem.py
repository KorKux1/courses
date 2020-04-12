

def knapsack(size, weights, values, n):
    if n == 0 or size == 0:
        return 0
    
    if weights[n-1] > size:
        return knapsack(size, weights, values, n-1)

    return max(values[n -1] + knapsack(size - weights[n -1] , weights, values, n -1 ), knapsack(size, weights, values, n-1))
    # Complejidad: O(2^n)
    
if __name__ == "__main__":
    values = [500, 200, 120]
    weights = [10, 20, 30]
    knapsack_size = 25
    n = len(values)

    result = knapsack(knapsack_size, weights, values, n)
    print(result)