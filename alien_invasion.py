import pygame
from pygame.sprite import Group

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from ship import Ship
from button import Button
from pygame import mixer
import game_functions as gf

pygame.mixer.pre_init()
pygame.mixer.init()


sound_game = pygame.mixer.Sound('sounds/game_music.wav')


def run_game():
    # Инициализирует pygame, settings и объект экрана.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')
    # Создание кнопки Play.
    play_button = Button(ai_settings, screen, 'Play')
    # Создание экземпляров GameStats и Scoreboard.
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    # Создание корабля.
    ship = Ship(ai_settings, screen)
     # Создание группы для хранения пуль.
    bullets = Group()
    # Создание пришельца.
    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Запуск основного цикла игры.
    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship,
                            aliens, bullets)
        if stats.game_active:
            pygame.mixer.Sound.play(sound_game)
            mixer.Sound.set_volume(sound_game, 0.1)
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens,
                                bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens,
                                bullets)
        
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens,
                            bullets, play_button)
run_game()
