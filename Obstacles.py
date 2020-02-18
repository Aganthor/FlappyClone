import pygame as pg
import constants

class Obstacles(pg.sprite.Sprite):
    """
    Class to represent the stalagtites and stalagmites the the plane has to avoid.
    """
    MOVE_SPEED = 2

    def __init__(self, down):
        super(Obstacles, self).__init__()
        if down:
            self.image = pg.image.load("assets/images/rockGrassDown.png").convert()
            self.image.convert_alpha()
            self.image.set_colorkey((0, 0, 0))
            self.rect = pg.rect.Rect(constants.SCREEN_WIDTH - self.image.get_rect().width,
                                     0,
                                     self.image.get_rect().width,
                                     self.image.get_rect().height)
        else:
            self.image = pg.image.load("assets/images/rockGrass.png").convert()
            self.image.convert_alpha()
            self.image.set_colorkey((0, 0, 0))
            self.rect = pg.rect.Rect(constants.SCREEN_WIDTH - self.image.get_rect().width,
                                     constants.SCREEN_HEIGHT - self.image.get_rect().height,
                                     self.image.get_rect().width,
                                     self.image.get_rect().height)


    def update(self, *args):
        self.rect.move_ip(-self.MOVE_SPEED, 0)
        self.rect.move_ip(-self.MOVE_SPEED, 0)