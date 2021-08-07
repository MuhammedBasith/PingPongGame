import turtle as t
import random
import colorgram


def extract_color_list():
    """
    Extract the colors from an image, colors where the sum of red+green+blue are greater than 600 are likely to be
    the background color
    """
    rgb_colors = []
    rgb_background = {"r": 255, "g": 255, "b": 255}

    colors = colorgram.extract('image.jpg', 100)
    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        if r + g + b < 600:
            rgb_colors.append((r, g, b))
        else:
            # print(f"skipped color {r},{g},{b} with sum {r+g+b}")
            rgb_background["r"] = min(r, rgb_background["r"])
            rgb_background["g"] = min(g, rgb_background["g"])
            rgb_background["b"] = min(b, rgb_background["b"])
    # print(f"background color is {rgb_background}")

    return rgb_colors, (rgb_background["r"], rgb_background["g"], rgb_background["b"])


color_list, background = extract_color_list()

tim = t.Turtle()
tim.width(15)
tim.hideturtle()
tim.speed("fastest")
t.colormode(255)

tim.up()
screen = t.Screen()
screen.bgcolor(background)
xcoord, ycoord = screen.screensize()

for y in range(10):
    for x in range(10):
        tim.setposition(-xcoord + 70 * x, -ycoord + 70 * y)
        tim.dot(30, random.choice(color_list))

screen.exitonclick()
