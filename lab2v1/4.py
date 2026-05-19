import time
import matplotlib.pyplot as plt
from functools import lru_cache

# Стандартный рекурсивный Фибоначчи 
@lru_cache(maxsize=None)
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Стандартный рекурсивный Люка с кэшем
@lru_cache(maxsize=None)
def lucas(n):
    if n == 0:
        return 2
    if n == 1:
        return 1
    return lucas(n - 1) + lucas(n - 2)

# Быстрый итеративный Фибоначчи (без рекурсии)
def fib_fast(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

# Быстрый итеративный Люка
def lucas_fast(n):
    if n == 0:
        return 2
    if n == 1:
        return 1
    
    a, b = 2, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def measure_time(func, n, repeats=3):
    total = 0
    for _ in range(repeats):
        start = time.perf_counter()
        func(n)
        end = time.perf_counter()
        total += (end - start)
    return total / repeats

if __name__ == "__main__":
    n_values = list(range(10, 41, 5))
    
    fib_times = []
    fib_fast_times = []
    
    print("Измерение времени:")
    print("n\t\tFibonacci (рекурсивный)\tFib_fast (итеративный)")
    print("-" * 60)
    
    for n in n_values:
        fib_time = measure_time(fibonacci, n)
        fib_fast_time = measure_time(fib_fast, n)
        fib_times.append(fib_time)
        fib_fast_times.append(fib_fast_time)
        print(f"{n}\t\t{fib_time:.8f}\t\t\t{fib_fast_time:.8f}")
    
    plt.figure(figsize=(10, 6))
    plt.plot(n_values, fib_times, 'o-', label='Рекурсивный Фибоначчи', color='red', linewidth=2, markersize=8)
    plt.plot(n_values, fib_fast_times, 's-', label='Итеративный Фибоначчи O(n)', color='blue', linewidth=2, markersize=8)
    plt.xlabel('n', fontsize=12)
    plt.ylabel('Время (сек)', fontsize=12)
    plt.title('Сравнение производительности алгоритмов Фибоначчи', fontsize=14)
    plt.legend(fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.show()
    
    # Дополнительно покажем числа для проверки
    print("\nПроверка значений:")
    print(f"fibonacci(10) = {fibonacci(10)}")
    print(f"fib_fast(10) = {fib_fast(10)}")
    print(f"lucas(10) = {lucas(10)}")
    print(f"lucas_fast(10) = {lucas_fast(10)}")