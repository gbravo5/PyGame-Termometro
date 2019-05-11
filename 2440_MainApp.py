import pygame
from pygame.locals import *
import sys


class mainApp():
    
    # assumptions:
    
    # 1.- screen:
    __images = ('termo1.png', 'posiC.png', 'posiF.png')
    __screen_size = __width, __height = 290, 415
    __window_title = 'Temperature_Converter'
        # 'F4ECCB' ---> HEX F4 =  DEC 244 (Red), HEX EC =  DEC 236 (Green), HEX CB =  DEC 203 (Blue)
    __RGB = (244, 236, 203)
    
    
    def __init__(self):
        # 1.- screen:
        # a) create
        self.__screen = pygame.display.set_mode(self.__screen_size)
        # b) customize
            # title
        pygame.display.set_caption(self.__window_title)
            # background = colour
        self.__background = self.__screen.fill(self.__RGB)
    
    def __on_close(self):
        pygame.quit()
        sys.exit()
       
    def __refresh(self):
        pygame.display.flip()
        
    def conversion(self):
        while True:
            # manage events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.__on_close()
            # refresh
            self.__refresh()
        

if __name__ == '__main__':
    pygame.init()
    app = mainApp()
    app.conversion()
    

        