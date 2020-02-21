import pygame as pg
import os
import constants


class PlayerDeadState(pg.sprite.Sprite):
    def __init__(self):
        super(PlayerDeadState, self).__init__()
        self.font_game_over = pg.font.SysFont("comicsansms", 72)
        self.font_restart = pg.font.SysFont("comicsansms", 40)
        self.restart = False

    def render(self, screen):
        text = self.font_game_over.render("GAME OVER!!!", True, (255, 0, 0))
        w = constants.SCREEN_WIDTH / 2 - text.get_width() // 2
        h = constants.SCREEN_HEIGHT / 2 - text.get_height() // 2
        screen.blit(text, (w, h))
        h += text.get_height()
        text = self.font_restart.render("Press space bar to start a new game.", True, (0, 128, 0))
        w = constants.SCREEN_WIDTH / 2 - text.get_width() // 2
        screen.blit(text, (w, h))

    def handle_input(self, pressed_keys):
        if pressed_keys[pg.K_SPACE]:
            self.restart = True

    def restart_game(self):
        return self.restart