import colorgram as cg
from turtle import Turtle, Screen
from random import choice


def preprocess(img, n_colors = 26):
    colors = cg.extract(img, n_colors)
    new_colors = [color.rgb for color in colors if sum(list(color.rgb)) <= 600]
    print(len(new_colors))
    return new_colors


def main():
    palette = preprocess('hirst.jpg')
    tim = Turtle()
    tim.penup()
    tim.speed('fastest')
    tim.goto(-300, -300)
    canvas = Screen()
    canvas.colormode(255)
    n_spots = 10
    radius = 20

    for i in range(n_spots):
        tim.setposition(-300, 4*radius * i - 300)
        for j in range(n_spots):
            color = choice(palette)
            tim.color(color)
            tim.begin_fill()
            tim.circle(radius)
            tim.end_fill()
            tim.forward(4*radius)
    tim.hideturtle()
    canvas.exitonclick()


if __name__ == '__main__':
    main()
