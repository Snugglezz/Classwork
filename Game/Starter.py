import pygame
import os
from pygame.examples.moveit import HEIGHT
from pygame.transform import scale
from setuptools.command.build_ext import if_dl

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Dirt Trial')

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

BORDER = pygame.rect(WIDTH/2 - 5, 0, 10, HEIGHT)

FPS = 60
VEL = 5
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40

YELLOW_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join("Assets","spaceship_yellow.png"))
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    YELLOW_SPACESHIP_IMAGE,(SPACESHIP_WIDTH, SPACESHIP_HEIGHT)),90)

RED_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join("Assets","spaceship_red.png"))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    RED_SPACESHIP_IMAGE,(SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)

def draw_window(red, yellow):
    WIN.fill(WHITE)
    pygame.draw.rect(WIN, BLACK, BORDER)
    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP, (red.x, red.y))
    pygame.display.update()

def yellow_handle_movement(keys_pressed, yellow):
    if keys_pressed[pygame.K_a]:  # Left
        yellow.x -= VEL
    if keys_pressed[pygame.K_d]:  # Right
        yellow.x += VEL
    if keys_pressed[pygame.K_w]:  # up
        yellow.y -= VEL
    if keys_pressed[pygame.K_s]:  # down
        yellow.y += VEL

def red_handle_movement(keys_pressed, red):
    if keys_pressed[pygame.K_LEFT]:  # Left
        red.x -= VEL
    if keys_pressed[pygame.K_RIGHT]:  # Right
        red.x += VEL
    if keys_pressed[pygame.K_UP]:  # up
        red.y -= VEL
    if keys_pressed[pygame.K_DOWN]:  # down
        red.y += VEL

def main():
    red = pygame.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys_pressed = pygame.key.get_pressed()
        yellow_handle_movement(keys_pressed, yellow)
        red_handle_movement(keys_pressed, red)
        draw_window(red, yellow)

    pygame.quit()

if __name__ == '__main__':
   main()