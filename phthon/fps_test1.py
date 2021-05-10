"""fsp_test1.py"""

import sys
import pygame
from pygame.locals import QUIT

pygame.init()
SURFACE = pygame.display.set_mode((400,300))

def main():
    """main routine"""
    sysfont = pygame.font.SysFont(None,36)
    counter = 0
    while True:
        for event in pygame.event.get():
            pygame.quit()
            sys.exit()


        counter += 1
        SURFACE.fill((0,0,0))
        counter_image = sysfont.render\
            ("count is {}".format(counter), True, (255,255,255))
        SURFACE.blit(counter_image, (50, 50))
        pygame.display.update()


    if __name__ == '__main__':
        main()
