from blob import Blob
import color
import random

class RedBlob(Blob):
  def __init__(self, x_boundary, y_boundary):
    super().__init__(color.RED, x_boundary, y_boundary)