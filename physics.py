import math
from random import random

def normalize_vector(vector, module):
    [a, b] = vector
    old_module = math.sqrt(a**2 + b**2)
    factor = module / old_module
    return [a * factor, b * factor]

def init_random_velocities(players, module):
    velocities = [[random() - 0.5, random() - 0.5] for _ in range(players)]
    for i in range(players):
        velocities[i] = normalize_vector(velocities[i], module)
    return velocities

def init_random_positions(width, height, players):
    return [
        [
            0.25 * width + random() * width * 0.5,
            0.25 * height + random() * height * 0.5
        ] for _ in range(players)
    ]

def init_actives(players):
    return [True for _ in range(players)]

def update_position(position, velocity, dt):
    [x, y] = position
    [vx, vy] = velocity
    return [x + dt * vx, y + dt * vy]

def rotate_vector(vector, angle):
    [x_old, y_old] = vector
    x = x_old * math.cos(angle) - y_old * math.sin(angle)
    y = x_old * math.sin(angle) + y_old * math.cos(angle)
    return [x, y]
    
def update_velocity(velocity, direction, rotation_speed, dt):
    if direction == 'CLOCKWISE':
        angle = rotation_speed * dt
    elif direction == 'ANTI-CLOCKWISE':
        angle = -1 * rotation_speed * dt
    else:
        angle = 0.0
    return rotate_vector(velocity, angle)
