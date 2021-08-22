import pygame
from random import choice

example_sounds = []
for sbank in (f'data/soundbanks/Chiptronical.ogg', 'data/soundbanks/InterstellarOdyssey.ogg', 'data/soundbanks/SolveThePuzzle.ogg'):
    example_sounds.append(sbank)
    
def sound_on():
    sound_on = input('Start GoL with soundbanks?[Y/N]: ').lower()
    if sound_on == 'y':
        load, play = pygame.mixer.music.load(choice(example_sounds)), pygame.mixer.music.play()
        return load, play