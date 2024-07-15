import turtle

def koch_snowflake(length, depth):
    if depth == 0:
        turtle.forward(length)
    else:
        length /= 3
        koch_snowflake(length, depth-1)
        turtle.left(60)
        koch_snowflake(length, depth-1)
        turtle.right(120)
        koch_snowflake(length, depth-1)
        turtle.left(60)
        koch_snowflake(length, depth-1)

def draw_snowflake(length, depth):
    for _ in range(3):
        koch_snowflake(length, depth)
        turtle.right(120)

def main():
    depth = int(input("Enter the recursion depth: "))
    length = 300  # Довжина однієї сторони початкового трикутника

    turtle.speed(0)  # Максимальна швидкість малювання
    turtle.penup()
    turtle.goto(-length/2, length/3)  # Початкова позиція
    turtle.pendown()

    draw_snowflake(length, depth)

    turtle.hideturtle()
    turtle.done()

if __name__ == "__main__":
    main()
