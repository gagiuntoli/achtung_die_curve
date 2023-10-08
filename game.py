import pygame

from physics import \
    updated_visited, \
    init_random_velocities, \
    init_random_positions, \
    update_position, \
    update_velocity, \
    update_is_alive

from constants import \
    LINE_WIDTH, \
    FPS, \
    HEIGHT, \
    WIDTH, \
    SPEED, \
    ROTATION_SPEED, \
    DELTA_TIME, \
    ROTATION_KEYS, \
    PLAYERS_COLORS

from menu import menu

def draw_line(screen, p1, p2, color):
    pygame.draw.line(screen, color, p1, p2, LINE_WIDTH)

def compute_new_positions_and_velocities(positions, velocities, is_alive):
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

        if is_alive[player]:
            new_velocities.append(update_velocity(velocities[player], direction, ROTATION_SPEED, DELTA_TIME))
        else:
            new_velocities.append([0.0, 0.0])

    assert(len(positions) == len(new_positions))
    assert(len(velocities) == len(new_velocities))

    return new_positions, new_velocities, is_alive

def check_winner(is_alive):
    if is_alive.count(True) == 1:
        for player in range(len(is_alive)):
            if is_alive[player]:
                return player
    return None

def draw_new_paths(screen, old_positions, new_positions):
    assert(len(old_positions) == len(new_positions))

    for player in range(len(old_positions)):
        draw_line(screen, old_positions[player], new_positions[player], PLAYERS_COLORS[player])

def run_game(positions, velocities, is_alive, visited):
    while True:
        visited = updated_visited(visited, positions)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None

        new_positions, velocities, is_alive = compute_new_positions_and_velocities(positions, velocities, is_alive)

        draw_new_paths(screen, positions, new_positions)

        positions = new_positions
        is_alive = update_is_alive(positions, visited, WIDTH, HEIGHT, is_alive)

        winner = check_winner(is_alive)
        if winner != None:
            return winner

        # updates screen
        pygame.display.flip()

        clock.tick(FPS)

# Init game
pygame.init()

pygame.display.set_caption("Achtung die Curve!")

font = pygame.font.SysFont('freemono', 28)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

players = menu.show_players_counter(screen, clock, font)
if players == None:
    exit()

while True:
    positions = init_random_positions(WIDTH, HEIGHT, players)
    velocities = init_random_velocities(players, SPEED)
    is_alive = [True for _ in range(players)]

    visited = {}
    winner = run_game(positions, velocities, is_alive, visited)
    if winner == None:
        break

    if not menu.show_winner(screen, clock, winner, font):
        break

pygame.quit()
