import sys

import pygame

from duck import Duck


def run_game():
    pygame.init()
    screen = pygame.display.set_mode()
    pygame.display.set_caption("12-2 游戏角色")
    duck = Duck(screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill([0, 206, 255])
        duck.blitme()

        # 让最近绘制的屏幕可见
        pygame.display.flip()


run_game()
