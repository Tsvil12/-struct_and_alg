import turtle
import random
import time
import matplotlib.pyplot as plt

def mountain(t, length, depth, roughness):
    if depth == 0:
        t.forward(length)
    else:
        mid = length / 2
        offset = random.uniform(-roughness * length, roughness * length)
        pos = t.pos()
        heading = t.heading()
        t.forward(mid)
        t.left(90)
        t.forward(offset)
        t.right(90)
        mountain(t, mid, depth - 1, roughness / 1.5)
        t.penup()
        t.goto(pos)
        t.setheading(heading)
        t.forward(mid)
        t.right(90)
        t.forward(offset)
        t.left(90)
        t.pendown()
        mountain(t, mid, depth - 1, roughness / 1.5)

def draw_mountain(depth):
    start = time.perf_counter()
    t = turtle.Turtle()
    t.speed(0)
    t.up()
    t.goto(-300, -50)
    t.down()
    t.ht()
    mountain(t, 600, depth, 0.5)
    end = time.perf_counter()
    return end - start

depths = range(1, 7)
times = []
errors = []


for depth in depths:
    try:
        t = draw_mountain(depth)
        times.append(t)
        print(f"Глубина {depth}: {t:.4f} сек")
    except Exception as e:
        times.append(None)
        errors.append(depth)
        print(f"Глубина {depth}: ОШИБКА - {e}")

plt.figure(figsize=(10, 5))
valid_depths = [d for d, t in zip(depths, times) if t is not None]
valid_times = [t for t in times if t is not None]
plt.plot(valid_depths, valid_times, 'o-', color='brown', linewidth=2)

for err in errors:
    plt.axvline(x=err, color='red', linestyle='--', alpha=0.7)
    plt.text(err, max(valid_times)*0.9, f'Ошибка на {err}', color='red', ha='center')

plt.xlabel("Глубина рекурсии", fontsize=12)
plt.ylabel("Время отрисовки (сек)", fontsize=12)
plt.title("Фрактальные горы: рост времени при увеличении глубины", fontsize=14)
plt.grid(True, alpha=0.3)
plt.show()