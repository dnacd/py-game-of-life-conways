import pygame
from data.settings import resolution

icon = pygame.image.load('data/images/cell.png')
screen = pygame.display.set_mode(resolution)
clock = pygame.time.Clock()

background_image = pygame.image.load('data/images/Background.png')

def pygame_init():
    p_init = pygame.init()
    p_caption = pygame.display.set_caption('Game of life')
    p_icon = pygame.display.set_icon(icon)
    return p_init, p_caption, p_icon