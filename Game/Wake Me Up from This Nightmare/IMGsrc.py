# IMGsrc.py
import pygame
import os

# Define some colors
WHITE = (255, 255, 255)
DARK_GRAY = (50, 50, 50)

# Define backgrounds, characters, dialogues, and choices
scenes = [
    {
        'background': 'Background/houses.jpg', 
        'character': 'Character/pngegg.png',     
        'dialogue': "Hello! Welcome to our game.",
        'choices': [
            {'text': 'Greet back', 'next_scene': 1},
            {'text': 'Ignore', 'next_scene': 2}
        ]
    },
    {
        'background': 'Background/houses.jpg',  
        'character': 'Character/pngegg.png',     
        'dialogue': "Nice to meet you! How are you?",
        'choices': [
            {'text': 'I\'m good', 'next_scene': 2},
            {'text': 'Not great', 'next_scene': 3}
        ]
    },
    {
        'background': 'Background/houses.jpg',  
        'character': 'Character/pngegg.png',   
        'dialogue': "Alright, have a good day!",
        'choices': []
    },
    {
        'background': 'Background/houses.jpg', 
        'character': 'Character/pngegg.png',    
        'dialogue': "Sorry to hear that. Hope you feel better soon!",
        'choices': []
    }
]

# Load all images upfront
for scene in scenes:
    scene['background_img'] = pygame.image.load(scene['background'])
    scene['character_img'] = pygame.image.load(scene['character'])
