'''Classes for objects that are involved in my game'''


import pygame
import random
from helpers import load_image


# Game object classes
class Pig(pygame.sprite.Sprite):
    '''moves a clenched fist on the screen, follows the mouse
    but since i dont have the fist img ill just use the pigs'''
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)  # call the initializer for sprite class when init the pig class
        self.image, self.rect = load_image('amy.PNG', (150, 150))
        self.eating = 0

    def update(self):
        '''move the fist based on the mouse position'''
        pos = pygame.mouse.get_pos()  # gets position for mouse
        self.rect.midtop = pos
        if self.eating:
            self.rect.move_ip(5, 10)  # offsets the sprite if there is eating

    def eat(self, target):
        '''returns tru if pig is eating'''
        if not self.eating:
            self.eating = 1
            hitbox = self.rect.inflate(-5, -5)
            return hitbox.colliderect(target.rect)

    def uneat(self):
        '''called to uneat'''
        self.eating = 0


class Carrot(pygame.sprite.Sprite):
    '''moves a carrot acrosse the screen and spins when it
    is being eaten by the pig'''
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)  # init the sprites constructor again
        self.image, self.rect = load_image('carrot.png', (100, 100), (0, 0))

        transcolor = self.image.get_at((0, 0))
        self.image.set_colorkey(transcolor)  # make horrible white border transparent

        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.rect.topleft = random.randint(10, 500), random.randint(10, 300)
        self.xmove = random.randint(1, 10)
        self.ymove = random.randint(1, 10)
        self.dizzy = 0

    def update(self):
        '''walk or spin pending on monkey state'''
        if self.dizzy:
            self._spin()
        else:
            self._walk()

    def _walk(self):
        '''TODO: implement physics to run around randomly'''
        newpos = self.rect.move((self.xmove, self.ymove))
        if not self.area.contains(newpos):
            if self.rect.left < self.area.left or self.rect.right > self.area.right:
                self.xmove = -self.xmove
            if self.rect.top < self.area.top or self.rect.bottom > self.area.bottom:
                self.ymove = -self.ymove
            newpos = self.rect.move((self.xmove, self.ymove))
            self.image = pygame.transform.flip(self.image, 1, 0)
        self.rect = newpos

    def _spin(self):
        '''spin the monkey image'''
        center = self.rect.center
        self.dizzy += 12  # rotate in 12 degree increments until a full circle
        if self.dizzy >= 360:
            self.dizzy = 0
            self.image = self.original
        else:
            rotate = pygame.transform.rotate
            self.image = rotate(self.original, self.dizzy)
        self.rect = self.image.get_rect(center=center)

    def eaten(self):
        '''causes carrot to start spinning'''
        if not self.dizzy:
            self.dizzy = 1
            self.original = self.image
