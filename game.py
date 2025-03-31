import pygame
from game_state import game_state
from menu import Menu

class Game:
    def __init__(self):
        game_state.initialize_objects()
        game_state.score = 0
    
    def run(self):
        menu = Menu(game_state.screen)
        menu.run()
        
        if not game_state.running:
            pygame.quit()
            return

        while game_state.running:
            self.handle_events()
            self.update()
            self.render()
            pygame.time.delay(1)
            
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_state.running = False
                pygame.quit()
                return
            game_state.player.handle_event(event)
    
    def update(self):
        game_state.player.move(game_state.screen_size[0])
        game_state.ball.move(game_state.player, game_state.blocks)
        if not game_state.ball.movement:
            game_state.running = False
        game_state.running = not self.check_win()
    
    def render(self):
        game_state.screen.fill(game_state.colors["background"])
        pygame.draw.rect(game_state.screen, game_state.colors["paddle"], game_state.player.rect)
        pygame.draw.rect(game_state.screen, game_state.colors["ball"], game_state.ball.rect)
        for block in game_state.blocks:
            pygame.draw.rect(game_state.screen, game_state.colors["blocks"], block)
        self.display_score()
        self.developed_by()
        pygame.display.flip()
    
    def display_score(self):
        font = pygame.font.Font(None, 30)
        shadow = font.render(f"Score: {game_state.score}", True, (50, 50, 100))
        text = font.render(f"Score: {game_state.score}", True, game_state.colors["text"])
        
        game_state.screen.blit(shadow, (12, 782))
        game_state.screen.blit(text, (10, 780))
        
    def developed_by(self):
        font = pygame.font.Font(None, 20)
        text = font.render(f"Desenvolvido por: {game_state.developed_by}", True, game_state.colors["ball"])
        
        game_state.screen.blit(text, (225, 780))
        
    def check_win(self):
        return len(game_state.blocks) == 0