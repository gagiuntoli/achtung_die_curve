import pygame

from constants import BLACK, RED, GREEN, FPS, MINIMUM_PLAYERS, MAXIMUM_PLAYERS, CHARACTERS, MAX_NAME_LENGTH

class menu:
    def __init__(self, screen, clock, font):
        self.screen = screen
        self.clock = clock
        self.font = font

    def show_players_counter(self):
        players = 2
        while True:
            self.screen.fill(BLACK)
            self.screen.blit(self.font.render('Select the number of players: Up/Down + Enter ', True, RED), (200, 350))
            self.screen.blit(self.font.render('Players: ', True, RED), (400, 400))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return None
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        self.screen.fill(BLACK)
                        return players
                    elif event.key == pygame.K_UP and players < MAXIMUM_PLAYERS:
                        players += 1
                    elif event.key == pygame.K_DOWN and players > MINIMUM_PLAYERS:
                        players -= 1

            img = self.font.render(str(players), True, RED)
            self.screen.blit(img, (600, 400))

            pygame.display.flip()
            self.clock.tick(FPS)

    def select_player_names(self, number_of_players):
        players = []
        name = ''
        while len(players) < number_of_players:
            self.screen.fill(BLACK)
            self.screen.blit(self.font.render(f'Please insert name of player {len(players) + 1}', True, RED), (200, 350))
            self.screen.blit(self.font.render(f'Player {len(players) + 1}: ', True, RED), (400, 400))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return None
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        if name == '':
                            name = f'player_{len(players) + 1}'
                        players.append(name)
                        name = ''
                    elif event.key in [pygame.K_DELETE, pygame.K_BACKSPACE]:
                        if len(name) > 0:
                            name = name[0:-1]
                    else:
                        if len(name) < MAX_NAME_LENGTH and event.unicode in CHARACTERS:
                            name += event.unicode

            self.screen.blit(self.font.render(name, True, RED), (600, 400))

            pygame.display.flip()
            self.clock.tick(FPS)
            
        self.screen.fill(BLACK)
        return players

    def show_winner(self, winner, distance):
        pygame.draw.rect(self.screen, (GREEN), (250, 300, 600, 300))
        self.screen.blit(self.font.render(f'Player {winner} won!', True, RED), (300, 380))
        self.screen.blit(self.font.render(f'Distance: {distance:.1f}', True, RED), (300, 420))
        self.screen.blit(self.font.render('Do you want to play again? Y/N', True, RED), (300, 460))

        pygame.display.flip()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return None
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_n:
                        self.screen.fill(BLACK)
                        return False
                    elif event.key == pygame.K_y:
                        self.screen.fill(BLACK)
                        return True
