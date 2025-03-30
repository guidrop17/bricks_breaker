import pygame

class Player:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.moving_left = False
        self.moving_right = False
        self.speed = 1

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                self.moving_right = True
            elif event.key == pygame.K_LEFT:
                self.moving_left = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                self.moving_right = False
            elif event.key == pygame.K_LEFT:
                self.moving_left = False

    def move(self, screen_width):
        if self.moving_right and self.rect.right < screen_width:
            self.rect.x += self.speed
        if self.moving_left and self.rect.left > 0:
            self.rect.x -= self.speed