import math


def distance(p1, p2):
    """
    Расстояние между двумя точками
    """
    # TODO: напишите тело функции

    # return math.sqrt((p2["x"] - p1["x"]) * (p2["x"] - p1["x"]) + (p2["y"] - p1["y"]) * (p2["y"] - p1["y"]))
    return math.sqrt((p2["x"] - p1["x"]) ** 2 + (p2["y"] - p1["y"]) ** 2)


# Даны две точки на координатной плоскости
# point1 = {"x": 2, "y": 5}
# point2 = {"x": -2, "y": 4}
point1 = {"x": 3, "y": 0}
point2 = {"x": 0, "y": 4}

dist = distance(point1, point2)

print("Расстояние между точками = ", dist)
