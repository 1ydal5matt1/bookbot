
def get_num_words(content):
    return len(content.split())

def count_char(content):
    chars = {}
    for i in "abcdefghijklmnopqrstuvwxyz!.,;:":
        count = content.lower().count(i)
        chars[i] = count
    return chars