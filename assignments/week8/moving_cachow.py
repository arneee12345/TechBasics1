import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH = 800
HEIGHT = 600
NUM_CARS = 5
FPS = 60

# Set up display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Assignment 8 – Moving Cachow")

# Load and scale your image
car_image = pygame.image.load("cachow.png")
car_image = pygame.transform.scale(car_image, (80, 60))  # Adjust size if needed

# Define the Car class
class Cachow:
    def __init__(self):
        self.image = car_image
        self.x = random.randint(0, WIDTH - 80)
        self.y = random.randint(0, HEIGHT - 60)
        self.speed_x = random.choice([-3, -2, -1, 1, 2, 3])
        self.speed_y = random.choice([-3, -2, -1, 1, 2, 3])
        self.color_tint = pygame.Color(255, 255, 255)
        self.tint = random.randint(180, 255)

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

        # Bounce on walls
        if self.x <= 0 or self.x + 80 >= WIDTH:
            self.speed_x *= -1
        if self.y <= 0 or self.y + 60 >= HEIGHT:
            self.speed_y *= -1

    def draw(self, surface):
        tinted = self.image.copy()
        tinted.fill((self.tint, self.tint, self.tint), special_flags=pygame.BLEND_RGB_MULT)
        surface.blit(tinted, (self.x, self.y))

# Create multiple instances
cars = [Cachow() for _ in range(NUM_CARS)]

# Game loop
clock = pygame.time.Clock()
running = True

while running:
    screen.fill((30, 30, 30))  # Background color

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update and draw each car
    for car in cars:
        car.move()
        car.draw(screen)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()