def hanoi(n, source, target, auxiliary, state):
    """Рекурсивне вирішення задачі Ханойських башт."""
    if n == 1:
        # Переміщуємо найменший диск
        disk = state[source].pop()
        state[target].append(disk)
        print(f"Перемістити диск з {source} на {target}: {disk}")
        print(f"Проміжний стан: {state}")
        return

    # Переміщуємо n-1 дисків з source на auxiliary
    hanoi(n - 1, source, auxiliary, target, state)

    # Переміщуємо найбільший диск з source на target
    disk = state[source].pop()
    state[target].append(disk)
    print(f"Перемістити диск з {source} на {target}: {disk}")
    print(f"Проміжний стан: {state}")

    # Переміщуємо n-1 дисків з auxiliary на target
    hanoi(n - 1, auxiliary, target, source, state)


def main():
    n = int(input("Введіть кількість дисків: "))
    # Ініціалізуємо стан стрижнів
    state = {
        'A': list(range(n, 0, -1)),  # Початковий стрижень з дисками
        'B': [],  # Допоміжний стрижень
        'C': []   # Цільовий стрижень
    }

    print(f"Початковий стан: {state}")
    hanoi(n, 'A', 'C', 'B', state)
    print(f"Кінцевий стан: {state}")


if __name__ == "__main__":
    main()