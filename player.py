import pygame as pg
import os

class Player(pg.sprite.Sprite):
    """
    Simple class to represent our little user controlled plane in the
    game.
    """
    MOVE_SPEED = 5

    def __init__(self):
        super(Player, self).__init__()
        self.images = []
        for i in range(3):
            img = pg.image.load(os.path.join('assets/images/', 'planeRed' + str(i+1) + '.png')).convert()
            img.convert_alpha()
            img.set_colorkey((0, 0, 0))
            self.images.append(img)
        self.current_index = 0
        self.image = self.images[self.current_index]
        self.rect = self.image.get_rect()


    def update(self):
        self.current_index += 1
        if self.current_index >= len(self.images):
            self.current_index = 0
        self.image = self.images[self.current_index]


    def handle_input(self, pressed_keys):
        if pressed_keys[pg.K_LEFT]:
            self.rect.move_ip(-self.MOVE_SPEED, 0)
        elif pressed_keys[pg.K_RIGHT]:
            self.rect.move_ip(self.MOVE_SPEED, 0)
        if pressed_keys[pg.K_UP]:
            self.rect.move_ip(0, -self.MOVE_SPEED)
        elif pressed_keys[pg.K_DOWN]:
            self.rect.move_ip(0, self.MOVE_SPEED)
