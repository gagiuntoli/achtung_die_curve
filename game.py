# Importieren der Pygame-Bibliothek
import pygame
import math

# initialisieren von pygame
pygame.init()

BLACK  = ( 0x00, 0x00, 0x00 )
ORANGE = ( 0xFF, 0x8C, 0x00 )
WHITE  = ( 0xFF, 0xFF, 0xFF )
RED    = ( 0xFF, 0x00, 0x00 )

FPS        = 10
HEIGHT     = 640
WIDTH      = 640
SPEED      = 1.0
ROTATION_SPEED  = 1.0
DELTA_TIME = 1.0 / SPEED

# initial positions for every participant
position = [10.0, 10.0]

# initial velocities for every participant (they should be all the time being normalize by SPEED)
velocity = [1.0, 1.0]

screen = pygame.display.set_mode((HEIGHT, WIDTH))
clock = pygame.time.Clock()

pygame.display.set_caption("Achtung die Curve!")

running = True

def draw_line(screen, p1, p2, color):
    pygame.draw.line(screen, color, p1, p2, 5)

def update_position(position, velocity):
    [x, y] = position
    [vx, vy] = velocity
    return [x + DELTA_TIME * vx, y + DELTA_TIME * vy]

def rotate_vector(vector, angle):
    [x_old, y_old] = vector
    x = x_old * math.cos(angle) - y_old * math.sin(angle)
    y = x_old * math.sin(angle) + y_old * math.cos(angle)
    return [x, y]
    

def update_velocity(velocity, direction):
    if direction == 'CLOCKWISE':
        angle = 0.1
        return rotate_vector(velocity, angle)
    elif direction == 'ANTI-CLOCKWISE':
        angle = -0.1
        return rotate_vector(velocity, angle)
    else:
        return velocity

# Schleife Hauptprogramm
while running:
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    print("a", keys[pygame.K_a], "z", keys[pygame.K_z])

    # Spiellogik hier integrieren

    direction = None
    if keys[pygame.K_a]:
        direction = 'CLOCKWISE'
    elif keys[pygame.K_z]:
        direction = 'ANTI-CLOCKWISE'

    old_position = position
    position = update_position(position, velocity)
    velocity = update_velocity(velocity, direction)

    # Spielfeld/figur(en) zeichnen (davor Spielfeld löschen)

    # Fenster aktualisieren

    # Draw on the screen a green line from (0, 0) to (50, 30)
    # 5 pixels wide. Uses (r, g, b) color - medium sea green.
    draw_line(screen, old_position, position, WHITE)

    pygame.display.flip()

    # Refresh-Zeiten festlegen
    clock.tick(FPS)

pygame.quit()
