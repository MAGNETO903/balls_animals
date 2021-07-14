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

    def spawn(self):
        self.status = 'active'

    def hide(self):
        self.status = 'inventory'


    def update(self, *args):
        #if self.status == 'active':
        ground = args[2]
        self.speed_x = args[1]
        self.rect.x += self.speed_x

        if self.rect.left < 0:
            self.rect.left = 0
            self.speed_x *= -1

        if self.rect.right > args[0]:
            self.rect.right = args[0]
            self.speed_x *= -1

        if self.speed_y <= self.jump_force:
            if self.rect.bottom + self.speed_y < ground:
                #self.rect.bottom += self.speedy
                if self.speed_y < self.jump_force:
                    self.speed_y += self.gravity

            else:
                self.rect.bottom = ground
                self.speed_y = 0

        self.rect.y += self.speed_y
        #print(self.rect.bottom, ground)
        if abs(self.rect.bottom - ground) < 0.01:

            self.speed_y = -self.jump_force