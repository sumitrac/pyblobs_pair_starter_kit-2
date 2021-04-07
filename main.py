import pygame
import random
import math
from red_blob import RedBlob
from blue_blob import BlueBlob
import color 

STARTING_BLUE_BLOBS = 20
STARTING_RED_BLOBS = 20

WIDTH = 600
HEIGHT = 600

game_display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Blob World")
clock = pygame.time.Clock()

def is_touching(b1, b2):
  return math.sqrt((b2.x-b1.x)**2 + (b2.y-b1.y)**2) < (b1.size + b2.size)

def handle_collisions(blob_list):
    blues, reds = blob_list
    for blue_id, blue_blob in blues.copy().items():
        for other_blobs in blues, reds:#, greens:
            for other_blob_id, other_blob in other_blobs.copy().items():
                if blue_blob == other_blob:
                    pass
                else:
                    if is_touching(blue_blob, other_blob):
                      pass#insert collision event here
                            
    return blues, reds#, greens

def draw_environment(blob_list):
    #draw
    game_display.fill(color.WHITE)
    for blob_dict in blob_list:
        for (blob_id, blob) in blob_dict.items():
            
            blob.draw(game_display)
            blob.move()
            handle_collisions(blob_list)
    # present
    pygame.display.update()
    
def main():
  blue_blobs = dict(enumerate([BlueBlob(WIDTH,HEIGHT) for i in range(STARTING_BLUE_BLOBS)]))
  red_blobs = dict(enumerate([RedBlob(WIDTH,HEIGHT) for i in range(STARTING_RED_BLOBS)]))

  while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        draw_environment([blue_blobs,red_blobs])
        clock.tick(60)

if __name__ == '__main__':
    main()