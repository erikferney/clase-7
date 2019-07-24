import sys, pygame
from pygame.locals import *
from ship import Ship
from ufo import Ufo

size = width, height = 800, 600
screen = pygame.display.set_mode(size)

def main():
    pygame.init()
    
    background_image = pygame.image.load("imagenes/space.png")
    background_rect = background_image.get_rect()
    
    pygame.display.set_caption( "asteroids" )
    
    ship = Ship(size)
    ufos = []
    for i in range(0,10):
        ufos.append(Ufo(size, i, 10))
    
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()
        
        ship.update()
        screen.blit(background_image, background_rect)
        screen.blit(ship.image, ship.rect)
        
        for bullet in ship.bullets:
            bullet.update()
            for ufo in ufos:
                if bullet.rect.colliderect(ufo.rect):
                    ship.bullets.remove(bullet)
                    ufos.remove(ufo)
            if bullet.rect.top <= 0:
                ship.bullets.remove(bullet)
            screen.blit(bullet.image, bullet.rect) 
        
        for ufo in ufos:
            ufo.update()
            screen.blit(ufo.image, ufo.rect) 
        
        pygame.display.update()
        pygame.time.delay(10)
            
if __name__ == '__main__': 
    main()
