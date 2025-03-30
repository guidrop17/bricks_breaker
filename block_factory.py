import pygame

class BlockFactory:
    @staticmethod
    def create_blocks(columns, rows, screen_size):
        block_width = screen_size[0] / columns - 5
        block_height = 15
        blocks = []
        
        for row in range(rows):
            for col in range(columns):
                block = pygame.Rect(
                    col * (block_width + 5),
                    row * (block_height + 10),
                    block_width,
                    block_height,
                )
                blocks.append(block)
        return blocks
