# scripts.py
import pygame
from IMGsrc import scenes, WHITE, DARK_GRAY

# Function to render text on the screen
def render_text(screen, text, x, y, color=WHITE):
    font = pygame.font.Font(None, 36)
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

# Function to draw a box around the text
def draw_text_box(screen, x, y, width, height):
    pygame.draw.rect(screen, DARK_GRAY, (x, y, width, height), border_radius=10)
    pygame.draw.rect(screen, WHITE, (x, y, width, height), 2, border_radius=10)

# Function to handle rendering a scene
def render_scene(scene_index, screen, screen_width, screen_height):
    scene = scenes[scene_index]
    screen.blit(pygame.transform.scale(scene['background_img'], (screen_width, screen_height)), (0, 0))  # Display background image
    screen.blit(pygame.transform.scale(scene['character_img'], (200, 300)), (200, 100))  # Display character image

    # Display dialogue with box
    dialogue_box_width = screen_width - 100
    dialogue_box_height = 80
    draw_text_box(screen, 50, 400, dialogue_box_width, dialogue_box_height)
    render_text(screen, scene['dialogue'], 60, 420, WHITE)

    # Display choices if available with boxes
    if 'choices' in scene and scene['choices']:
        for i, choice in enumerate(scene['choices']):
            choice_box_y = 500 + i * 50
            draw_text_box(screen, 50, choice_box_y, dialogue_box_width, 40)
            render_text(screen, f"{i+1}. {choice['text']}", 60, choice_box_y + 10, WHITE)

# Function to check if a mouse click is within a choice box
def check_click(mouse_pos, scene_index):
    scene = scenes[scene_index]
    if 'choices' in scene and scene['choices']:
        for i, choice in enumerate(scene['choices']):
            if 50 <= mouse_pos[0] <= 800 - 50 and (500 + i * 50) <= mouse_pos[1] <= (500 + i * 50 + 40):
                return choice['next_scene']
    return None

# Function to create buttons for exiting
def draw_exit_button(screen):
    pygame.draw.rect(screen, (200, 200, 200), (650, 10, 120, 40))
    render_text(screen, "Exit", 680, 20, (0, 0, 0))

# Function to check if a mouse click is on the exit button
def check_button_click(mouse_pos):
    # Exit button
    if 650 <= mouse_pos[0] <= 770 and 10 <= mouse_pos[1] <= 50:
        return "exit"
    
    return None
