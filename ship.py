import pygame

class Ship:
	def __init__(self, game_instance):
		'''Initialise the player ship and its attributes'''
		self.screen = game_instance.screen
		self.image = pygame.image.load('fish-spaceship-game-character.png')
		self.rect = self.image.get_rect()
		self.screen_rect = game_instance.screen.get_rect()
		self.rect.midleft = self.screen_rect.midleft

		self.speed = 5
		self.moving_up = False
		self.moving_down = False
		self.moving_left = False
		self.moving_right = False

		self.firing = False
		self.time_last_fired = 0

	def blit_me(self):
		'''Blit the player ship to the screen'''
		self.screen.blit(self.image, self.rect)

	def move_ship(self):
		'''Update the ship's position'''
		if self.moving_up and self.rect.top > self.screen_rect.top:
			self.rect.y -= self.speed
		if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
			self.rect.y += self.speed
		if self.moving_left and self.rect.left > self.screen_rect.left:
			self.rect.x -= self.speed
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.rect.x += self.speed

