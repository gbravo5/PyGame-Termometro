import pygame
from pygame.locals import *
import sys


images = ('termo1.png', 'posiC.png', 'posiF.png')


class thermometer():
    
    def __init__(self):
        self.custome = pygame.image.load('images/{}'.format(images[0]))


class mainApp():
    
    # assumptions:
    
    # 1.- screen:
    __screen_size = __width, __height = 290, 415
    __window_title = 'Temperature_Converter'
        # 'F4ECCB' ---> HEX F4 =  DEC 244 (Red), HEX EC =  DEC 236 (Green), HEX CB =  DEC 203 (Blue)
    __RGB = (244, 236, 203)
    
    # 2.- features:
    thermometer = None
    coordinates_thermometer = 50, 34
    data_input  = None
    selector    = None    
    
    def __init__(self):
        # 1.- screen:
        # a) create
        self.__screen = pygame.display.set_mode(self.__screen_size)
        # b) customize
            # title
        pygame.display.set_caption(self.__window_title)
            # background = colour (RGB)
        self.__background = self.__screen.fill(self.__RGB)
        # 2.- thermometer:
        # a) create
        self.thermometer = thermometer()
    
    def __on_close(self):
        pygame.quit()
        sys.exit()
        
    def __update(self):
        # a) draw thermometer
        self.__screen.blit(self.thermometer.custome, self.coordinates_thermometer)
       
    def __refresh(self):
        pygame.display.flip()
        
    def conversion(self):
        while True:
            # manage events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.__on_close()
            # update
            self.__update()
            # refresh
            self.__refresh()
        

if __name__ == '__main__':
    pygame.init()
    app = mainApp()
    app.conversion()
    

        