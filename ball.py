import pygame
from game import Game
from game_state import game_state

class Ball:
    def __init__(self, x, y, size, movement):
        self.rect = pygame.Rect(x, y, size, size)
        self.movement = movement
        self.alive = True
        
    def display_for_loser(self):
        font = pygame.font.Font(None, 30)
        shadow = font.render(f"Você Perdeu", True, (50, 50, 100))
        text = font.render(f"Você Perdeu", True, game_state.colors["text"])
        
        game_state.screen.blit(shadow, (352, 402))
        game_state.screen.blit(text, (350, 400))
    
    def move(self, player, blocks):
        if not self.alive:
            self.display_for_loser()
            pygame.display.flip()
            pygame.time.delay(3000)
            Game().run()
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
                self.movement[1] = -self.movement[1]
                break