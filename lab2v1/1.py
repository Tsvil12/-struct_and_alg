import time
import random
import matplotlib.pyplot as plt

# Сортировка выбором
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Быстрая сортировка
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def measure_time(sort_func, data):
    start = time.perf_counter()
    sort_func(data.copy())
    end = time.perf_counter()
    return end - start

def run_experiment():
    sizes = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
    
    # Случайные списки
    selection_random = []
    quick_random = []
    
    # Отсортированные списки
    selection_sorted = []
    quick_sorted = []
    
    # Обратные списки
    selection_reversed = []
    quick_reversed = []
    
    for size in sizes:
        data_random = [random.randint(0, 10000) for _ in range(size)]
        data_sorted = sorted(data_random)
        data_reversed = list(reversed(data_sorted))
        
        selection_random.append(measure_time(selection_sort, data_random))
        quick_random.append(measure_time(quick_sort, data_random))
        
        selection_sorted.append(measure_time(selection_sort, data_sorted))
        quick_sorted.append(measure_time(quick_sort, data_sorted))
        
        selection_reversed.append(measure_time(selection_sort, data_reversed))
        quick_reversed.append(measure_time(quick_sort, data_reversed))
        
        print(f"N={size}: selection={selection_random[-1]:.4f}s, quick={quick_random[-1]:.4f}s")
    
    # График 1: случайные числа
    plt.figure(figsize=(15, 5))
    
    plt.subplot(1, 3, 1)
    plt.plot(sizes, selection_random, 'o-', label='Сортировка выбором O(N²)', color='red')
    plt.plot(sizes, quick_random, 's-', label='Быстрая сортировка O(N log N)', color='blue')
    plt.xlabel('Размер массива N')
    plt.ylabel('Время (сек)')
    plt.title('Случайные числа')
    plt.legend()
    plt.grid(True)
    
    # График 2: отсортированные
    plt.subplot(1, 3, 2)
    plt.plot(sizes, selection_sorted, 'o-', label='Сортировка выбором', color='red')
    plt.plot(sizes, quick_sorted, 's-', label='Быстрая сортировка', color='blue')
    plt.xlabel('Размер массива N')
    plt.ylabel('Время (сек)')
    plt.title('Отсортированный список')
    plt.legend()
    plt.grid(True)
    
    # График 3: обратные
    plt.subplot(1, 3, 3)
    plt.plot(sizes, selection_reversed, 'o-', label='Сортировка выбором', color='red')
    plt.plot(sizes, quick_reversed, 's-', label='Быстрая сортировка', color='blue')
    plt.xlabel('Размер массива N')
    plt.ylabel('Время (сек)')
    plt.title('Обратный список')
    plt.legend()
    plt.grid(True)
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    run_experiment()