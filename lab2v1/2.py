def tribonacci(n):
    """
    Рекурсивная функция для вычисления n-го числа Трибоначчи
    Ряд: 0, 0, 1, 1, 2, 4, 7, 13, 24, ...
    """
    # Базовые случаи
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    
    # Рекурсивный случай
    return tribonacci(n - 1) + tribonacci(n - 2) + tribonacci(n - 3)

if __name__ == "__main__":
    print("Числа Трибоначчи:")
    for i in range(15):
        print(f"tribonacci({i}) = {tribonacci(i)}")