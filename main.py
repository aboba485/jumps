import pygame
import players

# Initialize Pygame
pygame.init()



# Set the window title
pygame.display.set_caption("Jumps")


# Game loop

clock = pygame.time.Clock()


running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the screen
    pygame.display.flip()

# Quit Pygame
pygame.quit()
