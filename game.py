import pygame
from farben import Farben
farbe = Farben()


class Game:
    def __init__(self):
        # solange die Variable True ist, soll das Spiel laufen
        self.spiel_rennt = True
        self.spielpause = False
        self.spielpause_x = 0
        self.spielpause_y = 0

        # fenster größen variable
        self.screen_width = 1000
        self.screen_height = 600

        # Anzeige Feld
        self.scorefield_height = 100
        self.scorefield_width = 1000

        # Spielfeld
        self.gamefield_image = pygame.image.load("hintergrund.jpg")
        self.gamefield_width = 1000
        self.gamefield_height = 500
        self.gamefield_scaled = pygame.transform.scale(self.gamefield_image,
                                                (self.gamefield_width, self.gamefield_height))

        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        # Titel für Fensterkopf
        self.screen_title = pygame.display.set_caption("Ping pong schmugi")

        # Bildschirm Aktualisierungen einstellen
        self.clock = pygame.time.Clock()
        # fps in variable
        self.fps = 60

    def get_spielpause(self):
        return self.spielpause

    def set_spielpause(self, spielpaus):
        self.spielpause = spielpaus

    def get_screen_width(self):
        return self.screen_width

    def get_screen_height(self):
        return self.screen_height

    #def set_screen(self, screen):
        #self.screen = screen

    def get_screen(self):
        # Fenster öffnen
        return self.screen

    @staticmethod
    def spielfeld_loeschen(screen, farbe):
        # Spielfeld löschen
        return screen.fill(farbe)

    def draw_spielfeld(self):
        # Spielfeld zeichnen
        gamefield = self.screen.blit(self.gamefield_scaled, (0, 100))
        return gamefield

    def spieler_zeichnen(self, screen, player_x, player_y, schlaegerhoehe, color):
        spieler_zeichnen = pygame.draw.rect(screen, color,
                                            [player_x, player_y, 20, schlaegerhoehe])
        return spieler_zeichnen


def colission(player1zeichnung, player2zeichnung, ballzeichnung,
              sound, ball, player1, player2):
    # Kollision spieler 1
    if player1zeichnung.colliderect(ballzeichnung):
        sound.get_soundeffekte()
        ball.bewegung_x = (ball.bewegung_x * -1)
        ball.ballpos_x = 40
        # ballwechsel += 1
        player1.schlaegerhoehe -= 5
        ball_markierung = 1
        ball.set_ball_markierung(ball_markierung)
        print(ball.ball_markierung)

    # Kollision spieler 2
    if player2zeichnung.colliderect(ballzeichnung):
        sound.get_soundeffekte()
        ball.bewegung_x = (ball.bewegung_x * -1)
        ball.ballpos_x = 940
        # ballwechsel += 1
        player2.schlaegerhoehe -= 5
        ball_markierung =2
        ball.set_ball_markierung(ball_markierung)
        print(ball.ball_markierung)



def score(bob, screen,  player1, player2):
    # spielergebnis
    ausgabetext = str(player1) + ":" + str(player2)
    font = pygame.font.SysFont(bob, 70)
    text = font.render(ausgabetext, True, farbe.rot)
    scor = screen.blit(text, [500, 20])


def restart(player1, player2, game, ball):
    player1.schlaegerhoehe = 220
    player1.spielfigur_x = 20
    player1.spielfigur_y = 250
    player1.spielfigur_bewegung = 0

    player2.schlaegerhoehe = 220
    player2.spielfigur_x = game - (2*20)
    player2.spielfigur_y = 250
    player2.spielfigur_bewegung = 0

    ball.set_ballpos_x(500)
    ball.set_ballpos_y(300)


def score_zaehlen(ballpos_x, screen_width, ball_d, spieler1_punkte,
                  spieler2_punkte, player_1, player_2, ball):
    if ballpos_x > screen_width - ball_d:
        restart(player_1, player_2, screen_width, ball)
        spieler1_punkte += 1
        player_1.set_spieler_punkte(spieler1_punkte)

    elif ballpos_x <= 0:
        spieler2_punkte += 1
        player_2.set_spieler_punkte(spieler2_punkte)
        restart(player_1, player_2, screen_width, ball)


def update(player1, player2, item, bal, item_rect, item_sprite, display):
    pygame.display.update()
    # spielpause()
    player1.update()
    player2.update()
    if item.colision_ball(item_rect, bal, display):
        item.kill()
        item_sprite.remove(item)
        item.update()




def spielpause(event, ball):
    # Spiel pausieren

    # for event in pygame.event.get():
        if event.key == pygame.K_p or Game().get_spielpause() is True:
            return print("Spiel pausieren")

        if Game().get_spielpause() is True:
            Game.set_spielpause = False
            print(Game().get_spielpause)
            pygame.mixer.music.unpause()
            ball.bewegung_x = Game().spielpause_x
            ball.bewegung_y = Game().spielpause_y

        else:
            Game.spielpause = True
            pygame.mixer.music.pause()
            Game.spielpause_x = ball.bewegung_x
            Game.spielpause_y = ball.bewegung_y
            ball.bewegung_x = 0
            ball.bewegung_y = 0


def bewegung(player1, player2, ball):
    # Überprüfen ob nutzer eine Aktion durchgeführt hat
    for event in pygame.event.get():
        # hier implentieren wir zusätzlich noch die ESC taste
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and\
                event.key == pygame.K_ESCAPE:
            Game.spiel_rennt = False
            return quit()
        # Tasten drücken
        if event.type == pygame.KEYDOWN:
            # spieler 1 tasten drücken
            if event.key == pygame.K_w:
                player1.spielfigur_bewegung -= 6
                return player1.spielfigur_bewegung

            elif event.key == pygame.K_s:
                player1.spielfigur_bewegung = 6
                return player1.spielfigur_bewegung

            # spieler 2 tasten drücken
            if event.key == pygame.K_UP:
                player2.spielfigur_bewegung = -6
                return player2.spielfigur_bewegung

            elif event.key == pygame.K_DOWN:
                player2.spielfigur_bewegung = 6
                return player2.spielfigur_bewegung

            spielpause(event, ball)
        # zum Stoppen der Spielerbewegung, wenn Taste los gelassen wird
        if event.type == pygame.KEYUP:
            # Taste für Spieler 1
            if event.key == pygame.K_w or event.key == pygame.K_s:
                player1.spielfigur_bewegung = 0

            # Taste für Spieler 2
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                player2.spielfigur_bewegung = 0


def spieler_bewegung(player1, player2, screen_height):
    # Spiellogik hier integrieren
    # Spielfigur 1
    if player1.spielfigur_bewegung != 0:
        player1.spielfigur_y += player1.spielfigur_bewegung

    if player1.spielfigur_y < 100:
        player1.spielfigur_y = 100

    if player1.spielfigur_y > screen_height - player1.schlaegerhoehe:
        player1.spielfigur_y = screen_height - player1.schlaegerhoehe

    # Spielfigur 2
    if player2.spielfigur_bewegung != 0:
        player2.spielfigur_y += player2.get_spielfigur_bewegung()

    if player2.spielfigur_y < 100:
        player2.spielfigur_y = 100

    if player2.spielfigur_y > screen_height - player2.schlaegerhoehe:
        player2.spielfigur_y = screen_height - player2.schlaegerhoehe
