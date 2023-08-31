import pygame


class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Definieren der Variablen
        self.ballpos_x = 20
        self.ballpos_y = 120
        # Ball Bewegung
        self.bewegung_x = 6
        self.bewegung_y = 6

        # ball durchmesser
        self.ball_d = 20
        # ball markierung
        self.ball_markierung = 0

    # getter und setter

    def get_ballpos_x(self):
        self.ballpos_x += self.bewegung_x
        return self.ballpos_x

    def set_ballpos_x(self, ballpos_x):
        self.ballpos_x = ballpos_x

    def get_ballpos_y(self):
        self.ballpos_y += self.bewegung_y
        return self.ballpos_y

    def set_ballpos_y(self, ballpos_y):
        self.ballpos_y = ballpos_y

    def get_bewegung_x(self):
        return self.bewegung_x

    def set_bewegung_x(self, game_width):
        if self.ballpos_x > game_width - self.ball_d or self.ballpos_x < 0:
            self.bewegung_x = (self.bewegung_x * -1)

    def get_bewegung_y(self):
        return self.bewegung_y

    def set_bewegung_y(self, game_height):
        if self.ballpos_y > game_height - self.ball_d or self.ballpos_y < 100:
            self.bewegung_y = (self.bewegung_y * -1)

    def get_ball_d(self):
        return self.ball_d

    def set_ball_d(self, ball_d):
        self.ball_d = ball_d

    def get_ball_markierung(self):
        return self.ball_markierung

    def set_ball_markierung(self, ball_markierung):
        self.ball_markierung = ball_markierung

    #def update(self):
        #self.update()

    def ball_zeichnen(self, screen, farbe):
        ball_zeichnen = pygame.draw.ellipse(screen, farbe, [self.ballpos_x, self.ballpos_y, self.ball_d, self.ball_d])
        return ball_zeichnen

    """def destroy(self, gamefieldhoehe):
        if self.ballpos_x is 0 or gamefieldhoehe:
            self.kill()"""
