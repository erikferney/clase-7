import pygame
from pygame.sprite import Sprite
from pygame.locals import *

class Ufo(Sprite):
    def __init__(self, cont_size, starfleet_pos, starfleet_size):
        Sprite.__init__(self)
        self.vel = [2,0]
        self.starfleet_pos = starfleet_pos
        self.starfleet_size = starfleet_size
        self.cont_size = cont_size
        self.image = pygame.image.load("imagenes/ufo.png")
        self.rect = self.image.get_rect()
        pos_x = (self.cont_size[0] / starfleet_size) + (self.starfleet_pos * 65)
        self.rect.move_ip(pos_x, 10)
        
    def update(self):
        self.rect = self.rect.move(self.vel)
        left_max = (self.starfleet_pos * 65)
        right_max = self.cont_size[0] - (((self.starfleet_size - 1) - self.starfleet_pos) * 65)
        if self.rect.left < left_max or self.rect.right > right_max:
            self.vel[0] = -self.vel[0]
            self.rect.top += 5
    
