"""
Trying to code a flappy bird clone!
1- will have 3 lives
2- procedurally generated columns
3- display (lives, score, time?)
"""
import pygame as pg
import random
from player import Player
from obstacles import Obstacles
from scoredisplay import ScoreDisplay
import constants
from game_state import GameStates
from player_dead_state import PlayerDeadState
from plane_explosion import PlaneExplosion


def main():
    screen = pg.display.set_mode(constants.SCREEN_RESOLUTION)
    pg.display.set_caption("Flappy Clone")

    # Create our plane!
    player = Player()
    player_group = pg.sprite.Group()
    player_group.add(player)

    score_display = ScoreDisplay(player.MAX_LIVES)
    player_explosion = PlaneExplosion()

    # Group creation. obstacles_group will contain every sprite in the game
    # to help with collision detection.
    obstacles_group = pg.sprite.Group()

    background = pg.image.load("assets/images/background.png").convert()
    background_box = background.get_rect()
    background_box.y += constants.SCORE_SURFACE_HEIGHT

    # Create a custom event for adding a new obstacle
    ADD_OBSTACLE = pg.USEREVENT + 1
    ADD_DOUBLE_OBSTACLES = pg.USEREVENT + 2
    pg.time.set_timer(ADD_OBSTACLE, 1000)
    pg.time.set_timer(ADD_DOUBLE_OBSTACLES, 3000)

    game_state = GameStates.GAME_RUNNING
    player_dead_state = PlayerDeadState()

    clock = pg.time.Clock()

    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    running = False
            if event.type == ADD_OBSTACLE:
                flip_a_coin = random.randint(0, 1)
                if flip_a_coin == 0:
                    obstacle = Obstacles(True)
                    obstacles_group.add(obstacle)
                else:
                    obstacle = Obstacles(False)
                    obstacles_group.add(obstacle)
            if event.type == ADD_DOUBLE_OBSTACLES:
                obstacle1 = Obstacles(True)
                obstacle2 = Obstacles(False)
                obstacles_group.add(obstacle1)
                obstacles_group.add(obstacle2)

        pressed_keys = pg.key.get_pressed()

        # Process user input.
        player.handle_input(pressed_keys)

        # PlayerDeadState should only process inputs if player is dead!
        if game_state == GameStates.PLAYER_DEAD:
            player_dead_state.handle_input(pressed_keys)
            if player_dead_state.restart_game():
                player.reset()
                player_group.add(player)
                obstacles_group.empty()
                game_state = GameStates.GAME_RUNNING

        if game_state == GameStates.PLAYER_EXPLOSION:
            player_explosion.update()

        if game_state == GameStates.GAME_RUNNING:
            # Update the game world.
            player.update()
            obstacles_group.update()
            score_display.update_score(player)

            # Collision detection...
            if pg.sprite.spritecollideany(player, obstacles_group):
                if player.player_death():
                    player.kill()
                    score_display.update_player_lives(player)
                    game_state = GameStates.PLAYER_DEAD
                else:
                    game_state = GameStates.PLAYER_EXPLOSION
                    player_explosion.set_position(player.rect.topleft)
                    score_display.update_player_lives(player)
                    player.reset_position()

        # Draw the game world
        screen.blit(background, background_box)
        obstacles_group.draw(screen)
        player_group.draw(screen)
        score_display.render(screen)
        if game_state == GameStates.PLAYER_DEAD:
            player_dead_state.render(screen)
        if game_state == GameStates.PLAYER_EXPLOSION:
            screen.blit(player_explosion.image, player_explosion.rect)

        pg.display.flip()

        clock.tick(60)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
