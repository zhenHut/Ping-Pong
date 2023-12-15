import pygame


#pygame.sprite.Sprite
class Sound:
    def __init__(self):
        #super().__init__()
        self.soundeffekte = pygame.mixer.Sound('./dependencies/assets/sounds/Explosion.wav')
        self.spielmusik = pygame.mixer.music.load('./dependencies/assets/sounds/ImYours.mp3'), pygame.mixer.music.play(-1, 0.0)
        self.lautstaerke = pygame.mixer_music.set_volume(.6)

    # getter und setter
    def set_lautstaerke(self, lautstaerke):
        self.lautstaerke = self.spielmusik.set_volume(1, 1)
        self.lautstaerke = lautstaerke

    def get_spielmusik(self):
        if self.spielmusik is True:
            self.spielmusik = (-1)
            self.lautstaerke(.6)
            return self.spielmusik

    def get_soundeffekte(self):
        play = pygame.mixer.Sound.play(self.soundeffekte)
        volum = pygame.mixer.Sound.set_volume(self.soundeffekte, .1)
        return play

    def set_soundeffekte(self, soundeffekte):
        self.soundeffekte = soundeffekte






