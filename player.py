import pygame as pg
import os
import constants


class Player(pg.sprite.Sprite):
    """
    Simple class to represent our little user controlled plane in the
    game.
    """
    MOVE_SPEED = 5
    MAX_LIVES = 3

    def __init__(self):
        super(Player, self).__init__()
        self.number_of_lives = self.MAX_LIVES
        self.images = []
        for i in range(3):
            img = pg.image.load(os.path.join('assets/images/', 'planeRed' + str(i + 1) + '.png')).convert()
            img.convert_alpha()
            img.set_colorkey((0, 0, 0))
            self.images.append(img)
        self.current_index = 0
        self.image = self.images[self.current_index]
        self.rect = self.image.get_rect()
        self.rect.topleft = (0, (constants.SCREEN_HEIGHT + constants.SCORE_SURFACE_HEIGHT) // 2)
        self.score = 0

    def update(self):
        self.current_index += 1
        if self.current_index >= len(self.images):
            self.current_index = 0
        self.image = self.images[self.current_index]
        if self.rect.top < constants.SCORE_SURFACE_HEIGHT:  # Can't go in the score display surface.
            self.rect.top = constants.SCORE_SURFACE_HEIGHT
        if self.rect.bottom >= constants.SCREEN_HEIGHT:  # Clip so that the plane can't go below the max...
            self.rect.bottom = constants.SCREEN_HEIGHT

    def handle_input(self, pressed_keys):
        if pressed_keys[pg.K_LEFT]:
            self.rect.move_ip(-self.MOVE_SPEED, 0)
        elif pressed_keys[pg.K_RIGHT]:
            self.rect.move_ip(self.MOVE_SPEED, 0)
        elif pressed_keys[pg.K_UP]:
            self.rect.move_ip(0, -self.MOVE_SPEED)
        elif pressed_keys[pg.K_DOWN]:
            self.rect.move_ip(0, self.MOVE_SPEED)
        if pressed_keys[pg.K_s]:
            self.score += 10

    def get_score(self):
        return self.score

    def get_lives(self):
        return self.number_of_lives

    def reset(self):
        self.number_of_lives = self.MAX_LIVES
        self.score = 0
        self.rect.topleft = (0, (constants.SCREEN_HEIGHT + constants.SCORE_SURFACE_HEIGHT) // 2)

    def player_death(self):
        self.number_of_lives -= 1
        if self.number_of_lives < 1:
            return True
        else:
            return False

    def reset_position(self):
        self.rect.topleft = (0, (constants.SCREEN_HEIGHT + constants.SCORE_SURFACE_HEIGHT) // 2)
