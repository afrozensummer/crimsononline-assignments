"""
Question 1

objectives
    - get more comfortable with Python
    - learn how to handle exceptions
    - work with the file system
"""
from collections import Counter

#So, I kind of got it printing tuples for each one...
#so I have to fix that....

def common_words(filename):
    """question 1a

    Write a function that takes a path to a text file as input. The function
    should open the file, count the number of occurrences of each word, and
    return a sorted list of the most common words.
    """
    #Counter has methods that finds the most common words :)
    words = []
    temp = []
    f = open(filename, mode = 'r')
    for line in f:
        temp = line.split()
        words = words + temp
    count = Counter(words)
    list = count.most_common()
    return list
    f.close()

def common_words_min(filename, min_chars):
    """question 1b

    Modify this function to take a second argument that specifies the
    minimum number of characters long a word can be to be counted.
    """
    words = []
    temp = []
    newwords = []
    f = open(filename, mode = 'r')
    for line in f:
        temp = line.split()
        words = words + temp
    for word in words:
        if (len(word) >= min_chars):
            newwords.append(word)
    count = Counter(newwords)
    list = count.most_common()
    return list
    f.close()

def common_words_tuple(filename, min_chars):
    """question 1c

    Modify this function to return a list of tuples rather than just a list
    of strings. Each tuple should be of the format
        (word, number of occurrences)
    Of course, the list of tuples should still be sorted as in part a.
    """
    words = []
    temp = []
    f = open(filename, mode = 'r')
    for line in f:
        temp = line.split()
        words = words + temp
    count = Counter(words)
    list = count.most_common()
    return list
    f.close()

def common_words_safe(filename, min_chars):
    """question 1d

    Modify your function so that it catches the IOError exception and prints
    a friendly error message.
    """
    try:
        words = []
        open(filename, mode = 'r')
        count = Counter(words)
        for line in filename:
            for word in line:
                words.append(word)
        common = set(words)
        list = count.most_common()
        filename.close()
    except (IndexError, IOError):
        print 'ERROR. (you fail)'