import pygame

# Initialize Pygame
pygame.init()

# Create display window
window = pygame.display.set_mode((400, 400))

# Set background color
window.fill((255, 255, 255))

# Set color and line thickness
black = (0, 0, 0)
line_width = 5

# Draw the cart body (rectangle)
pygame.draw.rect(window, black, (100, 150, 200, 100), line_width)

# Draw the wheels (circles)
pygame.draw.circle(window, black, (120, 280), 20, line_width)  # Left wheel
pygame.draw.circle(window, black, (280, 280), 20, line_width)  # Right wheel

# Draw the basket lines (horizontal)
pygame.draw.line(window, black, (110, 200), (290, 200), line_width)
pygame.draw.line(window, black, (110, 175), (290, 175), line_width)

# Draw the basket lines (vertical)
pygame.draw.line(window, black, (150, 150), (150, 250), line_width)
pygame.draw.line(window, black, (250, 150), (250, 250), line_width)

# Draw the handle (line)
pygame.draw.line(window, black, (290, 175), (350, 100), line_width)

# Update the display
pygame.display.update()

# Keep window open for a few seconds
pygame.time.wait(5000)

# Quit Pygame
pygame.quit()

