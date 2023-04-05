#!/usr/bin/python3
"""DEfine class Rectangle"""

class Rectangle:
    
    """Class rectangle: it will define the properties:
        Attributes: 
        width: rep width of the rectangle
        height: rep height of the rect:
        """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Method that will be called everytime when class rectangle is instaciated
         Args:
         width: default value of 0
         height: default value of o
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """the getter method for width
        
        return: the obj
        """
        return self.__width

    @width.setter
    def width(self, value):
        """the setter method for width
        args: 
            value(int)
        raise:
            TypeError: if not type(value==0)
            ValueError: value < 0
        """
        if not issubclass(type(value), int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width  = value

    @property
    def height(self):
        """The getter method for height"""
        return self.__height
    @height.setter
    def height(self, value):
        """The setter method for height
            args:
            value(int)
            raises:
            TypeError: if not isinstance(value, int)
            ValueError: value < 0
        """
        if not issubclass(type(value), int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """public instance for method that returns area of a triangle"""
        return self.__width*self.__height

    def perimeter(self):
        """Public instance method that returns the periemter of triangle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return (self.__width + self.__height)*2

    def __str__(self):
        """it will print the representation of the rectangle with character #"""
        if self.__height == 0 or self.__width == 0:
            return ("")

        rectlist = []

        for i in range(self.__height):
            for j in range(self.__width):
                rectlist.append(str(self.print_symbol))
            rectlist.append("\n")

        """remove the last blank line"""
        rectlist.pop()

        return ("".join(rectlist))

    def __repr__(self):
        """this method return the string rep of the rectangle"""
        div = "Rectangle({:d}, {:d})".format(self.__width, self.__height)
        return (div)

    def __del__(self):
        """for deleting an instance"""
        prin = "Bye rectangle..."
        print(f"{prin}")
        """DEcrement"""
        type(self).number_of_instances -= 1

    @staticmethod 
    def bigger_or_equal(rect_1, rect_2):
        """static method that returns the biggest rectangle based on area"""

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        F_area = rect_1.area()
        S_area = rect_2.area()

        if F_area >= S_area:
            return rect_1
        else:
            return rect_2




