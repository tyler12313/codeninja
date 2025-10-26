import pygame
import pygame.sprite

class Game:
    def __init__(self, name = "676767676767", screensize = (800,600)):
        print("Loading game: "+name)
        pygame.init()
        self.screensize = screensize
        displayoptions = (pygame.HWSURFACE | pygame.SCALED)

        self.display = pygame.display.set_mode(screensize, displayoptions)
        self.clock = pygame.time.Clock()

        self.sprites = pygame.sprite.Group()

        self.eventlist = []

        self.background_color = (16,64,16)

        self.exit = False
        pygame.display.set_caption(name)

    def update(self, deltaTime):
        for event in self.eventlist:
            self.processEvent(event)

    def processEvent(self, event):

        if event.type == pygame.QUIT:
            self.exit = True

    def draw(self):
        self.display.fill(self.background_color)
        self.sprites.draw(self.display)

    def run(self):
        while not self.exit:
            deltaTime = self.clock.tick(60)

            self.eventlist= pygame.event.get()
            self.update(deltaTime)
            self.draw()
            pygame.display.update()
        pygame.quit()

class Paddle(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([15,80])
        self.image.fill((0,255,0))
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y


class PongGame(Game):
    def __init__(self):
        super().__init__()
        self.player1 = Paddle(45,00)
        self.sprites.add(self.player1)


PongGame().run()


# pygame.init()

# displayoptions = (pygame.HWSURFACE | pygame.SCALED)
                  
# display = pygame.display.set_mode((800,600), displayoptions)

# clock = pygame.time.Clock()

# pygame.display.set_caption("My first pygame project")

# while True:
#     clock.tick(60)

#     display.fill((16,64,16))

#     pygame.display.update()
# pygame.quit()
