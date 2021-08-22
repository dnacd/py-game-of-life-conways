import pygame
from random import choice

spath = 'data/soundbanks/'
example_sounds = []
for sbank in (f'{spath}Chiptronical.ogg', '{spath}InterstellarOdyssey.ogg', '{spath}SolveThePuzzle.ogg'):
    example_sounds.append(sbank)
    
def sound_on():
    sound_on = input('Start GoL with soundbanks?[Y/N]: ').lower()
    if sound_on == 'y':
        load, play = pygame.mixer.music.load(choice(example_sounds)), pygame.mixer.music.play()
        return load, play