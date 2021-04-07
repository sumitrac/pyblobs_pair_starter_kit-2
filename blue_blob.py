from blob import Blob
import color
import random

class BlueBlob(Blob):
  def __init__(self, x_boundary, y_boundary):
    super().__init__(color.BLUE, x_boundary, y_boundary, stay_within_bounds=False)
  
  def move(self):
    self.x += random.randrange(-5,6)
    self.y += random.randrange(-5,6)