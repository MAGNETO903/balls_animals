import pygame

class Telega(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('images/telega.png').convert_alpha()
        self.rect = self.image.get_rect(centerx=x, bottom=y)
        self.speed = 1

    def update(self, *args):
        '''
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if key[pygame.K_RIGHT]:
            self.rect.x += self.speed

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > args[0]:
            self.rect.right = args[0]
        '''

        self.rect.x += self.speed

        if self.rect.left < 0:
            self.rect.left = 0
            self.speed *= -1

        if self.rect.right > args[0]:
            self.rect.right = args[0]
            self.speed *= -1




