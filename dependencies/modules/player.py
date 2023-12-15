import pygame.sprite


class Player(pygame.sprite.Sprite):
    def __init__(self, schlaegerhoehe, spielfigur_x, spielfigur_y,
                 spielfigur_bewegung):
        super().__init__()
        # Spielfigur
        self.schlaegerhoehe = schlaegerhoehe
        self.spielfigur_x = spielfigur_x
        self.spielfigur_y = spielfigur_y
        self.spielfigur_bewegung = spielfigur_bewegung
        self.spieler_item = 0
        self.spieler_punkte = 0

    def get_schlaegerhoehe(self):
        return self.schlaegerhoehe

    def set_schlaegerhoehe(self, schlaegerhoehe):
        self.schlaegerhoehe = schlaegerhoehe

    def get_spielfigur_x(self):
        return self.spielfigur_x

    def set_spielfigur_x(self, spielfigur_x):
        self.spielfigur_x = spielfigur_x

    def get_spielfigur_bewegung(self):
        return self.spielfigur_bewegung

    def set_spielfigur_bewegung(self, spielfigur_bewegung):
        self.spielfigur_bewegung = spielfigur_bewegung

    def get_spielfigur_y(self):
        return self.spielfigur_y

    def set_spielfigur_y(self, spielfigur_y):
        self.spielfigur_y = spielfigur_y

    def get_spieler_item(self):
        return self.spieler_item

    def set_spieler_item(self, spieler_item):
        self.spieler_item = spieler_item

    def get_spieler_punkte(self):
        return self.spieler_punkte

    def set_spieler_punkte(self, spieler_punkte):
        self.spieler_punkte = spieler_punkte



