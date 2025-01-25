import turtle

def draw_koch_snowflake(t, length, level):
    # Рекурсивна функція для малювання одного сегмента фракталу Коха.
    if level == 0:
        t.forward(length)
    else:
        length /= 3.0
        draw_koch_snowflake(t, length, level - 1)
        t.left(60)
        draw_koch_snowflake(t, length, level - 1)
        t.right(120)
        draw_koch_snowflake(t, length, level - 1)
        t.left(60)
        draw_koch_snowflake(t, length, level - 1)

def main():
    # Запитуємо у користувача рівень рекурсії
    level = int(input("Введіть рівень рекурсії (0 або більше): ").strip())

    # Ініціалізація Turtle
    screen = turtle.Screen()
    screen.setup(width=800, height=800)
    screen.title("Сніжинка Коха")

    t = turtle.Turtle()
    t.speed(0)  # Максимальна швидкість
    t.penup()
    t.goto(-200, 100)  # Початкова позиція
    t.pendown()

    # Малювання трьох сторін сніжинки
    for _ in range(3):
        draw_koch_snowflake(t, 400, level)
        t.right(120)

    # Завершення
    t.hideturtle()
    screen.mainloop()

if __name__ == "__main__":
    main()