import pygame
import random

class Enemy(pygame.sprite.Sprite):
	def __init__(self, game_instance):
		super().__init__()
		self.screen = game_instance.screen
		self.screen_rect = self.screen.get_rect()
		self.frames = [
			pygame.image.load('enemy.png'),
			pygame.image.load('enemy_damaged.png')
			]
		self.image = self.frames[0]
		self.rect = self.image.get_rect()
		self.rect.midright = self.screen_rect.midright
		self.x_speed = 6
		self.y_speed = 2 + random.randint(-1, 1)
		self.movement_direction = 1 # 1 for downwards, -1 for upwards
		self.hit_points = 3

	def update(self):
		self.rect.x -= self.x_speed
		self.rect.y += self.y_speed * self.movement_direction
		if self.rect.bottom >= self.screen_rect.bottom:
			self.movement_direction = -1
		if self.rect.top <= self.screen_rect.top:
			self.movement_direction = 1
