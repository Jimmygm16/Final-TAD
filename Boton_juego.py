import pygame as pg
class boton:
    def __init__(self, x, y, w, h, word):
        self.rectangulo = pg.Rect(x, y, w, h)
        self.word = word
        self.active = False
    
    def draw(self, SCREEN):
        font = pg.font.Font(None, 20)
        if self.rectangulo.collidepoint(pg.mouse.get_pos()):
            pg.draw.rect(SCREEN, (48, 59, 61), self.rectangulo, 0)
        else:
            pg.draw.rect(SCREEN, (95, 120, 124), self.rectangulo, 0)  
        txt = font.render(self.word, True, (0, 0, 0))
        SCREEN.blit(txt, (self.rectangulo.x+(self.rectangulo.width-txt.get_width())/2, 
                        self.rectangulo.y+(self.rectangulo.height-txt.get_height())/2))