import random
import pygame

class Blob:
    
  def __init__(self, color, x_boundary, y_boundary, stay_within_bounds=True, size_range=(4,8), movement_range=(-1,2)):
    self.x_boundary = x_boundary
    self.y_boundary = y_boundary
    self.x = random.randrange(0, self.x_boundary)
    self.y = random.randrange(0, self.y_boundary)
    self.size = random.randrange(size_range[0], size_range[1])
    self.color = color
    self.movement_range = movement_range
    self.stay_within_bounds = stay_within_bounds

  def move(self):
    self.move_x = random.randrange(self.movement_range[0], self.movement_range[1])
    self.move_y = random.randrange(self.movement_range[0], self.movement_range[1])
    self.x += self.move_x
    self.y += self.move_y
    if self.stay_within_bounds:
      self.check_bounds()

  def check_bounds(self):
    if self.x < 0: 
      self.x = 0
    elif self.x > self.x_boundary: 
      self.x = self.x_boundary
    
    if self.y < 0: 
      self.y = 0
    elif self.y > self.y_boundary: 
      self.y = self.y_boundary

  def collision_effect(self, blob):
    pass
  
  def draw(self, game_display):
    pygame.draw.circle(game_display, self.color, [self.x, self.y], self.size)
