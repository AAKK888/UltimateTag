import random

import pygame
import var


class Guy(pygame.sprite.Sprite):
    def __init__(self, color):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20, 20))
        self.image.fill(color)
        self.image.set_colorkey(var.BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (0, var.HEIGHT / 2)
        self.xspeed = 0
        self.yspeed = 0

    def update(self):
        self.xspeed = 0
        self.yspeed = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_a]:
            self.xspeed = -7
        if keystate[pygame.K_d]:
            self.xspeed = 7
        if keystate[pygame.K_w]:
            self.yspeed = -7
        if keystate[pygame.K_s]:
            self.yspeed = 7
        if self.yspeed != 0 and self.xspeed != 0:
            self.yspeed /= 1.414
            self.xspeed /= 1.414

        self.rect.x += self.xspeed
        self.rect.y += self.yspeed
        if self.rect.right > var.WIDTH:
            self.rect.right = var.WIDTH - 1
        if self.rect.left < 0:
            self.rect.left = 1
        if self.rect.top < 0:
            self.rect.top = 1
        if self.rect.bottom > var.HEIGHT:
            self.rect.bottom = var.HEIGHT - 1


class Guy2(pygame.sprite.Sprite):
    def __init__(self, color):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20, 20))
        self.image.fill(color)
        self.image.set_colorkey(var.BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (var.WIDTH, var.HEIGHT / 2)
        self.xspeed = 0
        self.yspeed = 0

    def update(self):
        self.xspeed = 0
        self.yspeed = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.xspeed = -7
        if keystate[pygame.K_RIGHT]:
            self.xspeed = 7
        if keystate[pygame.K_UP]:
            self.yspeed = -7
        if keystate[pygame.K_DOWN]:
            self.yspeed = 7
        if self.yspeed != 0 and self.xspeed != 0:
            self.yspeed /= 1.414
            self.xspeed /= 1.414

        self.rect.x += self.xspeed
        self.rect.y += self.yspeed
        if self.rect.right > var.WIDTH:
            self.rect.right = var.WIDTH - 1
        if self.rect.left < 0:
            self.rect.left = 1
        if self.rect.top < 0:
            self.rect.top = 1
        if self.rect.bottom > var.HEIGHT:
            self.rect.bottom = var.HEIGHT - 1


class Meteor(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((22, 22))
        self.image.fill(var.RED)
        self.image.set_colorkey(var.BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = var.WIDTH / 2, var.HEIGHT / 2

    def update(self):
        self.rect.x += random.randint(7, 15)
        self.rect.y += random.randint(7, 15)
        self.rect.x -= random.randint(7, 15)
        self.rect.y -= random.randint(7, 15)


class BigMeteor(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(var.BLACK)
        self.image.set_colorkey(var.BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = var.WIDTH / 2, var.HEIGHT / 2

    def update(self):
        self.rect.x += random.randint(7, 70)
        self.rect.y += random.randint(7, 70)
        self.rect.x -= random.randint(7, 70)
        self.rect.y -= random.randint(7, 70)
