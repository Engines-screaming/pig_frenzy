'''Main function for the hungry pig game'''


import pygame
from pygame.locals import *
from classes import Pig, Carrot
from helpers import load_sound, load_image


def main():
    # the main function
    pygame.init()
    pygame.font.init()
    pygame.mixer.init()  # not sure why i have to do this shit

    screen = pygame.display.set_mode((800, 480))
    pygame.display.set_caption('pig fever')
    pygame.mouse.set_visible(0)

    # create the background
    bg, bg_rect = load_image('grass.jpg')

    # display the background while setup finishes
    screen.blit(bg, bg_rect)  # blit the background
    pygame.display.flip()  # updates the areas that are changed using double buffer displays

    # objective text
    font = pygame.font.SysFont('Arial', 50)
    intro_text = font.render("Kill All the Carrots!", 1, (0, 0, 0))
    intro_text_pos = intro_text.get_rect()
    intro_text_pos.centerx = bg_rect.centerx
    bg.blit(intro_text, intro_text_pos)

    # # text for finishing the game
    font = pygame.font.SysFont('Arial', 70)
    end_text = font.render("PIG IS FED! GOOD JOB!", 1, (150, 0, 0))
    end_text_pos = end_text.get_rect()
    end_text_pos.centerx = bg_rect.centerx
    end_text_pos.bottom = bg_rect.bottom

    # prep game objects
    eating_sound = load_sound('owmylegs.wav')
    pig = Pig()

    carrot_objects = []
    for c in range(10):
        c = Carrot()
        carrot_objects.append(c)

    # Place all the carrot sprites in a container sprite
    pig_sprites = pygame.sprite.RenderPlain((pig))
    carrot_sprites = pygame.sprite.RenderPlain((carrot_objects))
    clock = pygame.time.Clock()  # created to control the game's framerate

    # main loop
    while 1:
        clock.tick(60)

        # handle events
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                return
            elif event.type == MOUSEBUTTONDOWN:
                collisions = pig.rect.collidelistall(carrot_objects)
                if len(collisions) > 0:
                    for c in collisions:
                        carrot_objects[c].eaten()
                        eating_sound.play()
                        carrot_objects[c].kill()
            elif event.type == MOUSEBUTTONUP:
                pig.uneat()

        if len(carrot_sprites) == 0:
            bg.blit(end_text, end_text_pos)

        pig_sprites.update()
        carrot_sprites.update()  # call update method on all sprites

        screen.blit(bg, bg_rect)  # calls bg image to erase everything from the last frame
        pig_sprites.draw(screen)
        carrot_sprites.draw(screen)  # draws the sprites
        pygame.display.flip()  # Makes everything visible at once


if __name__ == "__main__":
    main()
