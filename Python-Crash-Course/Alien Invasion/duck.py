import pygame

class Duck():

    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('images/duck.bmp')
        self.rect = self.image.get_rect()
        screen_rect = screen.get_rect()
        self.rect.centerx = screen_rect.centerx
        self.rect.centery = screen_rect.centery

    def blitme(self):
        self.screen.blit(self.image, self.rect)
