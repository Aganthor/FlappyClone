import pygame as pg
import constants


class Obstacles(pg.sprite.Sprite):
    """
    Class to represent the stalagtites and stalagmites the the plane has to avoid.
    """
    MOVE_SPEED = 2

    def __init__(self, down):
        super(Obstacles, self).__init__()
        self.image = pg.image
        self.rect = pg.rect.Rect
        if down:
            self.load_image("assets/images/rockGrassDown.png", down)
        else:
            self.load_image("assets/images/rockGrass.png", down)

    def update(self, *args):
        self.rect.move_ip(-self.MOVE_SPEED, 0)
        self.rect.move_ip(-self.MOVE_SPEED, 0)
        if self.rect.right < 0:
            self.kill()

    def load_image(self, filename, down):
        self.image = pg.image.load(filename).convert()
        self.image.convert_alpha()
        self.image.set_colorkey((0, 0, 0))

        # scale the image down a bit so that it's possible for the plane to pass between two obstacles.
        new_width, new_height = int(self.image.get_rect().width * 0.75), int(self.image.get_rect().height * 0.75)
        self.image = pg.transform.scale(self.image, (new_width, new_height))
        if down:
            self.rect = pg.rect.Rect(constants.SCREEN_WIDTH,
                                     0 + constants.SCORE_SURFACE_HEIGHT,
                                     self.image.get_rect().width,
                                     self.image.get_rect().height)
        else:
            self.rect = pg.rect.Rect(constants.SCREEN_WIDTH,
                                     constants.SCREEN_HEIGHT + constants.SCORE_SURFACE_HEIGHT - self.image.get_rect().height,
                                     self.image.get_rect().width,
                                     self.image.get_rect().height)
