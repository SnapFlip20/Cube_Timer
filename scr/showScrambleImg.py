#-*- coding:utf-8 -*-

dd = {'w':'white', 'y':'yellow', 'r':'red', 'o':'orange', 'g':'green', 'b':'blue'}

def return_color(sc_lst):
    w = [['w', 'w', 'w'],
        ['w', 'w', 'w'],
        ['w', 'w', 'w']]
    y = [['y', 'y', 'y'],
        ['y', 'y', 'y'],
        ['y', 'y', 'y']]
    r = [['r', 'r', 'r'],
        ['r', 'r', 'r'],
        ['r', 'r', 'r']]
    o = [['o', 'o', 'o'],
        ['o', 'o', 'o'],
        ['o', 'o', 'o']]
    g = [['g', 'g', 'g'],
        ['g', 'g', 'g'],
        ['g', 'g', 'g']]
    b = [['b', 'b', 'b'],
        ['b', 'b', 'b'],
        ['b', 'b', 'b']]

    # simulation start
    for j in sc_lst:
        if j == "U":
            w[0][0], w[0][2], w[2][0], w[2][2] = w[2][0], w[0][0], w[2][2], w[0][2]
            w[0][1], w[1][0], w[1][2], w[2][1] = w[1][0], w[2][1], w[0][1], w[1][2]
            r[0][0], r[0][1], r[0][2], g[0][0], g[0][1], g[0][2], o[0][0], o[0][1], o[0][2], b[0][0], b[0][1], b[0][2] = b[0][0], b[0][1], b[0][2], r[0][0], r[0][1], r[0][2], g[0][0], g[0][1], g[0][2], o[0][0], o[0][1], o[0][2]
        elif j == "U'":
            w[0][0], w[0][2], w[2][0], w[2][2] = w[0][2], w[2][2], w[0][0], w[2][0]
            w[0][1], w[1][0], w[1][2], w[2][1] = w[1][2], w[0][1], w[2][1], w[1][0]
            r[0][0], r[0][1], r[0][2], g[0][0], g[0][1], g[0][2], o[0][0], o[0][1], o[0][2], b[0][0], b[0][1], b[0][2] = g[0][0], g[0][1], g[0][2], o[0][0], o[0][1], o[0][2], b[0][0], b[0][1], b[0][2], r[0][0], r[0][1], r[0][2]
        elif j == "U2":
            w[0][0], w[0][2], w[2][0], w[2][2] = w[2][0], w[0][0], w[2][2], w[0][2]
            w[0][1], w[1][0], w[1][2], w[2][1] = w[1][0], w[2][1], w[0][1], w[1][2]
            r[0][0], r[0][1], r[0][2], g[0][0], g[0][1], g[0][2], o[0][0], o[0][1], o[0][2], b[0][0], b[0][1], b[0][2] = b[0][0], b[0][1], b[0][2], r[0][0], r[0][1], r[0][2], g[0][0], g[0][1], g[0][2], o[0][0], o[0][1], o[0][2]
            w[0][0], w[0][2], w[2][0], w[2][2] = w[2][0], w[0][0], w[2][2], w[0][2]
            w[0][1], w[1][0], w[1][2], w[2][1] = w[1][0], w[2][1], w[0][1], w[1][2]
            r[0][0], r[0][1], r[0][2], g[0][0], g[0][1], g[0][2], o[0][0], o[0][1], o[0][2], b[0][0], b[0][1], b[0][2] = b[0][0], b[0][1], b[0][2], r[0][0], r[0][1], r[0][2], g[0][0], g[0][1], g[0][2], o[0][0], o[0][1], o[0][2]
        elif j == "D":
            y[0][0], y[0][2], y[2][0], y[2][2] = y[2][0], y[0][0], y[2][2], y[0][2]
            y[0][1], y[1][0], y[1][2], y[2][1] = y[1][0], y[2][1], y[0][1], y[1][2]
            r[2][0], r[2][1], r[2][2], g[2][0], g[2][1], g[2][2], o[2][0], o[2][1], o[2][2], b[2][0], b[2][1], b[2][2] = g[2][0], g[2][1], g[2][2], o[2][0], o[2][1], o[2][2], b[2][0], b[2][1], b[2][2], r[2][0], r[2][1], r[2][2]
        elif j == "D'":
            y[0][0], y[0][2], y[2][0], y[2][2] = y[0][2], y[2][2], y[0][0], y[2][0]
            y[0][1], y[1][0], y[1][2], y[2][1] = y[1][2], y[0][1], y[2][1], y[1][0]
            r[2][0], r[2][1], r[2][2], g[2][0], g[2][1], g[2][2], o[2][0], o[2][1], o[2][2], b[2][0], b[2][1], b[2][2] = b[2][0], b[2][1], b[2][2], r[2][0], r[2][1], r[2][2], g[2][0], g[2][1], g[2][2], o[2][0], o[2][1], o[2][2]
        elif j == "D2":
            y[0][0], y[0][2], y[2][0], y[2][2] = y[2][0], y[0][0], y[2][2], y[0][2]
            y[0][1], y[1][0], y[1][2], y[2][1] = y[1][0], y[2][1], y[0][1], y[1][2]
            r[2][0], r[2][1], r[2][2], g[2][0], g[2][1], g[2][2], o[2][0], o[2][1], o[2][2], b[2][0], b[2][1], b[2][2] = g[2][0], g[2][1], g[2][2], o[2][0], o[2][1], o[2][2], b[2][0], b[2][1], b[2][2], r[2][0], r[2][1], r[2][2]
            y[0][0], y[0][2], y[2][0], y[2][2] = y[2][0], y[0][0], y[2][2], y[0][2]
            y[0][1], y[1][0], y[1][2], y[2][1] = y[1][0], y[2][1], y[0][1], y[1][2]
            r[2][0], r[2][1], r[2][2], g[2][0], g[2][1], g[2][2], o[2][0], o[2][1], o[2][2], b[2][0], b[2][1], b[2][2] = g[2][0], g[2][1], g[2][2], o[2][0], o[2][1], o[2][2], b[2][0], b[2][1], b[2][2], r[2][0], r[2][1], r[2][2]
        elif j == "R":
            r[0][0], r[0][2], r[2][0], r[2][2] = r[2][0], r[0][0], r[2][2], r[0][2]
            r[0][1], r[1][0], r[1][2], r[2][1] = r[1][0], r[2][1], r[0][1], r[1][2]
            w[2][0], w[2][1], w[2][2], g[0][2], g[1][2], g[2][2], y[0][0], y[0][1], y[0][2], b[0][0], b[1][0], b[2][0] = g[2][2], g[1][2], g[0][2], y[0][0], y[0][1], y[0][2], b[2][0], b[1][0], b[0][0], w[2][0], w[2][1], w[2][2]
        elif j == "R'":
            r[0][0], r[0][2], r[2][0], r[2][2] = r[0][2], r[2][2], r[0][0], r[2][0]
            r[0][1], r[1][0], r[1][2], r[2][1] = r[1][2], r[0][1], r[2][1], r[1][0]
            w[2][0], w[2][1], w[2][2], g[0][2], g[1][2], g[2][2], y[0][0], y[0][1], y[0][2], b[0][0], b[1][0], b[2][0] = b[0][0], b[1][0], b[2][0], w[2][2], w[2][1], w[2][0], g[0][2], g[1][2], g[2][2], y[0][2], y[0][1], y[0][0]
        elif j == "R2":
            r[0][0], r[0][2], r[2][0], r[2][2] = r[2][0], r[0][0], r[2][2], r[0][2]
            r[0][1], r[1][0], r[1][2], r[2][1] = r[1][0], r[2][1], r[0][1], r[1][2]
            w[2][0], w[2][1], w[2][2], g[0][2], g[1][2], g[2][2], y[0][0], y[0][1], y[0][2], b[0][0], b[1][0], b[2][0] = g[2][2], g[1][2], g[0][2], y[0][0], y[0][1], y[0][2], b[2][0], b[1][0], b[0][0], w[2][0], w[2][1], w[2][2]
            r[0][0], r[0][2], r[2][0], r[2][2] = r[2][0], r[0][0], r[2][2], r[0][2]
            r[0][1], r[1][0], r[1][2], r[2][1] = r[1][0], r[2][1], r[0][1], r[1][2]
            w[2][0], w[2][1], w[2][2], g[0][2], g[1][2], g[2][2], y[0][0], y[0][1], y[0][2], b[0][0], b[1][0], b[2][0] = g[2][2], g[1][2], g[0][2], y[0][0], y[0][1], y[0][2], b[2][0], b[1][0], b[0][0], w[2][0], w[2][1], w[2][2]
        elif j == "L":
            o[0][0], o[0][2], o[2][0], o[2][2] = o[2][0], o[0][0], o[2][2], o[0][2]
            o[0][1], o[1][0], o[1][2], o[2][1] = o[1][0], o[2][1], o[0][1], o[1][2]
            w[0][0], w[0][1], w[0][2], g[0][0], g[1][0], g[2][0], y[2][0], y[2][1], y[2][2], b[0][2], b[1][2], b[2][2] = b[0][2], b[1][2], b[2][2], w[0][2], w[0][1], w[0][0], g[0][0], g[1][0], g[2][0], y[2][2], y[2][1], y[2][0]
        elif j == "L'":
            o[0][0], o[0][2], o[2][0], o[2][2] = o[0][2], o[2][2], o[0][0], o[2][0]
            o[0][1], o[1][0], o[1][2], o[2][1] = o[1][2], o[0][1], o[2][1], o[1][0]
            w[0][0], w[0][1], w[0][2], g[0][0], g[1][0], g[2][0], y[2][0], y[2][1], y[2][2], b[0][2], b[1][2], b[2][2] = g[2][0], g[1][0], g[0][0], y[2][0], y[2][1], y[2][2], b[2][2], b[1][2], b[0][2], w[0][0], w[0][1], w[0][2]
        elif j == "L2":
            o[0][0], o[0][2], o[2][0], o[2][2] = o[2][0], o[0][0], o[2][2], o[0][2]
            o[0][1], o[1][0], o[1][2], o[2][1] = o[1][0], o[2][1], o[0][1], o[1][2]
            w[0][0], w[0][1], w[0][2], g[0][0], g[1][0], g[2][0], y[2][0], y[2][1], y[2][2], b[0][2], b[1][2], b[2][2] = b[0][2], b[1][2], b[2][2], w[0][2], w[0][1], w[0][0], g[0][0], g[1][0], g[2][0], y[2][2], y[2][1], y[2][0]
            o[0][0], o[0][2], o[2][0], o[2][2] = o[2][0], o[0][0], o[2][2], o[0][2]
            o[0][1], o[1][0], o[1][2], o[2][1] = o[1][0], o[2][1], o[0][1], o[1][2]
            w[0][0], w[0][1], w[0][2], g[0][0], g[1][0], g[2][0], y[2][0], y[2][1], y[2][2], b[0][2], b[1][2], b[2][2] = b[0][2], b[1][2], b[2][2], w[0][2], w[0][1], w[0][0], g[0][0], g[1][0], g[2][0], y[2][2], y[2][1], y[2][0]
        elif j == "F":
            g[0][0], g[0][2], g[2][0], g[2][2] = g[2][0], g[0][0], g[2][2], g[0][2]
            g[0][1], g[1][0], g[1][2], g[2][1] = g[1][0], g[2][1], g[0][1], g[1][2]
            w[0][0], w[1][0], w[2][0], r[0][0], r[1][0], r[2][0], y[0][0], y[1][0], y[2][0], o[0][2], o[1][2], o[2][2] = o[2][2], o[1][2], o[0][2], w[0][0], w[1][0], w[2][0], r[0][0], r[1][0], r[2][0], y[2][0], y[1][0], y[0][0]
        elif j == "F'":
            g[0][0], g[0][2], g[2][0], g[2][2] = g[0][2], g[2][2], g[0][0], g[2][0]
            g[0][1], g[1][0], g[1][2], g[2][1] = g[1][2], g[0][1], g[2][1], g[1][0]
            w[0][0], w[1][0], w[2][0], r[0][0], r[1][0], r[2][0], y[0][0], y[1][0], y[2][0], o[0][2], o[1][2], o[2][2] = r[0][0], r[1][0], r[2][0], y[0][0], y[1][0], y[2][0], o[2][2], o[1][2], o[0][2], w[2][0], w[1][0], w[0][0]
        elif j == "F2":
            g[0][0], g[0][2], g[2][0], g[2][2] = g[2][0], g[0][0], g[2][2], g[0][2]
            g[0][1], g[1][0], g[1][2], g[2][1] = g[1][0], g[2][1], g[0][1], g[1][2]
            w[0][0], w[1][0], w[2][0], r[0][0], r[1][0], r[2][0], y[0][0], y[1][0], y[2][0], o[0][2], o[1][2], o[2][2] = o[2][2], o[1][2], o[0][2], w[0][0], w[1][0], w[2][0], r[0][0], r[1][0], r[2][0], y[2][0], y[1][0], y[0][0]
            g[0][0], g[0][2], g[2][0], g[2][2] = g[2][0], g[0][0], g[2][2], g[0][2]
            g[0][1], g[1][0], g[1][2], g[2][1] = g[1][0], g[2][1], g[0][1], g[1][2]
            w[0][0], w[1][0], w[2][0], r[0][0], r[1][0], r[2][0], y[0][0], y[1][0], y[2][0], o[0][2], o[1][2], o[2][2] = o[2][2], o[1][2], o[0][2], w[0][0], w[1][0], w[2][0], r[0][0], r[1][0], r[2][0], y[2][0], y[1][0], y[0][0]
        elif j == "B":
            b[0][0], b[0][2], b[2][0], b[2][2] = b[2][0], b[0][0], b[2][2], b[0][2]
            b[0][1], b[1][0], b[1][2], b[2][1] = b[1][0], b[2][1], b[0][1], b[1][2]
            w[0][2], w[1][2], w[2][2], r[0][2], r[1][2], r[2][2], y[0][2], y[1][2], y[2][2], o[0][0], o[1][0], o[2][0] = r[0][2], r[1][2], r[2][2], y[0][2], y[1][2], y[2][2], o[2][0], o[1][0], o[0][0], w[2][2], w[1][2], w[0][2]
        elif j == "B'":
            b[0][0], b[0][2], b[2][0], b[2][2] = b[0][2], b[2][2], b[0][0], b[2][0]
            b[0][1], b[1][0], b[1][2], b[2][1] = b[1][2], b[0][1], b[2][1], b[1][0]
            w[0][2], w[1][2], w[2][2], r[0][2], r[1][2], r[2][2], y[0][2], y[1][2], y[2][2], o[0][0], o[1][0], o[2][0] = o[2][0], o[1][0], o[0][0], w[0][2], w[1][2], w[2][2], r[0][2], r[1][2], r[2][2], y[2][2], y[1][2], y[0][2]
        elif j == "B2":
            b[0][0], b[0][2], b[2][0], b[2][2] = b[2][0], b[0][0], b[2][2], b[0][2]
            b[0][1], b[1][0], b[1][2], b[2][1] = b[1][0], b[2][1], b[0][1], b[1][2]
            w[0][2], w[1][2], w[2][2], r[0][2], r[1][2], r[2][2], y[0][2], y[1][2], y[2][2], o[0][0], o[1][0], o[2][0] = r[0][2], r[1][2], r[2][2], y[0][2], y[1][2], y[2][2], o[2][0], o[1][0], o[0][0], w[2][2], w[1][2], w[0][2]
            b[0][0], b[0][2], b[2][0], b[2][2] = b[2][0], b[0][0], b[2][2], b[0][2]
            b[0][1], b[1][0], b[1][2], b[2][1] = b[1][0], b[2][1], b[0][1], b[1][2]
            w[0][2], w[1][2], w[2][2], r[0][2], r[1][2], r[2][2], y[0][2], y[1][2], y[2][2], o[0][0], o[1][0], o[2][0] = r[0][2], r[1][2], r[2][2], y[0][2], y[1][2], y[2][2], o[2][0], o[1][0], o[0][0], w[2][2], w[1][2], w[0][2]

    return dd[w[0][2]], dd[w[1][2]], dd[w[2][2]], dd[w[0][1]], dd[w[1][1]], dd[w[2][1]], dd[w[0][0]], dd[w[1][0]], dd[w[2][0]]


