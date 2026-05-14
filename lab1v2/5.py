import time
import matplotlib.pyplot as plt

def test_in_list(n):
    """Проверка оператора in для списка"""
    lst = list(range(n))
    start = time.perf_counter()
    for _ in range(10000):
        _ = (n - 1) in lst  # Худший случай - поиск последнего элемента
    end = time.perf_counter()
    return end - start

def test_in_set(n):
    """Проверка оператора in для множества"""
    s = set(range(n))
    start = time.perf_counter()
    for _ in range(10000):
        _ = (n - 1) in s
    end = time.perf_counter()
    return end - start

print("=== Задание 5 ===")
print("Сравнение производительности оператора in для множеств и списков")
print()

sizes = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
list_times = []
set_times = []

print("Результаты измерений (10000 операций in для каждого размера):")
print("N\t\tСписок (сек)\tМножество (сек)\tРазница (раз)")
print("-" * 70)

for size in sizes:
    list_time = test_in_list(size)
    set_time = test_in_set(size)
    list_times.append(list_time)
    set_times.append(set_time)
    speedup = list_time / set_time if set_time > 0 else 0
    print(f"{size}\t\t{list_time:.6f}\t\t{set_time:.6f}\t\t{speedup:.1f}x")

# Построение графика
plt.figure(figsize=(12, 7))

# Основной график
plt.plot(sizes, list_times, marker='o', linewidth=2, markersize=8,
         color='red', label='in для списка (O(N))')
plt.plot(sizes, set_times, marker='s', linewidth=2, markersize=8,
         color='blue', label='in для множества (O(1))')

plt.xlabel('Количество элементов', fontsize=12)
plt.ylabel('Время выполнения (сек) для 10000 операций', fontsize=12)
plt.title('Сравнение производительности оператора in\nМножество vs Список', fontsize=14)
plt.legend(fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)

# Добавим текст с пояснениями
plt.text(0.02, 0.98, 'Сложность:\n• Список: O(N)\n• Множество: O(1)', 
         transform=plt.gca().transAxes, fontsize=10, verticalalignment='top',
         bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

plt.tight_layout()
plt.show()

print()
print("Выводы:")
print("1. Оператор in для списка имеет сложность O(N) - линейный поиск")
print("2. Оператор in для множества имеет сложность O(1) - хэш-таблица")
print("3. При размере 10000 элементов множество быстрее списка примерно в 100-1000 раз")
print("4. Для операций поиска всегда предпочтительнее использовать множества")