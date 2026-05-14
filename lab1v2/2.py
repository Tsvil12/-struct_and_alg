import time
import matplotlib.pyplot as plt
import random

def all_unique_quadratic(arr):
    """O(N²) - попарное сравнение всех элементов"""
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] == arr[j]:
                return False
    return True

def all_unique_linear(arr):
    """O(N) - через множество"""
    return len(arr) == len(set(arr))

# Проверка работы
print("=== Задание 2 ===")
test1 = [1, 2, 3, 4, 5]
test2 = [1, 2, 3, 2, 5]
print(f"Квадратичный: {test1} -> {all_unique_quadratic(test1)}")
print(f"Квадратичный: {test2} -> {all_unique_quadratic(test2)}")
print(f"Линейный: {test1} -> {all_unique_linear(test1)}")
print(f"Линейный: {test2} -> {all_unique_linear(test2)}")
print()

def measure_time(func, sizes, repeats=3):
    """Измеряет среднее время выполнения функции"""
    times = []
    for size in sizes:
        total = 0
        for _ in range(repeats):
            data = list(range(size))  # Все уникальны
            start = time.perf_counter()
            func(data)
            end = time.perf_counter()
            total += (end - start)
        times.append(total / repeats)
    return times

# Измерение для линейного алгоритма (большие размеры)
print("Измерение линейного алгоритма O(N)...")
sizes_linear = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
times_linear = measure_time(all_unique_linear, sizes_linear)

# Измерение для квадратичного алгоритма (меньшие размеры, т.к. он медленный)
print("Измерение квадратичного алгоритма O(N²)...")
sizes_quadratic = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
times_quadratic = measure_time(all_unique_quadratic, sizes_quadratic)

# Построение графиков
plt.figure(figsize=(14, 5))

plt.subplot(1, 2, 1)
plt.plot(sizes_linear, times_linear, marker='o', color='blue', linewidth=2, markersize=6)
plt.xlabel('Размер списка N', fontsize=12)
plt.ylabel('Время (сек)', fontsize=12)
plt.title('Алгоритм O(N) - через множество', fontsize=14)
plt.grid(True, linestyle='--', alpha=0.7)

plt.subplot(1, 2, 2)
plt.plot(sizes_quadratic, times_quadratic, marker='s', color='red', linewidth=2, markersize=6)
plt.xlabel('Размер списка N', fontsize=12)
plt.ylabel('Время (сек)', fontsize=12)
plt.title('Алгоритм O(N²) - попарное сравнение', fontsize=14)
plt.grid(True, linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()

print("\nВывод: Линейный алгоритм (через множество) значительно быстрее при больших размерах данных")