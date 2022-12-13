from pygame import mixer

class Mixer:
    """Класс для звуков и музыки."""

    def __init__(self, ai_game):
        """Инициализация настроек и загрузка ресурсов."""
        self.settings = ai_game.settings
        self.laser_shot = mixer.Sound('sound/laser_shot.wav')
        self.alien_crashed = mixer.Sound('sound/alien_crashed.wav')
        self.game_over = mixer.Sound('sound/game_over.wav')

    def play_music(self):
        """Starts to play background music."""
        if self.settings.sound_on:
            mixer.music.load('sound/game_music.wav')
            mixer.music.set_volume(self.settings.music_volume)
            # играет, до тех пор, пока не выключишь
            mixer.music.play(-1)