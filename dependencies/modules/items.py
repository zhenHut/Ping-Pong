import pygame
import random


"""class Items(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.item_x = int
        self.item_y = int

    def destroy(self):
        return self.kill()

         kollision mit ball
    def colision_ball(self, item_rect, bal, ball):
        if bal.colliderect(item_rect):
           return self.destroy()"""


class Shrimp(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.item_x = 500
        self.item_y = 300
        self.item_image = pygame.image.load('Shrimp.png').convert_alpha()

        # größe skalieren
        self.item_image = pygame.transform.scale(self.item_image, (50, 20))
        self.item_image = self.item_image
        self.item_rect = self.item_image.get_rect(center=[self.item_x, self.item_y])
        # Startzeit für das Wiedereinsetzen (30 Sekunden)
        self.next_respawn_time = pygame.time.get_ticks() + 30000

    def item_draw(self, screen, x, y):
        self.item_rect = self.item_image.get_rect(center=[x, y])
        screen.blit(self.item_image, self.item_rect)

    def get_item_x(self):
        return self.item_x

    def set_item_x(self, item_x):
        self.item_x = item_x

    def get_item_y(self):
        return self.item_y

    def set_item_y(self, item_y):
        self.item_y = item_y

    def get_item_rect(self):
        return self.item_rect

    def set_item_rect(self, item_rect):
        self.item_rect = item_rect

    # Item anzeige
    def item_display(self, x, y, screen, farbe):
        item_display ="Items"
        font = pygame.font.SysFont(None, 70)
        text = font.render(item_display, True, farbe.rot)
        screeni = screen.blit(text, [x, y])

    def update(self, display):
        if pygame.time.get_ticks() >= self.next_respawn_time:
            self.respawn(display)
        super().update()

    def respawn(self, display):
        self.item_x = random.randint(0, display.get_width() - self.item_rect.width)
        self.item_y = random.randint(0, display.get_height() - self.item_rect.height)
        self.item_rect.center = (self.item_x, self.item_y)
        # Startzeit für das nächste Wiedereinsetzen
        self.next_respawn_time = pygame.time.get_ticks() + 30000

    def destroy(self):
        self.kill()

        # kollision mit ball
    def colision_ball(self, item_rect, bal, display):
        if bal.colliderect(item_rect):
            self.destroy()
            self.respawn(display)
