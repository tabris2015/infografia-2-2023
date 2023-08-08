def get_circle(xc, yc, r):
    points = []
    x = 0
    y = r
    Pk = 3 - 2 * r
    points.append((x, y))
    while x <= y:
        x += 1
        if Pk < 0:
            Pk += (4 * x) + 6
        else:
            Pk += 4 * (x - y) + 10
            y -= 1
        points.append((x, y))
    return points