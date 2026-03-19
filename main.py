from src.calculator import calculate

def main():
    print("=== Калькулятор с ОПН ===")
    print("Поддерживаемые операции: +, -, *, /, ^")
    print("Поддержка скобок: ( )")
    print("Для выхода введите: exit, quit или q\n")

    while True:
        try:
            # Запрос ввода у пользователя
            expression = input("Введите выражение: ").strip()

            # Проверка на выход
            if expression.lower() in ['exit', 'quit', 'q', 'выход']:
                print("👋 До свидания!")
                break

            # Если пусто — пропускаем
            if not expression:
                continue

            # Вычисление
            result = calculate(expression)
            print(f"✅ Результат: {result}\n")

        except ZeroDivisionError as e:
            print(f"❌ Ошибка: {e}\n")
        except Exception as e:
            print(f"❌ Ошибка ввода: {e}\n")

if __name__ == "__main__":
    main()