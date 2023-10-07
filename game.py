import pygame
from physics import updated_visited, init_random_velocities, init_random_positions, update_position, update_velocity, has_crashed
from constants import GREEN, LINE_WIDTH, WHITE, RED, ORANGE, FPS, HEIGHT, WIDTH, SPEED, ROTATION_SPEED, DELTA_TIME, CONTACT_RADIUS

pygame.init()

players = 2
colors = [WHITE, RED, ORANGE]

rotation_keys = [
    [pygame.K_z, pygame.K_a],
    [pygame.K_m, pygame.K_k],
    [pygame.K_v, pygame.K_b]
]

positions = init_random_positions(WIDTH, HEIGHT, players)
velocities = init_random_velocities(players, SPEED)
is_alive = [True for _ in range(players)]

visited = {}

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

pygame.display.set_caption("Achtung die Curve!")

def draw_line(screen, p1, p2, color):
    pygame.draw.line(screen, color, p1, p2, LINE_WIDTH)

def update_players_parameters(screen, keys, positions, velocities, visited):
    for player in range(len(positions)):
        if is_alive[player]:
            direction = None
            [cw_key, acw_key] = rotation_keys[player]

            if keys[cw_key]:
                direction = 'CLOCKWISE'
            elif keys[acw_key]:
                direction = 'ANTI-CLOCKWISE'

            old_position = positions[player]
            old_velocity = velocities[player]

            positions[player] = update_position(old_position, old_velocity, DELTA_TIME)
            velocities[player] = update_velocity(old_velocity, direction, ROTATION_SPEED, DELTA_TIME)

            draw_line(screen, old_position, positions[player], colors[player])
        
            is_alive[player] = False if has_crashed(positions[player], visited, WIDTH, HEIGHT) else True

    return positions, velocities, is_alive

def check_winner(is_alive):
    if is_alive.count(True) == 1:
        for player in range(len(is_alive)):
            if is_alive[player]:
                return player
    return None

def run_game(visited, positions, velocities):
    running = True

    while running:
        visited = updated_visited(visited, positions)

        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        positions, velocities, is_alive = update_players_parameters(screen, keys, positions, velocities, visited)

        winner = check_winner(is_alive)
        if winner != None:
            print("Winner", winner)
            rect = pygame.draw.rect(screen, (GREEN), (0.25 * WIDTH, 0.4 * HEIGHT, 0.5 * WIDTH, 0.2 * HEIGHT), 2)
            font = pygame.font.SysFont('Arial', 25)
            screen.blit(font.render('Player '+ str(winner) + ' Won!', True, (255,0,0)), (0.25 * WIDTH + 0.1 * WIDTH, 0.4 * HEIGHT + 0.05 * HEIGHT))
            pygame.display.flip()
            running = False
            pygame.time.delay(3000)

        pygame.display.flip()

        clock.tick(FPS)

run_game(visited, positions, velocities)

pygame.quit()
