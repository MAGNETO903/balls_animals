import pygame
import random
from telega import Telega
from ball import Ball

pygame.init()

size = [900, 570]
display = pygame.display.set_mode(size)

clock = pygame.time.Clock()
FPS = 60

white = (255, 255, 255)
black = (0, 0, 0)
grey = (127, 127, 127)

balls_data = ({'image': 'images/ball_bear.png', 'score': 1},
              {'image': 'images/ball_fox.png', 'score': 2},
              {'image': 'images/ball_hed.png', 'score': 4},
              {'image': 'images/ball_kitten.png', 'score': 8},
              {'image': 'images/ball_lemur.png', 'score': 16},
              {'image': 'images/ball_lion.png', 'score': 32})

score_bg = pygame.image.load('images/score_fon.png').convert_alpha()
score_font = pygame.font.SysFont('arial', 30)
score = 0

bg = pygame.image.load('images/back1.jpg').convert()
balls_img = []
for ball_data in balls_data:
    ball_img = pygame.image.load(ball_data['image']).convert()
    balls_img.append(ball_img)

balls = pygame.sprite.Group()
balls_amount = 0
telega = Telega(size[0] / 2, size[1])

ground = telega.rect.centery

balls.add(Ball(size[0] / 2, telega.rect.top, balls_data[0]['image'], balls_data[0]['score'], 0))

cell_size = 50
cell_margin = 10
coins = 0

inventory = [0, 1, 2, 0, 1, 2, 1]

#def draw_inventory():
inventory_surf = pygame.Surface((cell_size*4+cell_margin*5, cell_size*4 + cell_margin*5))
for x in range(4):
    for y in range(4):

        pygame.draw.rect(inventory_surf, grey, pygame.Rect(x*(cell_size+cell_margin)+cell_margin, y*(cell_size+cell_margin)+cell_margin, cell_size, cell_size))
        inventory_surf.set_alpha(128)

#def draw_shop():
shop_surf = pygame.Surface((cell_size*3+cell_margin*4, cell_size*len(balls_img) + cell_margin*(len(balls_img)+1)))
for y in range(len(balls_img)):
    cur_ball_img = pygame.transform.scale(balls_img[y], (cell_size, cell_size))
    shop_surf.blit(cur_ball_img, (cell_margin, y*(cell_size+cell_margin)+cell_margin))
    img_text = score_font.render('[{}] - {}'.format(y+1, balls_data[y]['score']*5), True, (255, 255, 255))

    shop_surf.blit(img_text, (cell_margin*2 + cell_size, y*(cell_size+cell_margin)+cell_margin))

def draw_inventory():
    shift = size[0] - inventory_surf.get_width()
    for i in range(len(inventory)):
        cur_ball_img = pygame.transform.scale(balls_img[inventory[i]], (cell_size, cell_size))
        x = i % 4
        y = i // 4
        display.blit(cur_ball_img, (x*(cell_size+cell_margin)+cell_margin + shift, y*(cell_size+cell_margin)+cell_margin))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                if score >= balls_data[0]['score'] * 5:
                    score -= balls_data[0]['score'] * 5
                    balls_amount += 1
                    balls.add(Ball(random.randrange(telega.rect.left, telega.rect.right), telega.rect.top, balls_data[0]['image'], balls_data[0]['score'], 0))
            elif event.key == pygame.K_2:
                if score >= balls_data[1]['score'] * 5:
                    score -= balls_data[1]['score'] * 5
                    balls_amount += 1
                    balls.add(Ball(random.randrange(telega.rect.left, telega.rect.right), telega.rect.top, balls_data[1]['image'], balls_data[1]['score'], 1))
            elif event.key == pygame.K_3:
                if score >= balls_data[2]['score'] * 5:
                    score -= balls_data[2]['score'] * 5
                    balls_amount += 1
                    balls.add(Ball(random.randrange(telega.rect.left, telega.rect.right), telega.rect.top, balls_data[2]['image'], balls_data[2]['score'], 2))
            elif event.key == pygame.K_4:
                if score >= balls_data[3]['score'] * 5:
                    score -= balls_data[3]['score'] * 5
                    balls_amount += 1
                    balls.add(
                        Ball(random.randrange(telega.rect.left, telega.rect.right), telega.rect.top, balls_data[3]['image'], balls_data[3]['score'], 3))
            elif event.key == pygame.K_5:
                if score >= balls_data[4]['score'] * 5:
                    score -= balls_data[4]['score'] * 5
                    balls_amount += 1
                    balls.add(
                        Ball(random.randrange(telega.rect.left, telega.rect.right), telega.rect.top, balls_data[4]['image'], balls_data[4]['score'], 4))
            elif event.key == pygame.K_6:
                if score >= balls_data[5]['score'] * 5:
                    score -= balls_data[5]['score'] * 5
                    balls_amount += 1
                    balls.add(
                        Ball(random.randrange(telega.rect.left, telega.rect.right), telega.rect.top, balls_data[5]['image'], balls_data[5]['score'], 5))


    telega.update(size[0])
    balls.update(size[0], telega.speed, ground)

    display.blit(bg, (0, 0))

    score_text = score_font.render(str(score), True, (95, 140, 15))
    display.blit(score_bg, (0, 0))
    display.blit(score_text, (20, 10))
    inventory = []
    i=0
    for ball in balls:
        i+=1
        #if ball.status == 'active':
        display.blit(ball.image, ball.rect)
        if abs(ball.rect.bottom - ground) < 0.01:
            score += ball.score
    #else:

        if (balls_amount>15):


            j=0
            for ball1 in balls:
                if j == 0:
                    ball1.kill()
                    balls_amount -= 1
                    break
                j += 1
            inventory.insert(0, ball.ball_type)
        else:
            inventory.append(ball.ball_type)




    #balls.draw(display)
    display.blit(telega.image, telega.rect)

    display.blit(inventory_surf, ((size[0] - inventory_surf.get_width(), 0)))
    display.blit(shop_surf, (0, size[1]*0.2))





    draw_inventory()

    pygame.display.update()
    clock.tick(FPS)