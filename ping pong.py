import pygame

from sounds import Sound
from farben import Farben
# pygame initialiesieren
pygame.init()

farbe = Farben()
sound = Sound()

# fenster größen variable
screen_width = 1000
screen_height = 600
# Anzeige Feld
#scorefield_height = 100
#scorefield_width = 1000
# Spielfeld
gamefield_image = pygame.image.load("hintergrund.jpg")
gamefield_width = 1000
gamefield_height = 500
gamefield_scaled = pygame.transform.scale(gamefield_image, (gamefield_width, gamefield_height))

# Fenster öffnen
screen = pygame.display.set_mode((screen_width, screen_height))

# Titel für Fensterkopf
screen_title = pygame.display.set_caption("Ping pong schmugi")

# solange die Variable True ist, soll das Spiel laufen
spiel_rennt = True
spielpause = False
spielpause_x = 0
spielpause_y = 0

# Bildschirm Aktualisierungen einstellen
clock = pygame.time.Clock()
# fps in variable
fps = 60

# Definieren der Variablen
ballpos_x = 30
ballpos_y = 120

bewegung_x = 6
bewegung_y = 6

# ball durchmesser
ball_d = 20
# ball markierung
ball_markierung = 0

class Items(pygame.sprite.Sprite):
    def destroy(self, spieler1_item, spieler2_item):
        # kollision mit ball
        if item_rect.colliderect(ball):
            if ball_markierung == 1:
                spieler1_item += 1
                self.kill()
                print(spieler1_item)
            if ball_markierung == 2:
                spieler2_item += 1
                self.kill()


class Shrimp(Items):
    def __init__(self):
        super().__init__()
        self.item_x = 500
        self.item_y = 300
        self.item_image = pygame.image.load('Shrimp.png').convert_alpha()

    def item_draw(self, screen, x, y):
        item_image = pygame.transform.scale(self.item_image, (50, 20))
        item_rect = item_image.get_rect(center=[x, y])
        screen.blit(item_image, item_rect)


# (center=[self.item_x, self.item_y])
item1 = Shrimp()

# item
item_image = pygame.image.load('Shrimp.png').convert_alpha()

# item position
item_x = 500
item_y = 300

#größe skalieren
item_image = pygame.transform.scale(item_image, (50, 20))
item_rect = item_image.get_rect(center=[item_x, item_y])

# Item anzeige
def item_display(x, y):
    item_display ="Items"
    font = pygame.font.SysFont(None, 70)
    text = font.render(item_display, True, farbe.rot)
    screeni = screen.blit(text, [x, y])

schlägerhöhe1 = 220
schlägerhöhe2 = 220
ballwechsel = 0

# Spielfigur 1
spielfigur_1_x = 20
spielfigur_1_y = 250
spielfigur_1_bewegung = 0
spieler1_item = 0

# Spielfigur 2
spielfigur_2_x = screen_width - (2*20)
spielfigur_2_y = 250
spielfigur_2_bewegung = 0
spieler2_item = 0

spieler1_punkte = 0
spieler2_punkte = 0


def score():
        ausgabetext = str(spieler1_punkte) + ":" + str(spieler2_punkte)
        font = pygame.font.SysFont(None, 70)
        text = font.render(ausgabetext, True, farbe.rot)
        screeni = screen.blit(text, [500, 20])


# Schleife Hauptprogramm
while spiel_rennt:
    # Überprüfen ob nutzer eine Aktion durchgeführt hat
    for event in pygame.event.get():

        # hier implentieren wir zusätzlich noch die ESC taste
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            spiel_rennt = False  # alternativ geht auch quit()

            # Tasten drücken
        if event.type == pygame.KEYDOWN:
            # spieler 1 tasten drücken
            if event.key == pygame.K_w:
                spielfigur_1_bewegung = -6
            elif event.key == pygame.K_s:
                spielfigur_1_bewegung = 6

            # spieler 2 tasten drücken
            if event.key == pygame.K_UP:
                spielfigur_2_bewegung = -6
            elif event.key == pygame.K_DOWN:
                spielfigur_2_bewegung = 6

                # Spiel pausieren
            elif event.key == pygame.K_p or spielpause is True:
                print("Spiel pausieren")

                if spielpause is True:
                    spielpause = False
                    pygame.mixer.music.unpause()
                    bewegung_x = spielpause_x
                    bewegung_y = spielpause_y

                else:
                    spielpause = True
                    pygame.mixer.music.pause()
                    spielpause_x = bewegung_x
                    spielpause_y = bewegung_y
                    bewegung_x = 0
                    bewegung_y = 0

        # zum Stoppen der Spielerbewegung, wenn Taste los gelassen wird
        if event.type == pygame.KEYUP:

            # Taste für Spieler 1
            if event.key == pygame.K_w or event.key == pygame.K_s:
                spielfigur_1_bewegung = 0

            # Taste für Spieler 2
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                spielfigur_2_bewegung = 0


    # Spiellogik hier integrieren
    # Spielfigur 1s
    if spielfigur_1_bewegung != 0:
        spielfigur_1_y += spielfigur_1_bewegung

    if spielfigur_1_y < 100:
        spielfigur_1_y = 100

    if spielfigur_1_y > screen_height - schlägerhöhe1:
        spielfigur_1_y = screen_height - schlägerhöhe1


    # Spielfigur 2
    if spielfigur_2_bewegung != 0:
        spielfigur_2_y += spielfigur_2_bewegung

    if spielfigur_2_y < 100:
        spielfigur_2_y = 100

    if spielfigur_2_y > screen_height - schlägerhöhe2:
        spielfigur_2_y = screen_height - schlägerhöhe2

    # Spielfeld löschen
    screen.fill(farbe.darkcyan)

    # Spielfeld zeichnen
    screen.blit(gamefield_scaled, (0, 100))

    # item malen
    screen.blit(item_image, item_rect)

    #itemdisplay
    item1.item_draw(screen, 40, 70)
    # Spielfeld/figuren zeichnen
    # Ball
    ball = pygame.draw.ellipse(screen, farbe.weiss, [ballpos_x, ballpos_y, ball_d, ball_d])

    # bewegen unseres Ball
    ballpos_x += bewegung_x
    ballpos_y += bewegung_y

    if ballpos_y > screen_height - ball_d or ballpos_y < 100:
        bewegung_y = (bewegung_y * -1)

    if ballpos_x > screen_width - ball_d or ballpos_x < 0:
        bewegung_x = (bewegung_x * -1)

    # Spielerfigur 1
    spieler1 = pygame.draw.rect(screen, farbe.weiss, [spielfigur_1_x, spielfigur_1_y, 20, schlägerhöhe1])

    # Spielerfigur 2
    spieler2 = pygame.draw.rect(screen, farbe.weiss, [spielfigur_2_x, spielfigur_2_y, 20, schlägerhöhe2])
    # Punkte erzielen
    if ballpos_x >= screen_width - ball_d:
        spieler1_punkte += 1

    elif ballpos_x < 0:
        spieler2_punkte += 1

    # Kollision spieler 1

    if spieler1.colliderect(ball):
        sound.get_soundeffekte()
        bewegung_x = (bewegung_x * -1)
        ballpos_x = 40
       #ballwechsel += 1
        schlägerhöhe1 -= 5
        ball_markierung = 1

    # Kollision spieler 2
    if spieler2.colliderect(ball):
        sound.get_soundeffekte()
        bewegung_x = (bewegung_x * -1)
        ballpos_x = 940
        #ballwechsel += 1
        schlägerhöhe2 -= 5
        ball_markierung = 2

    # kollision mit ball
    if item_rect.colliderect(ball):
        if ball_markierung == 1:
            spieler1_item += 1
            item1.kill()
            print(spieler1_item)
        if ball_markierung == 2:
            spieler2_item += 1

    # textausgabe
    # spielergebnis
    score()
    item_display(20, 10)
    item_display(850, 10)
    item1.kill()
    # Fenster Aktualisieren
    # pygame.display.flip()   # alternativ geht auch pygame.display.update()
    pygame.display.update()

    # refresh zeiten festlegen
    clock.tick(fps)

pygame.quit()

