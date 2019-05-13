import pygame
from pygame.locals import *
import sys


images = ('termo1.png', 'posiC.png', 'posiF.png')


class thermometer():
    
    def __init__(self):
        self.custome = pygame.image.load('images/{}'.format(images[0]))
        

class data_input():
    
    __value = 0                                               # by default
    __value_txt   = ''                                        # by default
    __value_colour = (74, 74, 74)                             # RGB
    
    __coordinates_rectangle = __x, __y = 0, 0                 # [x, y] by default
    __size_rectangle        = __width, __height = 0, 0        # [width, height] by default
    
    __font_name = 'Arial'                                     # by default
    __font_size = 24                                          # by default
    
    def __init__(self, value = 0):
        
        # render to string
        txt_block = self.__font.render(self.__value_txt, True, self.__value_colour)
        
        # draw rectangle
        rectangle = txt_block.get_rect()
        rectangle.left = self.__x
        rectangle.top  = self.__y
        rectangle.size = self.__size_rectangle
        
        # font set up
        self.__font = pygame.font.SysFont(self.__font_name, self.__font_size)
        
   
    # provide public setter and getter methods to access and update the value of a private variable:
    
        # a) setter y getter de value 
    
    def value(self, val = None):
        if val == None:
            return self.__value                     # setter
        else:
            val = str(val)
            try:
                self.__value     = int(val)         # getter
                self.__value_txt = val              # getter
            except:
                pass
    
        # b) setter y getter de size-width
        
    def size_rectangle_width(self, val = None):
        if val == None:
            return self.__width                      # setter
        else:
            try:
                self.__width = int(val)              # getter
            except:
                pass
        
        # c) setter y getter de size-height
        
    def size_rectangle_height(self, val = None):
        if val == None:
            return self.__height                     # setter
        else:
            try:
                self.__height = int(val)             # getter
            except:
                pass
        
        # d) setter y getter de coordinates_rectangle-x
    
    def coordinates_rectangle_x(self, val = None):
        if val == None:
            return self.__x
        else:
            try:
                self.__x = int(val)
            except:
                pass
            
        # e) setter y getter de coordinates_rectangle-y
    
    def coordinates_rectangle_y(self, val = None):
        if val == None:
            return self.__y
        else:
            try:
               self.__y = int(val)
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
    size_temperature = width, height = 133, 28
    coordinates_temperature = x, y = 106, 58
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
        self.temperature.size_rectangle_width(self.width)
        self.temperature.size_rectangle_height(self.height)
        self.temperature.coordinates_rectangle_x(self.x)
        self.temperature.coordinates_rectangle_y(self.y)
    
    def __on_close(self):
        pygame.quit()
        sys.exit()
        
    def __update(self):
        # a) draw thermometer
        self.__screen.blit(self.thermometer.custome, self.coordinates_thermometer)
        # a) draw temperatur-rectangle
        self.__screen.blit(
       
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
    

        