import pygame as pg
import os
import constants


class ScoreDisplay:
    """
    Class to show the score in the gaming window.
    """
    SCORE_NUMBER_WIDTH = 53

    def __init__(self):
        self.number_dict = {}
        self.letters_dict = {}
        self.score_surf = pg.Surface((constants.SCREEN_WIDTH, constants.SCORE_SURFACE_HEIGHT))
        self.score_surf.fill((255, 255, 255))
        self.score = 10
        self.load_number_sprites()
        self.load_letter_sprites()

    def render(self, screen):
        """
        Render the ScoreDisplay surface onto the main screen.
        :param screen: The main game screen surface
        :return: None
        """
        self.score_surf.blit(self.prepare_score_surface(), (0, 0))
        screen.blit(self.score_surf, (0, 0))

    def update_score(self, player):
        """
        Update the internal score to display.
        :param player: The player object from which we can get the score.
        :return:
        """
        self.score += player.get_score()
        #print(f"Player score is {self.score}")

    def prepare_score_surface(self):
        """
        Prepare a pygame surface with the proper sprite that matched current score.
        :return: the temporary surface to blit to self.score_surf
        """
        number_as_str = str(self.score)
        temp_surf = pg.Surface((len(number_as_str) * self.SCORE_NUMBER_WIDTH, constants.SCORE_SURFACE_HEIGHT))
        temp_surf.fill((255, 255, 255))
        width = 0
        for ch in number_as_str:
            temp_surf.blit(self.number_dict[int(ch)], (width, 0))
            width += self.SCORE_NUMBER_WIDTH
        return temp_surf

    def load_number_sprites(self):
        """
        Loads the number sprites and add each as a surface in the dictionnary.
        :return: None
        """
        for i in range(10):
            img = pg.image.load(os.path.join('assets/images/numbers', 'number' + str(i) + '.png')).convert()
            img.convert_alpha()
            img.set_colorkey((0, 0, 0))
            # scale the image down a bit.
            #new_width, new_height = int(img.get_rect().width * 0.5), int(img.get_rect().height * 0.5)
            self.number_dict[i] = img#pg.transform.scale(img, (new_width, new_height))

    def load_letter_sprites(self):
        # for letter in ['S', 'C']
        # self.letters_dict['S'] = pg.image.load(os.path.join('assets/images/letters/', 'letterS.png')).convert()
        # self.letters_dict['C'] = pg.image.load(os.path.join('assets/images/letters/', 'letterC.png')).convert()
        # self.letters_dict['O'] = pg.image.load(os.path.join('assets/images/letters/', 'letterO.png')).convert()
        # self.letters_dict['R'] = pg.image.load(os.path.join('assets/images/letters/', 'letterR.png')).convert()
        # self.letters_dict['E'] = pg.image.load(os.path.join('assets/images/letters/', 'letterE.png')).convert()
        # self.letters_dict['L'] = pg.image.load(os.path.join('assets/images/letters/', 'letterL.png')).convert()
        # self.letters_dict['I'] = pg.image.load(os.path.join('assets/images/letters/', 'letterI.png')).convert()
        # self.letters_dict['V'] = pg.image.load(os.path.join('assets/images/letters/', 'letterV.png')).convert()
        pass