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
background = pygame.image.load('sleepless subaru.jpg')
pygame.display.set_caption("space invader")
icon = pygame.image.load('Serpo_alien-removebg-preview.png')
pygame.display.set_icon(icon)
player_image = pygame.image.load('obama_prism2-removebg-preview.png')
player_x = player_start_x
player_y = player_start_y
player_x_change = 0
enemy_image = []
enemy_x = []
enemy_y = []
enemy_x_change = []
enemy_y_change = []
number_of_enemies = 8
for _i in range(number_of_enemies):
    enemy_image.append(pygame.image.load('petrification_device-removebg-preview.png'))
    enemy_x.append(random.randint(0, screen_width - 64))
    enemy_y.append(random.randint(enemy_start_y_min, enemy_start_y_max))
    enemy_x_change.append(enemy_speed_x)
    enemy_y_change.append(enemy_speed_y)
bullet_image = pygame.image.load('diamond_sword-removebg-preview.png')
bullet_x = 0
bullet_y = player_start_y
bullet_x_change = 0
bullet_y_change = bullet_speed_y
bullet_state = "available"
score_value = 0
font = pygame.font.Font('freensansbold.ttf', 32)
text_x = 10
text_y = 10
game_over_font = pygame.font.Font('freesansbold.ttf', 64)
def show_score(x, y):
    score = font.render("score:" + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))
def game_over_text():
    game_over_text = game_over_font.render("GAME OVER HOW DO U FEEL ABOUT URSELF HUH? U JUST FAILED THE UNIVERSE", True, (255, 255, 255))
    screen.blit(game_over_text, (200, 250))
def player(x, y):
    screen.blit(player_image, (x, y))
def enemy(x, y, i):
    screen.blit(enemy_image[i], (x, y))
def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_image, (x + 16, y + 10))