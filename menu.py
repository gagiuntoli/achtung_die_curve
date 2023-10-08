import pygame

from constants import WHITE, BLACK, RED, FPS, MINIMUM_PLAYERS, MAXIMUM_PLAYERS

class menu:

    def show_players_counter(screen, clock):
        font = pygame.font.SysFont('freemono', 28)
        img = font.render('Players', True, RED)
        screen.blit(img, (20, 20))

        players = 2
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return None
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        running = False
                    elif event.key == pygame.K_UP and players < MAXIMUM_PLAYERS:
                        players += 1
                    elif event.key == pygame.K_DOWN and players > MINIMUM_PLAYERS:
                        players -= 1

            pygame.draw.rect(screen, (WHITE), (150, 20, 30, 30))

            img = font.render(str(players), True, RED)
            screen.blit(img, (160, 20))

            pygame.display.flip()
            clock.tick(FPS)
            
        screen.fill(BLACK)

        return players

    def ask_for_continuation(screen, clock):
        screen.fill(BLACK)

        font = pygame.font.SysFont('freemono', 28)
        img = font.render('Do you want to play again? Y/N', True, RED)
        screen.blit(img, (20, 20))

        pygame.display.flip()

        running = True
        answer = False

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_n:
                        answer = False
                        running = False
                    elif event.key == pygame.K_y:
                        answer = True
                        running = False
            clock.tick(FPS)

        screen.fill(BLACK)

        return answer