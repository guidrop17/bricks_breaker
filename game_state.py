import pygame

class GameState:
    def __init__(self):
        pygame.init()
        self.screen_size = (800, 800)
        self.screen = pygame.display.set_mode(self.screen_size)
        pygame.display.set_caption("Bricks Breaker")
        self.mode = ""

        self.colors = {
            "background": (20, 20, 40),
            "paddle": (0, 255, 180),
            "ball": (255, 0, 150),
            "blocks": (255, 200, 50),
            "text": (255, 255, 255),
        }
        
        self.developed_by = "Guilherme Nascimento RU:4524389"

        self.running = True
        self.score = 0

        self.blocks = []
        self.ball = None
        self.player = None
        
        self.size_of_ball = 15
        self.movement = [1, -1]
        self.ball_inicialize_in_x = 200
        self.ball_inicialize_in_y = 500
        
        self.width_of_player = 100
        self.height_of_player = 10
        self.player_inicialize_in_x = 350
        self.player_inicialize_in_y = 750
        
        self.columns_of_blocks = 8
        self.rows_of_blocks = 5

    def initialize_objects(self):
        from block_factory import BlockFactory
        from ball import Ball
        from player import Player

        self.blocks = BlockFactory.create_blocks(self.columns_of_blocks, self.rows_of_blocks, self.screen_size)
        self.ball = Ball(self.ball_inicialize_in_x, self.ball_inicialize_in_y, self.size_of_ball, self.movement)
        self.player = Player(self.player_inicialize_in_x, self.player_inicialize_in_y, self.width_of_player, self.height_of_player)
        
game_state = GameState()