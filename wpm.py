def raw_wpm(time, str):
    char_count = len(str)
    raw_wpm = (char_count / 5) / time
    return raw_wpm

def adjusted_wpm(raw, accuracy):
    return (accuracy / 100) * raw