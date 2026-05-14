import time
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')  # Для корректного отображения графиков

def foo(i):
    """Преобразует число в строку без использования str()"""
    digits = "0123456789"
    if i == 0:
        return "0"
    result = ""
    while i > 0:
        result = digits[i % 10] + result
        i = i // 10
    return result

print("=== Задание 1 ===")
print(f"foo(123) = {foo(123)}")
print(f"foo(0) = {foo(0)}")
print(f"foo(4567) = {foo(4567)}")
print()

# Измерение времени выполнения
sizes = [10, 100, 1000, 10000, 100000, 1000000, 10000000]
times = []

print("Измерение времени...")
for size in sizes:
    start = time.perf_counter()
    for _ in range(1000):
        foo(size)
    end = time.perf_counter()
    avg_time = (end - start) / 1000
    times.append(avg_time)
    print(f"N={size:8d}: {avg_time:.8f} сек")

# Построение графика
plt.figure(figsize=(10, 6))
plt.plot(sizes, times, marker='o', linewidth=2, markersize=8, color='blue')
plt.xlabel('Входное число N', fontsize=12)
plt.ylabel('Среднее время выполнения (сек)', fontsize=12)
plt.title('Зависимость времени выполнения функции foo(N) от N\nСложность O(log N)', fontsize=14)
plt.xscale('log')
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

print("\nВывод: Сложность алгоритма O(log N), т.к. количество итераций цикла равно количеству цифр в числе")