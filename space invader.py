import math
import random
import pygame
screen_width = 800
screen_height = 500
player_start_x = 370
player_start_y = 380
enemy_start_y_min = 50
enemy_start_y_max = 150
enemy_speed_x = 4
enemy_speed_y = 40
bullet_speed_y = 10
collision_distance = 27
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
background = pygame.image.load('background.png')
pygame.display.set_caption("space invader")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)
player_image = pygame.image.load('player.png')
player_x = player_start_x
player_y = player_start_y
player_x_change = 0
enemy_image = []
enemy_x = []
enemy_y = []
enemy_x_change = []
enemy_y_change = []
number_of_enemies = 6
for _i in range(number_of_enemies):
    enemy_image.append(pygame.image.load('enemy.png'))
    enemy_x.append(random.randint(0, screen_width - 64))
    enemy_y.append(random.randint(enemy_start_y_min, enemy_start_y_max))
    enemy_x_change.append(enemy_speed_x)
    enemy_y_change.append(enemy_speed_y)
bullet_image = pygame.image.load('bullet.png')
bullet_x = 0
bullet_y = player_start_y
bullet_x_change = 0
bullet_y_change = bullet_speed_y
bullet_state = "ready"
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
text_x = 10
text_y = 10
game_over_font = pygame.font.Font('freesansbold.ttf', 64)
def show_score(x, y):
    score = font.render("score:" + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))
def game_over_text():
    game_over_text = game_over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(game_over_text, (200, 250))
def player(x, y):
    screen.blit(player_image, (x, y))
def enemy(x, y, i):
    screen.blit(enemy_image[i], (x, y))
def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_image, (x + 16, y + 10))
def iscollision(enemy_x, enemy_y, bullet_x, bullet_y):
    distance = math.sqrt((enemy_x - bullet_x) ** 2 + (enemy_y - bullet_y) ** 2)
    return distance < collision_distance
running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change = -5
            if event.key == pygame.K_RIGHT:
                player_x_change = 5
            if event.key == pygame.K_SPACE and bullet_state == "ready":
                bullet_x = player_x
                fire_bullet(bullet_x, bullet_y)
        if event.type == pygame.KEYUP and event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
            player_x_change = 0
    player_x += player_x_change
    player_x = max(0, min(player_x, screen_width - 64))
    for i in range(number_of_enemies):
        if enemy_y[i] > 340:
            for j in range(number_of_enemies):
                enemy_y[j] = 2000
            game_over_text()
            break
        enemy_x[i] += enemy_x_change[i]
        if enemy_x[i] <= 0 or enemy_x[i] >= screen_width - 64:
            enemy_x_change[i] *= -1
            enemy_y[i] += enemy_y_change[i]
        if iscollision(enemy_x[i], enemy_y[i], bullet_x, bullet_y):
            bullet_y = player_start_y
            bullet_state = "ready"
            score_value += 1
            enemy_x[i] = random.randint(0, screen_width - 64)
            enemy_y[i] = random.randint(enemy_start_y_min, enemy_start_y_max)
        enemy(enemy_x[i], enemy_y[i], i)
    if bullet_y <= 0:
        bullet_y = player_start_y
        bullet_state = "ready"
    elif bullet_state == "fire":
        fire_bullet(bullet_x, bullet_y)
        bullet_y -= bullet_y_change
    player(player_x, player_y)
    show_score(text_x, text_y)
    pygame.display.update()