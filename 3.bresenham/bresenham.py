
def get_line(x0, y0, x1, y1):
    points = [(x0, y0)]
    d_x = x1 - x0
    d_y = y1 - y0 
    x_k = x0
    y_k = y0

    p_k = 2 * d_y - d_x
    
    while x_k < x1:
        x_k += 1
        if p_k < 0:
            p_k += 2 * d_y
        else:
            y_k += 1
            p_k += 2 * d_y - 2 * d_x 
        points.append((x_k, y_k))
    return points

if __name__ == "__main__":
    print(get_line(2, 2, 10, 5))