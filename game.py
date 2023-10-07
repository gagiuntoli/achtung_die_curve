# Importieren der Pygame-Bibliothek
import pygame

# initialisieren von pygame
pygame.init()

BLACK  = ( 0x00, 0x00, 0x00 )
ORANGE = ( 0xFF, 0x8C, 0x00 )
ROT    = ( 0xFF, 0x00, 0x00 )

FPS    = 60
HEIGHT = 640
WIDTH  = 640

screen = pygame.display.set_mode((HEIGHT, WIDTH))
clock = pygame.time.Clock()

pygame.display.set_caption("Achtung die Curve!")

running = True

# Schleife Hauptprogramm
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Spiellogik hier integrieren

    # Spielfeld/figur(en) zeichnen (davor Spielfeld löschen)

    # Fenster aktualisieren
    pygame.display.flip()

    # Refresh-Zeiten festlegen
    clock.tick(FPS)

pygame.quit()
