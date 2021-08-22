import pygame
from random import randint, choice

from data.settings import *
from data.pg_innit import screen


next_condition_field = [[0 for w in range(divide_width)] for h in range(divide_height)]
current_condition_field = [[randint(0, 1) for w in range(divide_width)] for h in range(divide_height)]

def get_the_random_color_rect():
    """ Just a random cells color """
    return randint(0, 55), randint(0, 55), randint(0, 55)


def get_the_random_color_circle():
    """ Just a random cells color """
    return randint(100, 255), 50, randint(100, 255)


def get_circle_and_rect(x, y):
    two_figure = []
    rect = pygame.draw.rect(screen, pygame.Color(get_the_random_color_rect()), (x * cell_size - 1, y * cell_size - 1,
                                                                                cell_size, cell_size))
    circle = pygame.draw.circle(screen, pygame.Color(get_the_random_color_circle()),
                                (x * cell_size + 5, y * cell_size + 5),
                                cell_radius)
    two_figure.append(rect)
    two_figure.append(circle)
    return choice(two_figure)


def check_the_life(current_cnd_field, osx, osy):
    """ Check the cell's neighbors by two cycles j and i"""
    count = 0
    for j in range(osy - 1, osy + 2):
        for i in range(osx - 1, osx + 2):
            if current_cnd_field[j][i]:
                count += 1
    if current_cnd_field[osy][osx]:
        count -= 1
        if count == 2 or count == 3:
            return 1
        return 0
    else:
        if count == 3:
            return 1
        return 0