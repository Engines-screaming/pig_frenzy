'''Utility functions to help load images and sounds'''

import pygame
import os
from pygame.locals import *

def load_image(name, resize=None, pixel_loc=None):
    '''Try to load in the image and exit with a clean
    error message. optional args to resize to a tuple.
    colorkey takes in a tuple of pixel loc
    to make transparent'''

    fullname = os.path.join('imgs', name)

    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)

    image = image.convert()  # necessary to make blits faster

    # optional argument parsing
    if pixel_loc is not None:
        colorkey = image.get_at(pixel_loc)
        image.set_colorkey(colorkey, RLEACCEL)
    if resize is not None:
        image = pygame.transform.scale(image, resize)
    return image, image.get_rect()


def load_sound(name):
    # Checks to see if mixer module was loaded
    # if not, returns class with dummy play sound to work without error checking
    class NoneSound:
        def play(self): pass
    if not pygame.mixer:
        return NoneSound()
    fullname = os.path.join('sounds', name)
    try:
        sound = pygame.mixer.Sound(fullname)  # loads a sound file
    except pygame.error as message:
        print('Cannot load sound:', name)
        raise SystemExit(message)
    return sound
