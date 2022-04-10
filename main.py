import pygame, sys



WIDTH, HEIGHT = 1080, 720
FPS = 10
pygame.display.set_caption("Wizard Jump")
background_color = pygame.Color('white')
CHAR_WIDTH, CHAR_HEIGHT = 75, 75

class Player(pygame.sprite.Sprite):

    def __init__(self):
        super(Player, self).__init__()

        self.sprites = []
        self.sprites.append(pygame.transform.scale(running1, (CHAR_WIDTH, CHAR_HEIGHT)))
        self.sprites.append(pygame.transform.scale(running2, (CHAR_WIDTH, CHAR_HEIGHT)))
        self.sprites.append(pygame.transform.scale(running3, (CHAR_WIDTH, CHAR_HEIGHT)))
        self.sprites.append(pygame.transform.scale(running4, (CHAR_WIDTH, CHAR_HEIGHT)))
        self.sprites.append(pygame.transform.scale(running5, (CHAR_WIDTH, CHAR_HEIGHT)))
        self.sprites.append(pygame.transform.scale(running6, (CHAR_WIDTH, CHAR_HEIGHT)))
        self.sprites.append(pygame.transform.scale(running7, (CHAR_WIDTH, CHAR_HEIGHT)))
        self.sprites.append(pygame.transform.scale(running8, (CHAR_WIDTH, CHAR_HEIGHT)))
        
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = pygame.Rect(175, 600, 75, 75)
    
    def update(self):
        self.current_sprite += 1

        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0

        self.image = self.sprites[self.current_sprite]

    # Main function of the game
def main():
    pygame.init()
    WIN = pygame.display.set_mode((WIDTH,HEIGHT))
    player = Player()
    moving_sprites = pygame.sprite.Group(player)
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        moving_sprites.update()
        WIN.fill(background_color)
        moving_sprites.draw(WIN)
        pygame.display.update()
        clock.tick(FPS)


if __name__ == "__main__":
    main()