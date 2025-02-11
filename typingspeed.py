import time
import random
import json
from accuracy import string_similarity
import time
from wpm import raw_wpm, adjusted_wpm

with open('typing_test_words_1000.json', 'r') as word_doc:
    data = json.load(word_doc) 

complete_list = data['typing_test_words']

random_50 = random.sample(complete_list, 30)

typing_test_string = ' '.join(random_50)
print(typing_test_string + '\n')
input("This is a typing speed test. Press Enter to begin the test")
start_time = time.time()
user_text = input('Go!\n')
end_time = time.time()
user_time = end_time - start_time
user_time = user_time / 60
percent = string_similarity(typing_test_string, user_text)
user_raw = raw_wpm(user_time, user_text)
user_adj = adjusted_wpm(user_raw, percent)


print("\nResults:")
print("Adjusted WPM: " + str(int(user_adj)))
print("Accuracy: " + str(int(percent)) + "%")
print("Raw WPM: " + str(int(user_raw)) + "\n")






