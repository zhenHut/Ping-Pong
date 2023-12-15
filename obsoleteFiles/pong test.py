from game import *
from sounds import Sound
from player import Player
from ball import Ball
from farben import Farben
from items import Shrimp
pygame.init()
sound = Sound()
farbe = Farben()
game = Game()
display = game.get_screen()

all_sprites = pygame.sprite.Group()
player_sprites = pygame.sprite.Group()  # Spieler-Sprites
ball_sprite = pygame.sprite.GroupSingle()  # Einzelner Ball-Sprite
item_sprite = pygame.sprite.GroupSingle()

ball = Ball()

player_1 = Player(220, 20, 250, 0)
player_2 = Player(220, game.get_screen_width() - (2*20), 250, 0)

item1 = Shrimp()
# test
# Spieler zur Spieler-Sprite-Gruppe hinzufügen
#player_sprites.add(player_1)
#player_sprites.add(player_2)
#ball_sprite.add(ball)
#item_sprite.add(item1)

while game.spiel_rennt:
    bewegung(player_1, player_2, ball)
    # Spiellogik hier integrieren
    # Spielfigur 1s
    spieler_bewegung(player_1, player_2, display.get_height())

    # Spielfeld löschen
    game.spielfeld_loeschen(game.screen, farbe.darkcyan)

    # Spielfeld zeichnen
    game.draw_spielfeld()
    # Ball
    bal = ball.ball_zeichnen(display, farbe.weiss)

    ball.get_ball_markierung()
    # screen.blit(item_image, item_rect)

    # bewegen unseres ball
    ball.get_ballpos_x()
    ball.get_ballpos_y()
    ball.set_bewegung_y(display.get_height())
    ball.set_bewegung_x(display.get_width())

    # Spielfiguren zeichnen
    # Spielerfigur 1
    player1 = game.spieler_zeichnen(display, player_1.spielfigur_x,
                                    player_1.spielfigur_y, player_1.schlaegerhoehe, farbe.weiss)
    # Item schriftzug
    item1.item_display(20, 10, display, farbe)

    # Spielerfigur 2
    player2 = game.spieler_zeichnen(display, player_2.spielfigur_x,
                                    player_2.spielfigur_y, player_2.schlaegerhoehe, farbe.weiss)
    # Item schriftzug
    item1.item_display(850, 10, display, farbe)
    # kollision
    colission(player1, player2, bal, sound, ball, player_1, player_2)

    # punkte
    score_zaehlen(ball.ballpos_x, game.get_screen_width(), ball.ball_d,
                  player_1.spieler_punkte, player_2.spieler_punkte, player_1, player_2, ball)
    # score anzeige
    score(None, display, player_1.get_spieler_punkte(), player_2.get_spieler_punkte())

    # item malen
    item1.item_draw(display, item1.get_item_x(), item1.get_item_y())
    # Fenster Aktualisieren
    # pygame.display.flip()   # alternativ geht auch pygame.display.update()

    update(player_1, player_2, item1, bal, item1.get_item_rect(), item_sprite,display)
    item1.colision_ball(item1.get_item_rect(), bal, display)

    # refresh zeiten festlegen
    game.clock.tick(game.fps)
pygame.quit()
