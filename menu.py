import pygame

from constants import BLACK, RED, GREEN, FPS, MINIMUM_PLAYERS, MAXIMUM_PLAYERS, CHARACTERS

class menu:
    def __init__(self, screen, clock, font):
        self.screen = screen
        self.clock = clock
        self.font = font

    def show_players_counter(self):
        players = 2
        running = True

        while running:
            self.screen.fill(BLACK)

            img = self.font.render('Select the number of players: Up/Down + Enter ', True, RED)
            self.screen.blit(img, (200, 350))

            img = self.font.render('Players: ', True, RED)
            self.screen.blit(img, (400, 400))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return None
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        running = False
                    elif event.key == pygame.K_UP and players < MAXIMUM_PLAYERS:
                        players += 1
                    elif event.key == pygame.K_DOWN and players > MINIMUM_PLAYERS:
                        players -= 1

            img = self.font.render(str(players), True, RED)
            self.screen.blit(img, (600, 400))

            pygame.display.flip()
            self.clock.tick(FPS)
            
        self.screen.fill(BLACK)

        return players

    def select_player_names(self, number_of_players):
        players = []
        name = ''

        while len(players) < number_of_players:
            self.screen.fill(BLACK)

            img = self.font.render(f'Please insert name of player {len(players) + 1}', True, RED)
            self.screen.blit(img, (200, 350))

            img = self.font.render(f'Player {len(players) + 1}: ', True, RED)
            self.screen.blit(img, (400, 400))

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
                    else:
                        if event.unicode in CHARACTERS:
                            name += event.unicode

            img = self.font.render(name, True, RED)
            self.screen.blit(img, (600, 400))

            pygame.display.flip()
            self.clock.tick(FPS)
            
        self.screen.fill(BLACK)

        return players

    def show_winner(self, winner):
        pygame.draw.rect(self.screen, (GREEN), (250, 300, 600, 200))
        self.screen.blit(self.font.render(f'Player {winner} won!', True, RED), (300, 380))
        
        img = self.font.render('Do you want to play again? Y/N', True, RED)
        self.screen.blit(img, (300, 420))

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

            self.clock.tick(FPS)

        self.screen.fill(BLACK)

        return answer
