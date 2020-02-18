import pygame as pg
import random
from player import Player
from Obstacles import Obstacles
import constants


def main():
    screen = pg.display.set_mode(constants.SCREEN_RESOLUTION)
    pg.display.set_caption("Flappy Clone")

    # Create our plane!
    player = Player()
    player_group = pg.sprite.Group()
    player_group.add(player)

    # Group creation. obstacles_group will contain every sprite in the game
    # to help with collision detection.
    obstacles_group = pg.sprite.Group()

    background = pg.image.load("assets/images/background.png").convert()
    background_box = background.get_rect()

    # Create a custom event for adding a new obstacle
    ADD_OBSTACLES = pg.USEREVENT + 1
    pg.time.set_timer(ADD_OBSTACLES, 1000)

    clock = pg.time.Clock()

    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    running = False
            if event.type == ADD_OBSTACLES:
                flip_a_coin = random.randint(0, 1)
                if flip_a_coin == 0:
                    obstacle = Obstacles(True)
                    obstacles_group.add(obstacle)
                else:
                    obstacle = Obstacles(False)
                    obstacles_group.add(obstacle)

        pressed_keys = pg.key.get_pressed()

        # Process user input.
        player.handle_input(pressed_keys)

        # Update the game world.
        player.update()
        obstacles_group.update()

        # Collision detection...
        if pg.sprite.spritecollideany(player, obstacles_group):
            player.kill()

        # Draw the game world
        screen.blit(background, background_box)
        obstacles_group.draw(screen)
        player_group.draw(screen)

        pg.display.flip()

        clock.tick(60)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
