import pygame
import math
from random import random

pygame.init()

BLACK  = ( 0x00, 0x00, 0x00 )
ORANGE = ( 0xFF, 0x8C, 0x00 )
WHITE  = ( 0xFF, 0xFF, 0xFF )
RED    = ( 0xFF, 0x00, 0x00 )

FPS            = 24
HEIGHT         = 640
WIDTH          = 640
SPEED          = 30.0
ROTATION_SPEED = 1.0
DELTA_TIME     = 1.0 / FPS
CONTACT_RADIUS = 1.0

def normalize_vector(vector, module):
    [a, b] = vector
    old_module = math.sqrt(a**2 + b**2)
    factor = module / old_module
    return [a * factor, b * factor]

players = 2
colors = [WHITE, RED, ORANGE]

rotation_keys = [
    [pygame.K_a, pygame.K_z],
    [pygame.K_m, pygame.K_k],
    [pygame.K_v, pygame.K_b]
]

positions = [
    [
        0.25 * WIDTH + random() * WIDTH * 0.5,
        0.25 * HEIGHT + random() * HEIGHT * 0.5
    ] for _ in range(players)
]

velocities = [[random(), random()] for _ in range(players)]
for i in range(players):
    velocities[i] = normalize_vector(velocities[i], SPEED)

is_alive = [True for _ in range(players)]

visited = {}

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
        angle = ROTATION_SPEED * DELTA_TIME
    elif direction == 'ANTI-CLOCKWISE':
        angle = -1 * ROTATION_SPEED * DELTA_TIME
    else:
        angle = 0.0

    return rotate_vector(velocity, angle)

def distance(p1, p2):
    [x1, y1] = p1
    [x2, y2] = p2
    return (x2 - x1)**2 + (y2 - y1)**2

def has_crashed(position, visited):
    [x, y] = position
    if x < 0 or x > WIDTH or y < 0 or y > HEIGHT:
        return True

    for vpoint in visited.keys():
        if distance(vpoint, position) < CONTACT_RADIUS:
            return True

def update_players_parameters(screen, keys, positions, velocities, visited):
    for player in range(players):
        if is_alive[player]:
            direction = None
            [cw_key, acw_key] = rotation_keys[player]

            if keys[cw_key]:
                direction = 'CLOCKWISE'
            elif keys[acw_key]:
                direction = 'ANTI-CLOCKWISE'

            old_position = positions[player]
            old_velocity = velocities[player]

            positions[player] = update_position(old_position, old_velocity)
            velocities[player] = update_velocity(old_velocity, direction)

            draw_line(screen, old_position, positions[player], colors[player])
        
            is_alive[player] = False if has_crashed(positions[player], visited) else True

    return positions, velocities, is_alive

def updated_visited(visited, positions):
    for player in range(players):
        [x, y] = positions[player]
        visited[(x,y)] = True
    return visited

while running:
    visited = updated_visited(visited, positions)

    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    positions, velocities, is_alive = update_players_parameters(screen, keys, positions, velocities, visited)

    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()
