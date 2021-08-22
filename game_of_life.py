import pygame
from random import randint, choice
from copy import deepcopy

from data.settings import *
from data.pg_innit import pygame_init, screen, background_image, clock
from data.crect import *
from data.soundbanks.sounds import sound_on


if __name__ == "__main__":
    print(instruction)
    pygame_init()
    sound_on()

    try:
        genrate = int(input("Generation per second? (better 10-15) "))
    except:
        print('in GenRate must be only integers')
           
    while True:
        screen.blit(background_image, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        for x in range(1, divide_width - 1):
            for y in range(0, divide_height - 1):
                if current_condition_field[y][x]:
                    get_circle_and_rect(x, y)
                next_condition_field[y][x] = check_the_life(current_condition_field, x, y)
        current_condition_field = deepcopy(next_condition_field)

        pygame.display.flip()
        clock.tick(genrate)
        print(f"GenPS: {int(clock.get_fps())}")