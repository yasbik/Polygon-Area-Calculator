class Rectangle:

    # initialize a rectangle
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height
    

    def set_width(self, w):
        self.width = w


    def set_height(self, h):
        self.height = h
    

    def get_area(self):
        return (self.width * self.height)
    

    def get_perimeter(self):
        return (2 * (self.width + self.height))
    

    # method to get the diagonal of a shape
    def get_diagonal(self):
        return  (((self.width ** 2) + (self.height ** 2)) ** .5)
    

    # method to draw the shape using with *'s
    def get_picture(self):
        output = ""

        # cannot draw shapes with dimentions exceeding 50
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        
        # draw the shape
        for i in range(self.height):
            for j in range(self.width):
                output += "*"
            output += "\n"
        
        return output
    

    # method to calculate how many of one shape would fit into another without rotation
    def get_amount_inside(self, shape):
        width_ratio = self.width // shape.width
        height_ratio = self.height // shape.height
        return width_ratio * height_ratio
    

    # standard tostring method
    def __str__(self) -> str:
        output = f"Rectangle(width={self.width}, height={self.height})"
        return output
    

# child class of rectangle
class Square(Rectangle):

    # initialize a suqre
    def __init__(self, side) -> None:
        super().__init__(side, side)
    

    def set_side(self, s):
        self.width = s
        self.height = s
    

    # standard tostring method
    def __str__(self) -> str:
        output = f"Square(side={self.width})"
        return output

