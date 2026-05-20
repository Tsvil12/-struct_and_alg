import turtle
import time
import matplotlib.pyplot as plt

def koch_curve(t, length, depth):
    if depth == 0:
        t.forward(length)
    else:
        length /= 3
        koch_curve(t, length, depth - 1)
        t.left(60)
        koch_curve(t, length, depth - 1)
        t.right(120)
        koch_curve(t, length, depth - 1)
        t.left(60)
        koch_curve(t, length, depth - 1)

def draw_koch(depth):
    start = time.perf_counter()
    t = turtle.Turtle()
    t.speed(0)
    t.up()
    t.goto(-200, 0)
    t.down()
    t.ht()
    koch_curve(t, 400, depth)
    end = time.perf_counter()
    return end - start

depths = range(1, 7)
times = []
errors = []


for depth in depths:
    try:
        t = draw_koch(depth)
        times.append(t)
        print(f"Глубина {depth}: {t:.4f} сек")
    except Exception as e:
        times.append(None)
        errors.append(depth)
        print(f"Глубина {depth}: ОШИБКА - {e}")

plt.figure(figsize=(10, 5))
valid_depths = [d for d, t in zip(depths, times) if t is not None]
valid_times = [t for t in times if t is not None]
plt.plot(valid_depths, valid_times, 'o-', color='blue', linewidth=2)

for err in errors:
    plt.axvline(x=err, color='red', linestyle='--', alpha=0.7)
    plt.text(err, max(valid_times)*0.9, f'Ошибка на {err}', color='red', ha='center')

plt.xlabel("Глубина рекурсии", fontsize=12)
plt.ylabel("Время отрисовки (сек)", fontsize=12)
plt.title("Кривая Коха: зависимость времени от глубины", fontsize=14)
plt.grid(True, alpha=0.3)
plt.show()