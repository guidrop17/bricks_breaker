import pygame
from game_state import game_state

class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.options = ["New Game", "Score", "Quit"]
        self.selected = 0
        self.running = True
        self.surf = pygame.image.load('./assets/menu_image.png')
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        while self.running:
            self.handle_events()
            self.render()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_state.running = False
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    self.selected = (self.selected + 1) % len(self.options)
                elif event.key == pygame.K_UP:
                    self.selected = (self.selected - 1) % len(self.options)
                elif event.key == pygame.K_RETURN:
                    self.select_option()
    
    def select_option(self):
        if self.selected == 0:
            game_state.mode = "1P"
            self.running = False
        elif self.selected == 1:
            self.display_score()
            self.running = False
        elif self.selected == 2:
            self.running = False
            game_state.running = False            
    
    def display_score(self):
        font = pygame.font.Font(None, 40)
        text = font.render(f"Score Atual: {game_state.score}", True, game_state.colors["blocks"])
        self.screen.fill(game_state.colors["background"])
        self.screen.blit(text, (self.screen.get_width() // 2 - text.get_width() // 2, 300))
        pygame.display.flip()
        pygame.time.delay(2000)
    
    def render(self):
        self.screen.fill(game_state.colors["background"])
        self.screen.blit(self.surf, self.rect)
        font = pygame.font.Font(None, 40)
        for i, option in enumerate(self.options):
            color = game_state.colors["paddle"] if i == self.selected else (100, 100, 100)
            text = font.render(option, True, color)
            x = self.screen.get_width() // 2 - text.get_width() // 2
            y = 470 + i * 50
            self.screen.blit(text, (x, y))
        pygame.display.flip()