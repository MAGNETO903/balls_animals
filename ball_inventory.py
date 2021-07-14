import pygame
import random

class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y, filename, score, ball_type):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert_alpha()
        self.rect = self.image.get_rect(
            centerx=x, bottom=y)
        self.speed_x = 1
        self.speed_y = 0
        self.jump_force = 10
        self.gravity = 0.2
        self.score = score
        self.status = 'inventory'
        self.ball_type = ball_type

