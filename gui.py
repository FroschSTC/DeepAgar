import pygame

class Camera:
    def __init__(self, screen_width, screen_height):
        self.x = 0
        self.y = 0
        self.width = screen_width
        self.height = screen_height
        self.zoom = 0.5

    def centre(self,blobOrPos):
        if isinstance(blobOrPos, Player):
            p = blobOrPos
            self.x = (p.startX-(p.x*self.zoom))-p.startX+((screen_width/2))
            self.y = (p.startY-(p.y*self.zoom))-p.startY+((screen_height/2))
        elif(type(blobOrPos) == tuple):
            self.x,self.y = blobOrPos


class GUI:

    def __init__(self):
        pygame.init()
        pygame.display.set_caption("DeepAgar")
        screen_width, screen_height = (800, 500)

        self.surface = pygame.display.set_mode((screen_width,screen_height))
        self.surface_leaderboard = pygame.Surface((155, 278), pygame.SRCALPHA)
        self.surface_leaderboard.fill((50, 50, 50, 80))

        self.camera = Camera()


    def render(self):
        pass



    def draw_grid(self):
        for i in range(0,2001,25):
            pygame.draw.line(self.surface, (230, 240, 240), (0+camera.x,i*camera.zoom+camera.y),(2001*camera.zoom+camera.x,i*camera.zoom+camera.y),3)
            pygame.draw.line(self.surface, (230, 240, 240), (i*camera.zoom+camera.x,0+camera.y),(i*camera.zoom+camera.x,2001*camera.zoom+camera.y),3)