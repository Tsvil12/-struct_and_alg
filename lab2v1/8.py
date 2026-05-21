def print_sudoku(matrix):
    """Выводит судоку в красивом виде"""
    for i in range(4):
        for j in range(4):
            print(matrix[i][j], end=" ")
        print()

def find_empty(matrix):
    """Находит первую пустую клетку (0)"""
    for i in range(4):
        for j in range(4):
            if matrix[i][j] == 0:
                return i, j
    return None

def is_valid(matrix, num, pos):
    row, col = pos
    
    # Проверка строки
    for j in range(4):
        if matrix[row][j] == num and j != col:
            return False
    
    # Проверка столбца
    for i in range(4):
        if matrix[i][col] == num and i != row:
            return False
    
    # Проверка квадрата 2x2
    box_row = row // 2 * 2
    box_col = col // 2 * 2
    for i in range(box_row, box_row + 2):
        for j in range(box_col, box_col + 2):
            if matrix[i][j] == num and (i, j) != pos:
                return False
    
    return True

def solve_sudoku(matrix):
    """
    Решает судоку рекурсивно (backtracking)
    Базовый случай: нет пустых клеток - решение найдено
    Рекурсивный случай: ставим число и вызываем себя
    """
    find = find_empty(matrix)
    if not find:
        return True  # Базовый случай: все клетки заполнены
    
    row, col = find
    
    for num in range(1, 5):
        if is_valid(matrix, num, (row, col)):
            matrix[row][col] = num
            
            if solve_sudoku(matrix):  # Рекурсивный случай
                return True
            
            matrix[row][col] = 0  # Откат (backtracking)
    
    return False



sudoku = [
    [0, 0, 0, 0],
    [0, 0, 2, 0],
    [0, 1, 0, 0],
    [3, 0, 0, 4]
]

print("Исходное судоку:")
print_sudoku(sudoku)
print()

if solve_sudoku(sudoku):
    print("Решённое судоку:")
    print_sudoku(sudoku)
else:
    print("Решения не существует")

# Проверка правильности
print("\nПроверка:")
for i in range(4):
    print(f"Строка {i+1}: {sorted(sudoku[i])} == [1,2,3,4]")

for j in range(4):
    col = [sudoku[i][j] for i in range(4)]
    print(f"Столбец {j+1}: {sorted(col)} == [1,2,3,4]")