import pygame
  
pygame.init() 

w , h = 600, 600
  
# CREATING CANVAS 
canvas = pygame.display.set_mode((w, h))

Cw , Ch = w // 2, h // 2

#putpixel function
def putpixel(X, Y, Color):
    pygame.draw.circle(canvas, Color, [Cw + X, Ch - Y], 1)

def drawline(x0, y0, x1, y1, cor):
    Dy = y1 - y0
    Dx = x1 - x0
    print(f"Delta x: {Dx} | Delta y: {Dy}")

    if abs(Dx) > abs(Dy):

        # garantindo que X0 é menor que X1
        tx0, tx1 = 0, 0

        if x0 > x1:
            tx0 = x0
            tx1 = x1
            x1 = tx0
            x0 = tx1

        print(f"X0 {x0}, X1 {x1}")

        a = Dy / Dx
        y = y0
        for x in range(int(x0), int(x1)+1):
            putpixel(x, y, (cor))
            y = y + a

    else:

        # garantindo que Y0 é menor que Y1
        ty0, ty1 = 0, 0

        if y0 > y1:
            ty0 = y0
            ty1 = y1
            y1 = ty0
            y0 = ty1

        print(f"y0 {y0}, y1 {y1}")

        a = Dx / Dy
        x = x0
        for y in range(int(y0), int(y1)+1):
            putpixel(x, y, (cor))
            x = x + a


# perspective projection
Vw = 2
Vh = 2
d = 2

def viewport_to_canvas(x, y):
    return (x * (Cw/Vw), y * (Ch/Vh))

def project_vertex(v):
    return viewport_to_canvas(v[0] * (d/v[2]), v[1] * (d/v[2]))

# The four "front" vertices
vAf = [-4, -1, 5]
vBf = [-4,  1, 5]
vCf = [-2,  1, 5]
vDf = [-2, -1, 5]

# The four "back" vertices
vAb = [-4, -1, 6]
vBb = [-4,  1, 6]
vCb = [-2,  1, 6]
vDb = [-2, -1, 6]

exit = False
  
while not exit:

    canvas.fill((255, 255, 255))

    print(project_vertex(vAf)[0], project_vertex(vAf)[1],project_vertex(vBf)[0], project_vertex(vBf)[1])

    # The front face

    drawline(project_vertex(vAf)[0], project_vertex(vAf)[1],project_vertex(vBf)[0], project_vertex(vBf)[1], (0, 0, 0))
    drawline(project_vertex(vBf)[0], project_vertex(vBf)[1],project_vertex(vCf)[0], project_vertex(vCf)[1], (0, 0, 0))
    drawline(project_vertex(vCf)[0], project_vertex(vCf)[1],project_vertex(vDf)[0], project_vertex(vDf)[1], (0, 0, 0))
    drawline(project_vertex(vDf)[0], project_vertex(vDf)[1],project_vertex(vAf)[0], project_vertex(vAf)[1], (0, 0, 0))

    # The back face

    drawline(project_vertex(vAb)[0], project_vertex(vAb)[1],project_vertex(vBb)[0], project_vertex(vBb)[1], (0, 0, 0))
    drawline(project_vertex(vBb)[0], project_vertex(vBb)[1],project_vertex(vCb)[0], project_vertex(vCb)[1], (0, 0, 0))
    drawline(project_vertex(vCb)[0], project_vertex(vCb)[1],project_vertex(vDb)[0], project_vertex(vDb)[1], (0, 0, 0))
    drawline(project_vertex(vDb)[0], project_vertex(vDb)[1],project_vertex(vAb)[0], project_vertex(vAb)[1], (0, 0, 0))

    # The front face

    drawline(project_vertex(vAf)[0], project_vertex(vAf)[1],project_vertex(vAb)[0], project_vertex(vAb)[1], (0, 0, 0))
    drawline(project_vertex(vBf)[0], project_vertex(vBf)[1],project_vertex(vBb)[0], project_vertex(vBb)[1], (0, 0, 0))
    drawline(project_vertex(vCf)[0], project_vertex(vCf)[1],project_vertex(vCb)[0], project_vertex(vCb)[1], (0, 0, 0))
    drawline(project_vertex(vDf)[0], project_vertex(vDf)[1],project_vertex(vDb)[0], project_vertex(vDb)[1], (0, 0, 0))

    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            exit = True
    pygame.display.update()