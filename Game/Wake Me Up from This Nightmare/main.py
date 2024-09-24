# main.py
import pygame
from scripts import render_scene, draw_exit_button, check_button_click, check_click, scenes, WHITE

# Initialize Pygame
pygame.init()

# Set up the screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)

# Set the title of the window
pygame.display.set_caption("Slide Choice Game")

# Main loop
current_scene = 0
running = True

while running:
    screen.fill(WHITE)
    
    # Render the current scene
    render_scene(current_scene, screen, screen_width, screen_height)
    
    # Draw exit button
    draw_exit_button(screen)
    
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            
            # Check if the exit button is clicked
            button_action = check_button_click(mouse_pos)
            if button_action == "exit":
                running = False
            
            # Check if choices are clicked
            next_scene = check_click(mouse_pos, current_scene)
            if next_scene is not None:
                current_scene = next_scene

    # Update the display
    pygame.display.flip()

# Quit the game
pygame.quit()
