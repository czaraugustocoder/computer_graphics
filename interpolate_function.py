def interpolate(i0, d0, i1, d1):
    values = []
    a = (d1 - d0) / (i1 - i0)
    d = d0

    for i in range(i0, i1+1):
        values.append(d)
        d = d + a

    print(values)
    return values

ys = interpolate(80, 140, 200, 260)

for x in range(80, 201):
    print(ys[x - 80])