from random import random

from geometry import normalize_vector, rotate_vector

def init_random_velocities(players, module):
    velocities = [[random() - 0.5, random() - 0.5] for _ in range(players)]
    for i in range(players):
        velocities[i] = normalize_vector(velocities[i], module)
    return velocities

def init_random_positions(width, height, players):
    return [[ 0.25 * width + random() * width * 0.5, 0.25 * height + random() * height * 0.5 ] for _ in range(players)] 

def init_actives(players):
    return [True] * players

def update_position(position, velocity, dt):
    [x, y] = position
    [vx, vy] = velocity
    return [x + dt * vx, y + dt * vy]

def update_velocity(velocity, direction, rotation_speed, dt):
    angle = rotation_speed * dt
    if not direction:
        angle *= -1
    return rotate_vector(velocity, angle)
