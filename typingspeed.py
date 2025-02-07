import time
import random
import json

with open('typing_test_words_1000.json', 'r') as word_doc:
    data = json.load(word_doc)  # Load JSON data correctly

complete_list = data['typing_test_words']

random_50 = random.sample(complete_list, 50)

typing_test_string = ' '.join(random_50)
print(typing_test_string)