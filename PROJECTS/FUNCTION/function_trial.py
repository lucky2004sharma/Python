import math

shapes = {
    "circle": lambda r: math.pi * r ** 2,
    "square": lambda s: s ** 2,
    "triangle": lambda b, h: 0.5 * b * h
}

shape = input("Shape (circle/square/triangle): ").lower()
if shape == "triangle":
    b, h = float(input("Base: ")), float(input("Height: "))
    print("Area:", shapes[shape](b, h))
else:
    val = float(input("Side/Radius: "))
    print("Area:", shapes[shape](val))