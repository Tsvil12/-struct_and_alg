def recursive_poly(word):
   
    # Базовый случай
    if len(word) <= 1:
        return "YES"
    
    # Если первый и последний символы разные
    if word[0] != word[-1]:
        return "NO"
    
    # Рекурсивный случай: убираем первый и последний символ
    return recursive_poly(word[1:-1])

if __name__ == "__main__":
    print("=== Проверка слова на палиндром ===")
    print("Введите слово:")
    
    user_word = input("Слово: ").strip().lower()
    
    result = recursive_poly(user_word)
    
    print(f"\nСлово: {user_word}")
    print(f"Результат: {result}")
    
    if result == "YES":
        print("Это палиндром!")
    else:
        print("Это не палиндром.")