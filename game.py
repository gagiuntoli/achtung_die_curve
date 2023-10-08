import pygame

from physics import \
    updated_visited, \
    init_random_velocities, \
    init_random_positions, \
    update_position, \
    update_velocity, \
    update_actives

from constants import \
    LINE_WIDTH, \
    FPS, \
    HEIGHT, \
    WIDTH, \
    SPEED, \
    ROTATION_SPEED, \
    DELTA_TIME, \
    ROTATION_KEYS, \
    PLAYERS_COLORS, \
    CONTACT_RADIUS

from menu import menu

def draw_line(screen, p1, p2, color):
    pygame.draw.line(screen, color, p1, p2, LINE_WIDTH)

def compute_new_positions_and_velocities(positions, velocities, actives):
    keys = pygame.key.get_pressed()

    new_positions = []
    new_velocities = []

    for player in range(len(positions)):
        direction = None
        [cw_key, acw_key] = ROTATION_KEYS[player]

        if keys[cw_key]:
            direction = 'CLOCKWISE'
        elif keys[acw_key]:
            direction = 'ANTI-CLOCKWISE'
        
        new_positions.append(update_position(positions[player], velocities[player], DELTA_TIME))

        if actives[player]:
            new_velocities.append(update_velocity(velocities[player], direction, ROTATION_SPEED, DELTA_TIME))
        else:
            new_velocities.append([0.0, 0.0])

    assert(len(positions) == len(new_positions))
    assert(len(velocities) == len(new_velocities))

    return new_positions, new_velocities, actives

def check_winner(actives):
    if actives.count(True) == 1:
        for player in range(len(actives)):
            if actives[player]:
                return player
    return None

def draw_new_paths(screen, old_positions, new_positions):
    assert(len(old_positions) == len(new_positions))

    for player in range(len(old_positions)):
        draw_line(screen, old_positions[player], new_positions[player], PLAYERS_COLORS[player])

def run_game(positions, velocities, actives, visited):
    while True:
        visited = updated_visited(visited, positions)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None

        new_positions, velocities, actives = compute_new_positions_and_velocities(positions, velocities, actives)

        draw_new_paths(screen, positions, new_positions)

        positions = new_positions
        actives = update_actives(positions, visited, CONTACT_RADIUS, WIDTH, HEIGHT, actives)

        winner = check_winner(actives)
        if winner != None:
            return winner

        # updates screen
        pygame.display.flip()

        clock.tick(FPS)

# Init game
pygame.init()

pygame.display.set_caption("Achtung die Curve!")

font = pygame.font.SysFont('freemono', size=28, bold=True)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

players = menu.show_players_counter(screen, clock, font)
if players == None:
    exit()

while True:
    positions = init_random_positions(WIDTH, HEIGHT, players)
    velocities = init_random_velocities(players, SPEED)
    actives = [True for _ in range(players)]

    visited = {}
    winner = run_game(positions, velocities, actives, visited)
    if winner == None:
        break

    if not menu.show_winner(screen, clock, winner, font):
        break

pygame.quit()
