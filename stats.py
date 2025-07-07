
def get_num_words(content):
    return len(content.split())

def count_char(content):
    chars = {}
    for i in "abcdefghijklmnopqrstuvwxyz!.,;:":
        count = content.lower().count(i)
        chars[i] = count
    return chars

def sort_dict(dictonary):
    return sorted(dictonary.items(), key=lambda item: item[1], reverse=True)

#============ BOOKBOT ============
# Analyzing book found at books/frankenstein.txt...
# ----------- Word Count ----------
# Found 75767 total words
# --------- Character Count -------
# e: 44538
# t: 29493
# a: 25894
# o: 24494
# i: 23927
# n: 23643
# s: 20360
# r: 20079
# h: 19176
# d: 16318
# l: 12306
# m: 10206
# u: 10111
# c: 9011
# f: 8451
# y: 7756
# w: 7450
# p: 5952
# g: 5795
# b: 4868
# v: 3737
# k: 1661
# x: 691
# j: 497
# q: 325
# z: 235
# æ: 28
# â: 8
# ê: 7
# ë: 2
# ô: 1
# ============= END ===============