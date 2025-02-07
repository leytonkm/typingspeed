import time
import random
import json
import pygame

with open('typing_test_words_1000.json', 'r') as word_doc:
    data = json.load(word_doc) 

complete_list = data['typing_test_words']

random_50 = random.sample(complete_list, 50)

typing_test_string = ' '.join(random_50)
print(typing_test_string)

pygame.init()
screen = pygame.display.set_mode((600, 200))
font = pygame.font.Font(None, 36)

text = ""
running = True
while running:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                print("User Typed:", text)
                running = False
            elif event.key == pygame.K_BACKSPACE:
                text = text[:-1]
            else:
                text += event.unicode

    render_text = font.render(text, True, (0, 0, 0))
    screen.blit(render_text, (50, 100))
    pygame.display.flip()

pygame.quit()
