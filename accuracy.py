from difflib import SequenceMatcher
def truncate(num):
    return int(num * 100) / 100

def string_similarity(s1, s2):
    similarity = SequenceMatcher(None, s1, s2).ratio()
    return int(truncate(similarity) * 100)

s1 = "hello world"
s2 = "hello wrld"

print(string_similarity(s1, s2))



