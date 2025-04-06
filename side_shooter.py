import pygame
import sys
import random

from ship import Ship
from star import Star

class Game:
	def __init__(self):
		'''Initialise the screen and create game assets'''
		pygame.init()

		# Initialise the game window and screen surface.
		pygame.display.set_caption('Side Shooter')
		self.screen = pygame.display.set_mode((1200, 800))
		self.screen_rect = self.screen.get_rect()

		self.clock = pygame.time.Clock()

		# Initialise assets including the ship and starfields.
		self.ship = Ship(self)
		self.fore_stars = pygame.sprite.Group()
		self.create_starfield(self.fore_stars, 7, 'star.png')
		self.mid_stars = pygame.sprite.Group()
		self.create_starfield(self.mid_stars, 4, 'mid_star.png')
		self.back_stars = pygame.sprite.Group()
		self.create_starfield(self.back_stars, 1, 'rear_star.png')
		self.bullets = pygame.sprite.Group()
		self.enemies = pygame.sprite.Group()

	def check_events(self):
		'''Check for player input'''
		for event in pygame.event.get():

			# Check for KEYDOWN events.
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					self.ship.moving_up = True
				if event.key == pygame.K_DOWN:
					self.ship.moving_down = True
				if event.key == pygame.K_LEFT:
					self.ship.moving_left = True
				if event.key == pygame.K_RIGHT:
					self.ship.moving_right = True
				if event.key == pygame.K_LSHIFT:
					self.ship.firing = True
				if event.key == pygame.K_q:
					sys.exit()

			# Check for KEYUP events.
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_UP:
					self.ship.moving_up = False
				if event.key == pygame.K_DOWN:
					self.ship.moving_down = False
				if event.key == pygame.K_LEFT:
					self.ship.moving_left = False
				if event.key == pygame.K_RIGHT:
					self.ship.moving_right = False
				if event.key == pygame.K_LSHIFT:
					self.ship.firing = False
			
			if event.type == pygame.QUIT:
				sys.exit()

	def create_starfield(self, array, star_speed, image):
		'''Create a semi-random grid of stars using a specified image.'''
		for row in range(0, 10):
			for column in range(0, 12):
				star = Star(self, star_speed, image)
				star.rect.x = (row * 120) + random.randint(-50, 50)
				star.rect.y = (column * 80) + random.randint(-50, 50)
				array.add(star)

	def fire_bullet(self):
		if self.ship.firing:
			current_time = pygame.time.get_ticks()
			if current_time - self.ship.time_last_fired > 200:
				new_bullet = Bullet(self)
				self.bullets.add(new_bullet)
				self.ship.time_last_fired = pygame.time.get_ticks()

	def remove_bullets(self):
		for bullet in self.bullets:
			if bullet.rect.left > 1200:
				self.bullets.remove(bullet)

	def run_game(self):
		'''The main game loop'''
		while True:
			self.clock.tick(60)
			self.screen.fill('black')
			self.check_events()
			self.ship.move_ship()
			self.back_stars.update()
			self.back_stars.draw(self.screen)
			self.mid_stars.update()
			self.mid_stars.draw(self.screen)		
			self.fore_stars.update()
			self.fore_stars.draw(self.screen)
			self.bullets.update()
			self.bullets.draw(self.screen)
			self.ship.blit_me()
			self.fire_bullet()
			self.remove_bullets()
			pygame.display.flip()


class Bullet(pygame.sprite.Sprite):
	def __init__(self, game_instance):
		super().__init__()
		self.screen = game_instance.screen
		self.screen_rect = self.screen.get_rect()
		self.image = pygame.image.load('bullet.png')
		self.rect = self.image.get_rect()
		self.rect.center = game_instance.ship.rect.midright

	def update(self):
		self.rect.x += 20


class Enemy(pygame.sprite.Sprite):
	def __init__(self, game_instance):
		super().__init__()
		self.screen = game_instance.screen
		self.screen_rect = self.screen.get_rect()
		self.image = pygame.image.load('enemy.png')
		self.rect = self.image.get_rect()

game = Game()
game.run_game()
