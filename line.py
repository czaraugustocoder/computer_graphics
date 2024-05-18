import pygame
  
pygame.init() 

w , h = 600, 600
  
# CREATING CANVAS 
canvas = pygame.display.set_mode((w, h))

Cw , Ch = w // 2, h // 2

#putpixel function
def putpixel(X, Y, Color):
    pygame.draw.circle(canvas, Color, [Cw + X, Ch - Y], 2)

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
        for x in range(x0, x1+1):
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
        for y in range(y0, y1+1):
            putpixel(x, y, (cor))
            x = x + a

exit = False
  
while not exit:

    canvas.fill((255, 255, 255))

    drawline(-80, 140, 200, 260, (0, 0, 0))

    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            exit = True
    pygame.display.update()