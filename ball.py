import pygame
from game import Game
from game_state import game_state

class Ball:
    def __init__(self, x, y, size, movement):
        self.rect = pygame.Rect(x, y, size, size)
        self.movement = movement
        self.alive = True
        
    def run_game_for_loser(self):
        while game_state.running:
            self.display_for_loser()
            pygame.display.flip()
            for event in pygame.event.get():            
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        Game().run()
                        return
        
    def display_for_loser(self):
        font = pygame.font.Font(None, 30)
        shadow = font.render(f"Você Perdeu", True, (50, 50, 100))
        text = font.render(f"Você Perdeu", True, game_state.colors["text"])
        shadow_text_for_next = font.render(f"Pressione ESC para voltar ao menu", True, (50, 50, 100))
        text_for_next = font.render(f"Pressione ESC para voltar ao menu", True, game_state.colors["text"])
        
        game_state.screen.blit(shadow, (332, 402))
        game_state.screen.blit(text, (330, 400))
        game_state.screen.blit(shadow_text_for_next, (222, 452))
        game_state.screen.blit(text_for_next, (220, 450))
    
    def move(self, player, blocks):
        if not self.alive:
            self.run_game_for_loser()
            return
        
        self.rect.x += self.movement[0]
        self.rect.y += self.movement[1]
        
        if self.rect.left <= 0 or self.rect.right >= 800:
            self.movement[0] = -self.movement[0]
            
        if self.rect.top <= 0:
            self.movement[1] = -self.movement[1]
            
        if self.rect.bottom >= 800:
            self.alive = False
            self.movement = None
            
        if self.rect.colliderect(player.rect):
            self.movement[1] = -self.movement[1]
        
        for block in blocks[:]:
            if self.rect.colliderect(block):
                blocks.remove(block)
                game_state.score += 10
                self.movement[1] = -self.movement[1]
                break