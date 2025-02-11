def accuracy(self, str1, str2):
    matches = sum(1 for o, t in zip(str1, str2) if o == t)
