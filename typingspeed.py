import time
import random
import json
import pygame

with open('typing_test_words_1000.json', 'r') as word_doc:
    data = json.load(word_doc) 

complete_list = data['typing_test_words']

random_50 = random.sample(complete_list, 50)

typing_test_string = ' '.join(random_50)
print(typing_test_string + '\n')
user_text = input('type the following text as fast as you can!')
correct_chars = user_text & typing_test_string
correct_chars_length = len(correct_chars)


