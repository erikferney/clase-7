import sys, pygame

size = width, height = 640, 400

screen = pygame.display.set_mode(size)

def main():
    pygame.init()
    
    court = pygame.image.load("space.png")
    courtrect = court.get_rect()
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()
                
        screen.blit(court, courtrect)
        courtrect.scroll(0 ,-2)
        pygame.display.update()

if __name__ == '__main__': 
    main()