def get_circle(xc, yc, r):
    points = []
    x = 0
    y = r
    d = 3 - 2 * r
    points += get_symetry_points(xc, yc, x, y)
    while x <= y:
        x += 1
        if d < 0:
            d += (4 * x) + 6
        else:
            d += 4 * (x - y) + 10
            y -= 1
        
        points += get_symetry_points(xc, yc, x, y)

    return points

def get_symetry_points(xc, yc, x, y):
    return [
        (xc+x, yc+y),
        (xc-x, yc+y),
        (xc+x, yc-y),
        (xc-x, yc-y),
        (xc+y, yc+x),
        (xc-y, yc+x),
        (xc+y, yc-x),
        (xc-y, yc-x),
    ]