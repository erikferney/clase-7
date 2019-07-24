import pygame, math
from pygame.sprite import Sprite
from pygame.locals import *
from bullet import Bullet
import util

class Heroe(Sprite):
	def __init__(self, contenedor):
		Sprite.__init__(self)
		self.puntos = 0
		self.vida = 10000
		self.angulo = 0
		self.radio = 8
		self.vel = [0,0]
		self.contenedor = contenedor
		self.estado = "bajando"
		self.imagenes = [util.cargar_imagen('imagenes/Mammooth.png'),
						util.cargar_imagen('imagenes/Mammoth_Happy.png'),
						util.cargar_imagen('imagenes/Mammoth_Back.png'),
						util.cargar_imagen('imagenes/Mammoth_Seated.png')]
		self.image = self.imagenes[0]
		self.rect = self.image.get_rect()
		self.rect.move_ip(200, 10)
		self.bullets = []

	def update(self):
		teclas = pygame.key.get_pressed()
		if self.vida > 0:					
			if teclas[K_LEFT] and self.rect.x>=10:
				self.rect.x -= 10
				self.angulo = 180
			elif teclas[K_RIGHT] and self.rect.x<=640-self.rect.width:
				self.rect.x += 10
				self.angulo = 0
			if teclas[K_UP] and self.rect.y>=10:
				self.angulo = 90
				self.rect.y -= 10
				self.image = self.imagenes[2]
				if self.rect.y==0 and self.estado == "subiendo":
					self.puntos = self.puntos + 1
					self.estado = "bajando"
			elif teclas[K_DOWN] and self.rect.y<=480-self.rect.height:
				self.angulo = 270
				self.rect.y += 10
				self.image = self.imagenes[0]
				if self.rect.y==410 and self.estado == "bajando":
					self.puntos = self.puntos + 1
					self.estado = "subiendo"
			
			elif teclas[K_SPACE]:
				self.disparar()
		else:
			self.image = self.imagenes[3]
	
	def disparar(self):
		#self.disparo.play()
		vector = [0,0]
		vector[0] += math.cos(math.radians((self.angulo)%360))
		vector[1] -= math.sin(math.radians((self.angulo)%360))
		#pos = [self.rect.left + self.radio * vector[0], self.rect.bottom + self.radio * vector[1]]
		pos = [self.rect.x + self.radio, self.rect.y + self.radio]
		vel = [self.vel[0] + 6 * vector[0], self.vel[1] + 6 * vector[1]]
		self.bullets.append(Bullet(pos,self.angulo, vel, self.contenedor))