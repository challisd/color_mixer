# designed for use with matplotlib color tuples

def mix_colors(colors, degrees):
    a = r = g = b = 0
    for i in range(0,len(degrees)):
        a = a + colors[i][3]*degrees[i]
        r = r + colors[i][0]*degrees[i]
        g = g + colors[i][1]*degrees[i]
        b = b + colors[i][2]*degrees[i]
    d = sum(degrees)
    return((r/d,g/d,b/d,a/d))

def darken_color(color, how_much):
    r = max(color[0] - (color[0] * how_much), 0.0)
    g = max(color[1] - (color[1] * how_much), 0.0)
    b = max(color[2] - (color[2] * how_much), 0.0)
    return(r, g, b, color[3])
