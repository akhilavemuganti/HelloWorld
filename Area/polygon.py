class Polygon:
    __width = None # double __ indicates a private variable
    __height = None

    def set_value(self,width,height):
        self.__width = width
        self.__height = height

    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height