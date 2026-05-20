import turtle
import random
import time
import matplotlib.pyplot as plt

def tree(branchLen, t, thickness):
    if branchLen > 5:
        t.pensize(thickness)
        if branchLen < 15:
            t.color("green")
        else:
            t.color("brown")
        t.forward(branchLen)
        angle = random.randint(15, 45)
        t.right(angle)
        new_len = branchLen - random.randint(10, 20)
        tree(new_len, t, thickness - 1)
        t.left(angle * 2)
        tree(new_len, t, thickness - 1)
        t.right(angle)
        t.backward(branchLen)

def draw_tree(depth):
    start = time.perf_counter()
    t = turtle.Turtle()
    t.speed(0)
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.ht()
    tree(40 + depth * 5, t, 8)
    end = time.perf_counter()
    return end - start

depths = list(range(1, 10))
times = []
errors = []


for depth in depths:
    try:
        t = draw_tree(depth)
        times.append(t)
        print(f"Глубина {depth}: {t:.4f} сек")
    except Exception as e:
        times.append(None)
        errors.append(depth)
        print(f"Глубина {depth}: ОШИБКА - {e}")

# График
plt.figure(figsize=(10, 5))
valid_depths = [d for d, t in zip(depths, times) if t is not None]
valid_times = [t for t in times if t is not None]
plt.plot(valid_depths, valid_times, 'o-', color='green', linewidth=2)

for err in errors:
    plt.axvline(x=err, color='red', linestyle='--', alpha=0.7)
    plt.text(err, max(valid_times)*0.9, f'Ошибка на {err}', color='red', ha='center')

plt.xlabel("Глубина рекурсии", fontsize=12)
plt.ylabel("Время отрисовки (сек)", fontsize=12)
plt.title("Зависимость времени рисования фрактального дерева от глубины", fontsize=14)
plt.grid(True, alpha=0.3)
plt.savefig("C:/Users/pavel/Desktop/struct_and_alg/lab2v1/tree_time.png", dpi=150)
plt.show()