import pygame as pg
import os


class PlaneExplosion(pg.sprite.Sprite):
    def __init__(self):
        super(PlaneExplosion, self).__init__()
        self.images = []
        for i in range(9):
            img = pg.image.load(os.path.join('assets/images/smokeparticles/PNG/Explosion/', 'explosion0' + str(i) + '.png')).convert()
            img.convert_alpha()
            img.set_colorkey((0, 0, 0))
            # scale the image down a bit.
            new_width, new_height = int(img.get_rect().width * 0.3), int(img.get_rect().height * 0.3)
            img = pg.transform.scale(img, (new_width, new_height))
            self.images.append(img)
        self.current_index = 0
        self.image = self.images[self.current_index]
        self.rect = self.image.get_rect()

    def update(self):
        self.current_index += 1
        if self.current_index >= len(self.images):
            self.current_index = 0
        self.image = self.images[self.current_index]

    def set_position(self, pos):
        """
        Sets the position of the explosion.
        :param pos: Tuple for position.
        :return:
        """
        self.rect.topleft = pos