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
    a = Dy / Dx
    y = y0
    for x in range(x0, x1+1):
        putpixel(x, y, (cor))
        y = y + a

exit = False
  
while not exit:

    canvas.fill((255, 255, 255))

    drawline(0, 0, 240, 120, (0, 0, 0))
    drawline(0, 0, 60, 240, (0, 0, 0))
    drawline(60, 240, 240, 120, (0, 0, 0))

    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            exit = True
    pygame.display.update()