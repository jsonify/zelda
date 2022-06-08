import pygame
from settings import *


class Weapon(pygame.sprite.Sprite):
    def __init__(self, player, groups):
        super().__init__(groups)
        direction = player.status.split("_")[0]

        # graphic
        full_path = f"../graphics/weapons/{player.weapon}/{direction}.png"
        self.image = pygame.image.load(full_path).convert_alpha()

        # placement
        vertical_offset = pygame.math.Vector2(0, 16)
        horizontal_offset = pygame.math.Vector2(-10, 0)
        if direction == "right":
            self.rect = self.image.get_rect(
                midleft=player.rect.midright + vertical_offset
            )
        elif direction == "left":
            self.rect = self.image.get_rect(
                midright=player.rect.midleft + vertical_offset
            )
        elif direction == "up":
            self.rect = self.image.get_rect(
                midbottom=player.rect.midtop + horizontal_offset
            )
        elif direction == "down":
            self.rect = self.image.get_rect(
                midtop=player.rect.midbottom + horizontal_offset
            )
