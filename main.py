import pygame
import random
import var
import time
from Person import *
from os import path

img_dir = path.join(path.dirname(__file__), 'img')

SeeWhoIsIt = True

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((var.WIDTH, var.HEIGHT))
pygame.display.set_caption("Pokemon Game ")
clock = pygame.time.Clock()
# screen.fill(var.background)
screen.fill(var.BLUE)
font_name = pygame.font.match_font('arial')


def draw_text(text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, var.WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    screen.blit(text_surface, text_rect)


all_sprites = pygame.sprite.Group()
MyCharac = Guy(var.BROWN)
all_sprites.add(MyCharac)
OtherGuy = Guy2(var.YELLOW)
GuyGroup = pygame.sprite.Group()
GuyGroup.add(OtherGuy)
all_sprites.add(OtherGuy)
A_Meteor = Meteor()
Meteor2 = Meteor()
Meteor3 = Meteor()
Meteor4 = Meteor()
Meteor5 = Meteor()
Meteor6 = Meteor()
Meteor7 = Meteor()
Meteor8 = Meteor()
Meteor9 = Meteor()
Meteor10 = Meteor()
all_sprites.add(Meteor2)
all_sprites.add(A_Meteor)
all_sprites.add(Meteor3)
all_sprites.add(Meteor4)
all_sprites.add(Meteor5)
all_sprites.add(Meteor6)
all_sprites.add(Meteor7)
all_sprites.add(Meteor8)
all_sprites.add(Meteor9)
all_sprites.add(Meteor10)
BigBoy = BigMeteor()
all_sprites.add(BigBoy)

running = True
while running:
    #                   check events                                                                                 now
    clock.tick(var.FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        else:
            pass
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                MyCharac.rect.x = random.randint(0, var.WIDTH)
                MyCharac.rect.y = random.randint(0, var.HEIGHT)
                OtherGuy.rect.x = random.randint(0, var.WIDTH)
                OtherGuy.rect.y = random.randint(0, var.HEIGHT)

    if A_Meteor.rect.x >= var.WIDTH - 5 or A_Meteor.rect.x <= 0:
        A_Meteor.rect.center = var.WIDTH / 2, var.HEIGHT / 2
    if A_Meteor.rect.y >= var.HEIGHT - 5 or A_Meteor.rect.y <= 0:
        A_Meteor.rect.center = var.WIDTH / 2, var.HEIGHT / 2
    if Meteor2.rect.x >= var.WIDTH - 5 or A_Meteor.rect.x <= 0:
        Meteor2.rect.center = var.WIDTH / 2, var.HEIGHT / 2
    if Meteor2.rect.y >= var.HEIGHT - 5 or A_Meteor.rect.y <= 0:
        Meteor2.rect.center = var.WIDTH / 2, var.HEIGHT / 2
    if Meteor3.rect.x >= var.WIDTH - 5 or A_Meteor.rect.x <= 0:
        Meteor3.rect.center = var.WIDTH / 2, var.HEIGHT / 2
    if Meteor3.rect.y >= var.HEIGHT - 5 or A_Meteor.rect.y <= 0:
        Meteor3.rect.center = var.WIDTH / 2, var.HEIGHT / 2
    if Meteor4.rect.x >= var.WIDTH - 5 or A_Meteor.rect.x <= 0:
        Meteor4.rect.center = var.WIDTH / 2, var.HEIGHT / 2
    if Meteor4.rect.y >= var.HEIGHT - 5 or A_Meteor.rect.y <= 0:
        Meteor4.rect.center = var.WIDTH / 2, var.HEIGHT / 2
    if Meteor5.rect.x >= var.WIDTH - 5 or A_Meteor.rect.x <= 0:
        Meteor5.rect.center = var.WIDTH / 2, var.HEIGHT / 2
    if Meteor5.rect.y >= var.HEIGHT - 5 or A_Meteor.rect.y <= 0:
        Meteor5.rect.center = var.WIDTH / 2, var.HEIGHT / 2
    if Meteor6.rect.x >= var.WIDTH - 5 or A_Meteor.rect.x <= 0:
        Meteor6.rect.center = var.WIDTH / 2, var.HEIGHT / 2
    if Meteor6.rect.y >= var.HEIGHT - 5 or A_Meteor.rect.y <= 0:
        Meteor6.rect.center = var.WIDTH / 2, var.HEIGHT / 2
    if Meteor7.rect.x >= var.WIDTH - 5 or A_Meteor.rect.x <= 0:
        Meteor7.rect.center = var.WIDTH / 2, var.HEIGHT / 2
    if Meteor7.rect.y >= var.HEIGHT - 5 or A_Meteor.rect.y <= 0:
        Meteor7.rect.center = var.WIDTH / 2, var.HEIGHT / 2
    if Meteor8.rect.x >= var.WIDTH - 5 or A_Meteor.rect.x <= 0:
        Meteor8.rect.center = var.WIDTH / 2, var.HEIGHT / 2
    if Meteor8.rect.y >= var.HEIGHT - 5 or A_Meteor.rect.y <= 0:
        Meteor8.rect.center = var.WIDTH / 2, var.HEIGHT / 2
    if Meteor9.rect.x >= var.WIDTH - 5 or A_Meteor.rect.x <= 0:
        Meteor9.rect.center = var.WIDTH / 2, var.HEIGHT / 2
    if Meteor9.rect.y >= var.HEIGHT - 5 or A_Meteor.rect.y <= 0:
        Meteor9.rect.center = var.WIDTH / 2, var.HEIGHT / 2
    if Meteor10.rect.x >= var.WIDTH - 5 or A_Meteor.rect.x <= 0:
        Meteor10.rect.center = var.WIDTH / 2, var.HEIGHT / 2
    if Meteor10.rect.y >= var.HEIGHT - 5 or A_Meteor.rect.y <= 0:
        Meteor10.rect.center = var.WIDTH / 2, var.HEIGHT / 2
    if BigBoy.rect.x >= var.WIDTH - 5 or A_Meteor.rect.x <= 0:
        BigBoy.rect.center = var.WIDTH / 2, var.HEIGHT / 2
    if BigBoy.rect.y >= var.HEIGHT - 5 or A_Meteor.rect.y <= 0:
        BigBoy.rect.center = var.WIDTH / 2, var.HEIGHT / 2

    hits = pygame.sprite.spritecollide(MyCharac, GuyGroup, False)
    if hits:
        MyCharac.rect.x = 0
        MyCharac.rect.y = 0
        OtherGuy.rect.x = var.WIDTH - 10
        OtherGuy.rect.y = var.HEIGHT - 10
        A_Meteor.rect.center = var.WIDTH / 2, var.HEIGHT / 2
        Meteor2.rect.center = var.WIDTH / 2, var.HEIGHT / 2
        Meteor3.rect.center = var.WIDTH / 2, var.HEIGHT / 2
        Meteor4.rect.center = var.WIDTH / 2, var.HEIGHT / 2
        Meteor5.rect.center = var.WIDTH / 2, var.HEIGHT / 2
        Meteor6.rect.center = var.WIDTH / 2, var.HEIGHT / 2
        Meteor7.rect.center = var.WIDTH / 2, var.HEIGHT / 2
        Meteor8.rect.center = var.WIDTH / 2, var.HEIGHT / 2
        Meteor9.rect.center = var.WIDTH / 2, var.HEIGHT / 2
        Meteor10.rect.center = var.WIDTH / 2, var.HEIGHT / 2
        if SeeWhoIsIt:
            SeeWhoIsIt = False
            time.sleep(0.5)
        else:
            SeeWhoIsIt = True
            time.sleep(0.5)

    # 2. Update
    all_sprites.update()

    # 3. Draw / render
    screen.fill(var.BLUE)
    all_sprites.draw(screen)

    if SeeWhoIsIt:
        draw_text("Player 1 is it", 20, var.WIDTH / 2, var.HEIGHT / 2)
        A_Meteor.image.fill(var.YELLOW)
        Meteor2.image.fill(var.YELLOW)
        Meteor3.image.fill(var.YELLOW)
        Meteor4.image.fill(var.YELLOW)
        Meteor5.image.fill(var.YELLOW)
        Meteor6.image.fill(var.YELLOW)
        Meteor7.image.fill(var.YELLOW)
        Meteor8.image.fill(var.YELLOW)
        Meteor9.image.fill(var.YELLOW)
        Meteor10.image.fill(var.YELLOW)
    else:
        draw_text("Player 2 is it", 20, var.WIDTH / 2, var.HEIGHT / 2)
        A_Meteor.image.fill(var.BROWN)
        Meteor2.image.fill(var.BROWN)
        Meteor3.image.fill(var.BROWN)
        Meteor4.image.fill(var.BROWN)
        Meteor5.image.fill(var.BROWN)
        Meteor6.image.fill(var.BROWN)
        Meteor7.image.fill(var.BROWN)
        Meteor8.image.fill(var.BROWN)
        Meteor9.image.fill(var.BROWN)
        Meteor10.image.fill(var.BROWN)
    # after drawing everything, flip the display
    pygame.display.flip()
    time.sleep(0.001)
