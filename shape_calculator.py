class Rectangle:
  #initialize with width and height attributes
  def __init__(self, width, height):
    self.width = width
    self.height = height
  def set_width(self, new_width):
    self.width = new_width
  def set_height(self, new_height):
    self.height = new_height
  def get_area(self):
    area = self.width * self.height
    return area
  def get_perimeter(self):
    perimeter = (2 * self.width) + (2 * self.height)
    return perimeter
  def get_diagonal(self):
    diagonal = ((self.width ** 2) + (self.height ** 2)) ** 0.5
    return diagonal
  #Add *'s equal to the width followed by a "\n", repeated this n = height times
  def get_picture(self):
    if self.height and self.width > 50:
      return "Too big for picture."
    else:
      asterisks = []
      hcounter = 0
      while hcounter < self.height:
        wcounter = 0
        while wcounter < self.width:
          asterisks.append("*")
          wcounter += 1
        asterisks.append("\n")
        hcounter += 1
      return ''.join(asterisks)
  #divide area of current object by new object, retur only integer values
  def get_amount_inside(self, shape):
    area1 = self.get_area()
    area2 = shape.get_area()
    amount_inside = int(area1 / area2)  
    return amount_inside
  #what should happen when object is printed
  def __str__(self):
    return("Rectangle(width=" + str(self.width) + ", height=" + str(self.height)+")")
    
#Square is subclass of Rectangle    
class Square(Rectangle):
  def __init__(self, width):
    self.width = width
    self.height = width
  def set_side(self, new_width):
    self.width = new_width
    self.height = new_width
  def __str__(self):
    return("Square(side=" + str(self.width) + ")")