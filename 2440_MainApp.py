import pygame
from pygame.locals import *
import sys


images = ('termo1.png', 'posiC.png', 'posiF.png')


class thermometer():
    
    def __init__(self):
        self.custome = pygame.image.load('images/{}'.format(images[0]))
        

class data_input():
    
    __value = 0                                               # by default
    __value_txt   = '0'                                        # by default
    __value_colour = (74, 74, 74)                             # RGB
    
    __size_rectangle        =  [0, 0]                         # [width, height] by default
    __coordinates_rectangle =  [0, 0]                         # [x, y] by default
    
    __font_name = 'Arial'                                     # by default
    __font_size = 24                                          # by default
    
    def __init__(self):
        
        # font set up
        self.__font = pygame.font.SysFont(self.__font_name, self.__font_size)
   
    def render(self):
       
        # render to string
        txt_block = self.__font.render(self.__value_txt, True, self.__value_colour)
        
        # draw rectangle
        rectangle = txt_block.get_rect()                   # create a rectangle s.a txt_block size [width, height]
        rectangle.left = self.__coordinates_rectangle[0]
        rectangle.top  = self.__coordinates_rectangle[1]
        rectangle.size = self.__size_rectangle
        
        return [txt_block, rectangle]
    
    # provide public setter and getter methods to access and update the value of a private variable:
    
        # a) setter y getter de value 
    
    def value(self, val = None):
        if val == None:
            return self.__value                       # setter = value by default
        else:
            val = str(val)
            try:
                self.__value       = int(val)         # getter
                self.__value_txt   = val              # getter
            except:
                pass
    
        # b) setter y getter de size [width, height]
        
    def size_rectangle(self, val = None):
        if val == None:
            return self.__size_rectangle                               # setter = value by default
        else:
            try:
                self.__size_rectangle = [int(val[0]), int(val[1])]     # getter
            except:
                pass

        
        # d) setter y getter de coordinates_rectangle [x, y]
    
    def coordinates_rectangle(self, val = None):
        if val == None:
            return self.__coordinates_rectangle                               # setter = value by default
        else:
            try:
                self.__coordinates_rectangle = [int(val[0]), int(val[1])]     # getter
            except:
                pass
        

class mainApp():
    
    # assumptions:
    
    # 1.- screen:
    screen_size = width, height = 290, 415
    window_title = 'Temperature_Converter'
        # 'F4ECCB' ---> HEX F4 =  DEC 244 (Red), HEX EC =  DEC 236 (Green), HEX CB =  DEC 203 (Blue)
    RGB = (244, 236, 203)
    
    # 2.- features:
    thermometer = None
    coordinates_thermometer = 50, 34
    
    temperature = None
    size_temperature = [133, 28]
    coordinates_temperature = [106, 58]
    colour_temperature = (255, 255, 255)
    
    selector    = None
    #coordinates_selector =
    
    
    def __init__(self):
        
        # 1.- screen:
            # a) create
        self.__screen = pygame.display.set_mode(self.screen_size)
            # b) customize
            # title
        pygame.display.set_caption(self.window_title)
            # background = colour (RGB)
        self.background = self.__screen.fill(self.RGB)
        
        # 2.- thermometer:
            # a) create
        self.thermometer = thermometer()
        
        # 3.- temperature:
            # a) create 
        self.temperature = data_input()
            # b) rectangle set up
        self.temperature.size_rectangle(self.size_temperature)
        self.temperature.coordinates_rectangle(self.coordinates_temperature)


    def __on_close(self):
        pygame.quit()
        sys.exit()
        
    def __update(self):
        # a) draw thermometer
        self.__screen.blit(self.thermometer.custome, self.coordinates_thermometer)
        # b) draw temperature
        txt_block = self.temperature.render()[0]
        rectangle = self.temperature.render()[1]
            # b.1) fondo blanco (donde, color RGB, qué rectangulo)
        pygame.draw.rect(self.__screen, self.colour_temperature, rectangle)
            # b.2) txt
        self.__screen.blit(txt_block, self.coordinates_thermometer)
        
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
    

        