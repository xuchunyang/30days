import sys
import pygame

def run_game():
    pygame.init()
    screen = pygame.display.set_mode()
    pygame.display.set_caption("12-1 蓝色天空")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill((0, 0, 255))
        pygame.display.flip()

run_game()
