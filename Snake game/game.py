import pygame
import sys
from config import Config
from apple import Apple
from snake import Snake

class Game():
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((Config.WINDOW_WIDTH,Config.WINDOW_HEIGHT))
        self.BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
        self.OVER = pygame.font.Font('freesansbold.ttf', 54)
        self.apple = Apple()
        self.snake = Snake()
        self.Check = "GameisON"


    def drawlines(self):
        for x in range(0,Config.WINDOW_WIDTH,Config.CELLSIZE):
            pygame.draw.line(self.screen,Config.DARKGRAY,(x,0),(x,Config.WINDOW_HEIGHT))
        for y in range(0,Config.WINDOW_HEIGHT,Config.CELLSIZE):
            pygame.draw.line(self.screen,Config.DARKGRAY,(0,y),(Config.WINDOW_WIDTH,y))

    def run(self):
        self.StartString()
        while True:
            if self.Check == "GameisOFF":
                self.pressforkey()
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    pygame.quit()
                if e.type == pygame.KEYDOWN:
                    self.draw()
                    pygame.display.update()
                    self.loop()


    def drawApple(self):
        x = self.apple.x * Config.CELLSIZE
        y = self.apple.y * Config.CELLSIZE
        applerect = pygame.Rect(x,y,Config.CELLSIZE,Config.CELLSIZE)
        pygame.draw.rect(self.screen,Config.RED, applerect)

    def drawScore(self,score):
        scoreSurf = self.BASICFONT.render('Score: %s' % (score), True, Config.WHITE)
        scoreRect = scoreSurf.get_rect()
        scoreRect.topleft = (Config.WINDOW_WIDTH -120, 10)
        self.screen.blit(scoreSurf,scoreRect)


    def drawSnake(self):
        for a in self.snake.wormCoords:
            x= a['x'] * Config.CELLSIZE
            y = a['y'] * Config.CELLSIZE
            snakerect = pygame.Rect(x,y,Config.CELLSIZE,Config.CELLSIZE)
            pygame.draw.rect(self.screen,Config.DARKGREEN,snakerect)
            Innersnakerect = pygame.Rect(x+4,y+4,Config.CELLSIZE-8,Config.CELLSIZE-8)
            pygame.draw.rect(self.screen,Config.GREEN,Innersnakerect)

    def String(self):
        Strin = self.OVER.render('Game Over' , True, Config.WHITE)
        self.screen.blit(Strin,(200,200))

    def StartString(self):
        Strin1 = self.OVER.render('To Start the Game' , True, Config.WHITE)
        self.screen.blit(Strin1,(100,200))
    # To Rotate the String    rotatedSurf2 = pygame.transform.rotate(Strin1,10-degres)
        Strin2 = self.BASICFONT.render('"Press Any Key"' , True, Config.WHITE)
        self.screen.blit(Strin2,(250,280))
        pygame.display.update()


    def gameover(self):

        if (self.snake.wormCoords[0]['x'] >= Config.CELLWIDTH or
            self.snake.wormCoords[0]['x'] <= -1 or
            self.snake.wormCoords[0]['y'] <= -1 or
            self.snake.wormCoords[0]['y'] >= Config.CELLHEIGHT ):
            self.screen.fill(Config.BG_COLOR)
            self.String()
            self.Check = "GameisOFF"

        for worm in self.snake.wormCoords[1:]:
            if (worm['x'] == self.snake.wormCoords[0]['x'] and worm['y'] == self.snake.wormCoords[0]['y']):
               self.screen.fill(Config.BG_COLOR)
               self.String()
               self.Check = "GameisOFF"




    def pressforkey(self):
        self.Check = "GameisON"
        del self.snake
        del self.apple
        self.snake = Snake()
        self.apple = Apple()


    def handleevents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and self.snake.direction != self.snake.RIGHT:
                    self.snake.direction = self.snake.LEFT

                if event.key == pygame.K_RIGHT and self.snake.direction != self.snake.LEFT:
                    self.snake.direction = self.snake.RIGHT

                if event.key == pygame.K_UP and self.snake.direction != self.snake.DOWN:
                    self.snake.direction = self.snake.UP

                if event.key == pygame.K_DOWN and self.snake.direction != self.snake.UP:
                    self.snake.direction = self.snake.DOWN
    def draw(self):
        self.drawlines()
        self.drawSnake()
        self.drawApple()
        self.drawScore(len(self.snake.wormCoords) - 3)

    def loop(self):
        while True:
            self.handleevents()
            self.snake.update(self.apple)
            self.clock.tick(Config.FPS)
            self.screen.fill(Config.BG_COLOR)
            self.draw()
            self.gameover()
            pygame.display.update()

            if self.Check == "GameisOFF" :
                break
















