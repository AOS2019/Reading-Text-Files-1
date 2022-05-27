# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

from itertools import count


def read_file_content(filename):
    # [assignment] Add your code here 
    f=open(filename)
    text = f.read()
    return text


def count_words():
    #word_count = []
    #text_word = []
    text = read_file_content("./story.txt")
    # [assignment] Add your code here
    new_text=text.lower().replace('\n', " ")
    new_text=new_text.replace('.'," ")
    new_text=new_text.replace('?', " ")
    bagOfWords=new_text.split(' ')
    count = {}
    for i in bagOfWords:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    del count['']
    #count = sorted(count.items(), reverse = False)
    print(len(count))
    print(count)
    return count


count_words()