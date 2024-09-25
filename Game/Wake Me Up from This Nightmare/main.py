# Import Neccesary Lib And Modules
import pygame
from scripts import render_scene, draw_exit_button, check_button_click, check_click, scenes, WHITE

# Initialize Pygame
pygame.init()

# Window Set Up 
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)

# Title Window 
pygame.display.set_caption("Wake me up from this nightmare")

# Main loop
current_scene = 0
running = True

while running:
    screen.fill(WHITE)
    
    # Render Screen
    render_scene(current_scene, screen, screen_width, screen_height)
    
    # Call Exit Button
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

    # Update display
    pygame.display.flip()

# Quit 
pygame.quit()
