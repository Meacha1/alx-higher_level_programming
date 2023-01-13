#!/usr/bib/python3

ass Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        """Class constructor
        Arguments:
            width {int} -- width of the rectangle
            height {int} -- height of the rectangle
            x {int} -- default 0
            y {int} -- default 0
            id {int} -- id -> if None, will use the logic from the super class
        """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        if height <= 0:
            raise ValueError("height must be > 0")
        if x < 0:
            raise ValueError("x must be >= 0")
        if y < 0:
            raise ValueError("y must be >= 0")
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """Getter for the private width attribute
        Returns:
            int -- width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for the private width attribute
        Arguments:
            value {int} -- width of the rectangle
        Raises:
            TypeError: width must be an integer
            ValueError: width must be > 0
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter for the private height attribute
        Returns:
            int -- height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for the private height attribute
        Arguments:
            value {int} -- height of the rectangle
        Raises:
            TypeError: height must be an integer
            ValueError: height must be > 0
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter for the private x attribute
        Returns:
            int -- x of the rectangle
        """
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for the private x attribute
        Arguments:
            value {int} -- x of the rectangle
        Raises:
            TypeError: x must be an integer
            ValueError: x must be >= 0
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter for the private y attribute
        Returns:
            int -- y of the rectangle
        """
        return self.__y
        
    @y.setter
    def y(self, value):
        """Setter for the private y attribute
        Arguments:
            value {int} -- y of the rectangle
        Raises:
            TypeError: y must be an integer
            ValueError: y must be >= 0
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
    def area(self):
    """calculets the area of the rectangle"""
        return self.width * self.height
    def display(self):
    """display the shape of the rectangle"""
        for i in range(self.height):
            for j in range(self.width):
                print("#", end="")
            print()
