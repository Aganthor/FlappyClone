import pygame as pg
import os
import constants


class ScoreDisplay:
    """
    Class to show the score in the gaming window.
    """
    SCORE_NUMBER_WIDTH = 53
    SCORE_LETTER_WIDTH = 0
    SCORE_LETTER_HEIGHT = 0

    def __init__(self, max_lives):
        self.redo_score_surf = True  # Should we refresh the score_surf to reflect any score changes?
        self.redo_lives_surf = True
        self.number_dict = {}
        self.letters_dict = {}
        self.score_surf = pg.Surface((constants.SCREEN_WIDTH, constants.SCORE_SURFACE_HEIGHT))
        self.score_surf.fill((255, 255, 255))
        self.score = 10
        self.lives = max_lives
        self.lives_offset = 0
        self.load_number_sprites()
        self.load_letter_sprites()

    def render(self, screen):
        """
        Render the ScoreDisplay surface onto the main screen.
        :param screen: The main game screen surface
        :return: None
        """
        if self.redo_score_surf:
            self.score_surf.blit(self.prepare_score_surface(), (0, 0))
            self.redo_score_surf = False
        if self.redo_lives_surf:
            self.score_surf.blit(self.prepare_lives(), (self.lives_offset, 0))
            self.redo_lives_surf = False
        screen.blit(self.score_surf, (0, 0))

    def update_player_lives(self, player):
        """
        Update the internal live count. Will set redo_lives to True if lives has changed.
        :param player: The player object from which we can get the lives.
        :return:
        """
        if self.lives != player.get_lives():
            self.lives = player.get_lives()
            self.redo_lives_surf = True
        else:
            self.redo_lives_surf = False

    def prepare_lives(self):
        lives_width = (self.SCORE_NUMBER_WIDTH + ((len("LIVES") + 1) * self.SCORE_LETTER_WIDTH))
        temp_surf = pg.Surface((lives_width, constants.SCORE_SURFACE_HEIGHT))
        temp_surf.fill((255, 255, 255))
        width = 0
        # Prepare the letters first -> LIVES.
        for letter in ['L', 'I', 'V', 'E', 'S']:
            temp_surf.blit(self.letters_dict[letter], (width, (constants.SCORE_SURFACE_HEIGHT -
                                                               self.SCORE_LETTER_HEIGHT) / 2))
            width += self.letters_dict[letter].get_rect().width
        width += self.SCORE_LETTER_WIDTH
        temp_surf.blit(self.number_dict[self.lives], (width, 0))
        return temp_surf

    def update_score(self, player):
        """
        Update the internal score to display. Will set redo_score to True if score has changed.
        :param player: The player object from which we can get the score.
        :return:
        """
        if self.score != player.get_score():
            self.score = player.get_score()
            self.redo_score_surf = True
        else:
            self.redo_score_surf = False

    def prepare_score_surface(self):
        """
        Prepare a pygame surface with the proper sprite that matches the current score.
        :return: the temporary surface to blit to self.score_surf
        """
        number_as_str = str(self.score)
        score_width = ((len(number_as_str) * self.SCORE_NUMBER_WIDTH) + (len("SCORE ") * self.SCORE_LETTER_WIDTH))
        temp_surf = pg.Surface((score_width, constants.SCORE_SURFACE_HEIGHT))
        temp_surf.fill((255, 255, 255))
        width = 0
        # Prepare the letters first -> SCORE.
        for letter in ['S', 'C', 'O', 'R', 'E']:
            temp_surf.blit(self.letters_dict[letter], (width, (constants.SCORE_SURFACE_HEIGHT -
                                                               self.SCORE_LETTER_HEIGHT) / 2))
            width += self.letters_dict[letter].get_rect().width
        # Then, prepare the score.
        width += self.SCORE_LETTER_WIDTH / 2
        for ch in number_as_str:
            temp_surf.blit(self.number_dict[int(ch)], (width, 0))
            width += self.SCORE_NUMBER_WIDTH
        self.lives_offset = temp_surf.get_rect().width
        return temp_surf

    def load_number_sprites(self):
        """
        Load all the number images that we need.
        :return: None
        """
        for i in range(10):
            img = pg.image.load(os.path.join('assets/images/numbers', 'number' + str(i) + '.png')).convert()
            img.convert_alpha()
            img.set_colorkey((0, 0, 0))
            # scale the image down a bit.
            self.number_dict[i] = img

    def load_letter_sprites(self):
        """
        Load all the letter images that we need
        :return:
        """
        width = 0
        height = 0
        for letter in ['S', 'C', 'O', 'R', 'E', 'L', 'I', 'V']:
            img = pg.image.load(os.path.join('assets/images/Letters/', 'letter' + letter + '.png')).convert()
            img.convert_alpha()
            img.set_colorkey((0, 0, 0))
            # scale the image down a bit.
            new_width, new_height = int(img.get_rect().width * 0.8), int(img.get_rect().height * 0.8)
            img = pg.transform.scale(img, (new_width, new_height))
            self.letters_dict[letter] = img
            width += img.get_rect().width
            height += img.get_rect().height
        self.SCORE_LETTER_WIDTH = int(width / 8)
        self.SCORE_LETTER_HEIGHT = int(height / 8)
