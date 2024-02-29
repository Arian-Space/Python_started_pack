#source: danielle3625/shape_calculator
"""
Using source to make the objets notation in python,
Operations and loops are no problem
"""

# We define object: Rectangle
class Rectangle:

    # With this we define the parameters of the object
    def __init__(self, width, height):
        self.width = width 
        self.height = height

    # Now using set_width
    def set_width(self, width):
        self.width = width

    # Now using set_height
    def set_height(self, height):
        self.height = height

    # Area of ​​a rectangle
    def get_area(self):
        return self.width * self.height

    # Perimeter of a rectangle
    def get_perimeter(self):
        return (2 * self.width) + (2 * self.height)

    # Diagonal of a rectangle
    def get_diagonal(self):
        return((self.width ** 2 + self.height ** 2) ** .5)

    # get_picture function of a rectangle: 
    def get_picture(self):
        text = ''
        i = 0
        j = 0

        # Conditional for image
        if self.width and self.height <= 50:
            for i in range(0,self.height):
              for j in range(0,self.width):
                text = text + '*'
              text += '\n'
            return text
              
        else:
          # Exeption
          return 'Too big for picture.'

    # Function get_amount_inside: 
    def get_amount_inside(self, shape):
        self.shape = shape
        #reparación de código
        return self.get_area() // (shape.width * shape.height)
        
    # Rectangle string
    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'

# We define object: Square
class Square(Rectangle):
    # Define the equivalent parameter 'side'
    def __init__(self, side):
        (Rectangle.width,Rectangle.height) = (side,side)
  
    # Now using set_side
    def set_side(self, value):
        Rectangle.set_width(self, value)
        Rectangle.set_height(self, value)

    # Square string
    def __str__(self):
        return f'Square(side={self.width})'

# To create a rectangle
print('FOR RECTANGLE-----------------')
print()
rect = shape_calculator.Rectangle(10, 5)
print('create rectangle if with = 10, heigth = 3:')
print()
print('shape_calculator.Rectangle(with, heigth) =>')
print()
print('rect = shape_calculator.Rectangle(10, 5)')
print()
print('for set with => rect.set_width(num)')
print()
print('for set heigth => rect.set_heigth(num)')
print()
print('for area => rect.get_area(): ',rect.get_area())
print()
print('for perimeter => rect.get_perimeter(): ',rect.get_perimeter())
print()
print('for diagonal => rect.get_diagonal(): ',rect.get_diagonal())
print()
print('for picture => rect.get_picture(): ')
print()
print(rect.get_picture())
print()

# To create a square 
print('FOR SQUARE-------------------')
print()
sq = shape_calculator.Square(3)
print('create square if side = 3:')
print()
print('shape_calculator.Square(side) =>')
print()
print('sq = shape_calculator.Square(3)')
print()
print('for set with => rect.set_side(side)')
print()
print('for area => sq.get_area(): ',sq.get_area())
print()
print('for perimeter => sq.get_perimeter(): ',sq.get_perimeter())
print()
print('for diagonal => sq.get_diagonal(): ',sq.get_diagonal())
print()
print('for picture => sq.get_picture(): ')
print()
print(sq.get_picture())
print()
print("^ Yeah, it's a square")
