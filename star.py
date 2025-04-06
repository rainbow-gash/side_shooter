import pygame

class Star(pygame.sprite.Sprite):
	def __init__(self, game_instance, star_speed, star_image):
		super().__init__()
		self.screen = game_instance.screen
		self.screen_rect = self.screen.get_rect()
		self.image = pygame.image.load(star_image)
		self.star_speed = star_speed
		self.rect = self.image.get_rect()
		self.rect.x = 0
		self.rect.y = 0

	def update(self):
		'''Move the star left and reset it when it hits the edge.'''
		self.rect.x -= self.star_speed
		if self.rect.x <= 0:
			self.rect.x = self.screen_rect.right
