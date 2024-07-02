import pygame
from player import *
import random
import os

pygame.init()

counter = 0

font = pygame.font.SysFont('ghastly_panic_cyr', 45)
font2 = pygame.font.SysFont('ghastly_panic_cyr', 80)

lose = False

d = pygame.display.set_mode((700, 500))
pygame.display.set_caption('резняяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяя')

image_folder = os.path.abspath('.')
pygame.mixer.music.load(os.path.join(image_folder, 'space.ogg'))
# pygame.mixer.music.play(-1)

game = True
clock = pygame.time.Clock()

p_img = pygame.image.load(os.path.join(image_folder, 'rocket.png'))
e_img = pygame.image.load(os.path.join(image_folder, 'ufo.png'))
a_img = pygame.image.load(os.path.join(image_folder, 'asteroid.png'))

back = pygame.transform.scale(pygame.image.load(os.path.join(image_folder, 'galaxy.jpg')), (700, 500))

group = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
bullets = pygame.sprite.Group()

for i in range(6):
    group.add(Enemy(e_img, random.randint(1, 5), random.randint(100, 600), int('-' + str(random.randint(20, 52))), 80, 100))

for i in range(3):
    asteroids.add(Asteroid(a_img, random.randint(3, 7), random.randint(100, 600), int('-' + str(random.randint(20, 52))), 50, 50))

player = Player(p_img, 5, 350, 350, 80, 100)

last_time = time()

while game:
    d.fill((0, 0, 0))
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            game = False

    d.blit(back, (0, 0))

    if not lose:
        if player.rel_time:
            now_time = time()
            if now_time - last_time < 3:
                reload = font.render('ПЕРЕЗАРЯДКА', True, (255, 0, 0))
                d.blit(reload, (320, 200))
            else:
                player.cur_fire = 0
                player.rel_time = False

        player.move(d, bullets)
        group.update(d)
        asteroids.update(d, player)

        if len(bullets) > 0:
            bullets.draw(d)
            bullets.update(group)

        text = font.render('Пропущенно: ' + str(counter), 1, (255, 0, 0))
        text2 = font.render('Убито: ' + str(kills), 1, (255, 0, 0))

        if lives == 3:
            text3 = font.render('Жизни: ' + str(lives), 1, (0, 255, 0))
        elif lives == 2:
            text3 = font.render('Жизни: ' + str(lives), 1, (255, 255, 0))
        else:
            text3 = font.render('Жизни: ' + str(lives), 1, (255, 0, 0))

        d.blit(text, (20, 20))
        d.blit(text2, (20, 60))
        d.blit(text3, (20, 100))

        if counter == 3 or kills == 10 or lives == 0:
            lose = True
    else:
        pygame.mixer.music.stop()
        if counter == 3 or lives == 0:
            text = font.render('YOU LOSE!!! HAHAHAHAHAH', 1, (255, 0, 0))
        elif kills == 10:
            text = font.render('YOU WIN!!! HAHAHAHAHAH', 1, (0, 255, 0))
        d.blit(text, (40, 250))

    clock.tick(60)
    pygame.display.flip()import pygame
from player import *
import random
import os

pygame.init()

counter = 0

font = pygame.font.SysFont('ghastly_panic_cyr', 45)
font2 = pygame.font.SysFont('ghastly_panic_cyr', 80)

lose = False

d = pygame.display.set_mode((700, 500))
pygame.display.set_caption('резняяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяя')

image_folder = os.path.abspath('.')
pygame.mixer.music.load(os.path.join(image_folder, 'space.ogg'))
# pygame.mixer.music.play(-1)

game = True
clock = pygame.time.Clock()

p_img = pygame.image.load(os.path.join(image_folder, 'rocket.png'))
e_img = pygame.image.load(os.path.join(image_folder, 'ufo.png'))
a_img = pygame.image.load(os.path.join(image_folder, 'asteroid.png'))

back = pygame.transform.scale(pygame.image.load(os.path.join(image_folder, 'galaxy.jpg')), (700, 500))

group = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
bullets = pygame.sprite.Group()

for i in range(6):
    group.add(Enemy(e_img, random.randint(1, 5), random.randint(100, 600), int('-' + str(random.randint(20, 52))), 80, 100))

for i in range(3):
    asteroids.add(Asteroid(a_img, random.randint(3, 7), random.randint(100, 600), int('-' + str(random.randint(20, 52))), 50, 50))

player = Player(p_img, 5, 350, 350, 80, 100)

last_time = time()

while game:
    d.fill((0, 0, 0))
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            game = False

    d.blit(back, (0, 0))

    if not lose:
        if player.rel_time:
            now_time = time()
            if now_time - last_time < 3:
                reload = font.render('ПЕРЕЗАРЯДКА', True, (255, 0, 0))
                d.blit(reload, (320, 200))
            else:
                player.cur_fire = 0
                player.rel_time = False

        player.move(d, bullets)
        group.update(d)
        asteroids.update(d, player)

        if len(bullets) > 0:
            bullets.draw(d)
            bullets.update(group)

        text = font.render('Пропущенно: ' + str(counter), 1, (255, 0, 0))
        text2 = font.render('Убито: ' + str(kills), 1, (255, 0, 0))

        if lives == 3:
            text3 = font.render('Жизни: ' + str(lives), 1, (0, 255, 0))
        elif lives == 2:
            text3 = font.render('Жизни: ' + str(lives), 1, (255, 255, 0))
        else:
            text3 = font.render('Жизни: ' + str(lives), 1, (255, 0, 0))

        d.blit(text, (20, 20))
        d.blit(text2, (20, 60))
        d.blit(text3, (20, 100))

        if counter == 3 or kills == 10 or lives == 0:
            lose = True
    else:
        pygame.mixer.music.stop()
        if counter == 3 or lives == 0:
            text = font.render('YOU LOSE!!! HAHAHAHAHAH', 1, (255, 0, 0))
        elif kills == 10:
            text = font.render('YOU WIN!!! HAHAHAHAHAH', 1, (0, 255, 0))
        d.blit(text, (40, 250))

    clock.tick(60)
    pygame.display.flip()