import re

# Open the file
path=r"Confessions of a Tradesman by Frank Thomas Bullen Book Cover  Download This eBook.txt".replace('\\', '/')

# Function to search the hapaxes
def hapax(the_path):
    file = open(the_path)
    list_of_words = re.findall('\w+', file.read().lower())
    freq = {key: 0 for key in list_of_words}
    for word in list_of_words:
        freq[word] += 1
    for word in freq:
        if freq[word] == 1:
            print(word)
hapax(path)