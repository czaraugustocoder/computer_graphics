import pygame
  
pygame.init() 
  
# CREATING CANVAS 
canvas = pygame.display.set_mode((800, 800))

Cw , Ch = 800 // 2, 800 // 2

#putpixel function
def putpixel(X, Y, Color):
    pygame.draw.circle(canvas, Color, [Cw + X, Ch - Y], 10)

print(Cw , Ch)

exit = False
  
while not exit:

    canvas.fill((160, 160, 160))

    putpixel(300, 200, (255, 0, 0))
    putpixel(50, 200, (255, 0, 0))
    putpixel(200, 200, (255, 0, 0))
    putpixel(90, 200, (255, 0, 0))
    putpixel(300, -200, (255, 0, 0))
    putpixel(-300, 200, (255, 0, 0))

    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            exit = True
    pygame.display.update() 