# word_count.py
# Jeff Smith
# Opens a source text file and counts the most commonly used words
# Omit all common stopwords from count

from collections import Counter
import string

# Open source text
with open('frankenstein.txt', 'r') as frank_file:
    frank_file = frank_file.read()
    translator = str.maketrans(
        '', '', string.punctuation)  # Strip all punctuation
    string_without_punct = frank_file.translate(translator)
    stripped_frank = string_without_punct.split()

frank = [item.lower() for item in stripped_frank]

# List of words to ingnore
stopwords = [
    'a', 'about', 'above', 'after', 'again', 'against', 'ain', 'all', 'am', 'an', 'and', 'any', 'are', 'aren', "aren't", 'as', 'at', 'be', 'because', 'been', 'before', 'being', 'below', 'between', 'both', 'but', 'by', 'can', 'couldn', "couldn't", 'd', 'did', 'didn', "didn't", 'do', 'does', 'doesn', "doesn't", 'doing', 'don', "don't", 'down', 'during', 'each', 'few', 'for', 'from', 'further', 'had', 'hadn', "hadn't", 'has', 'hasn', "hasn't", 'have', 'haven', "haven't", 'having', 'he', 'her', 'here', 'hers', 'herself', 'him', 'himself', 'his', 'how', 'i', 'if', 'in', 'into', 'is', 'isn', "isn't", 'it', "it's", 'its', 'itself', 'just', 'll', 'm', 'ma', 'me', 'mightn', "mightn't", 'more', 'most', 'mustn', "mustn't", 'my', 'myself', 'needn', "needn't", 'no', 'nor', 'not', 'now', 'o', 'of', 'off', 'on', 'once', 'only', 'or', 'other', 'our', 'ours', 'ourselves', 'out', 'over', 'own', 're', 's', 'same', 'shan', "shan't", 'she', "she's", 'should', "should've", 'shouldn', "shouldn't", 'so', 'some', 'such', 't', 'than', 'that', "that'll", 'the', 'their', 'theirs', 'them', 'themselves', 'then', 'there', 'these', 'they', 'this', 'those', 'through', 'to', 'too', 'under', 'until', 'up', 've', 'very', 'was', 'wasn', "wasn't", 'we', 'were', 'weren', "weren't", 'what', 'when', 'where', 'which', 'while', 'who', 'whom', 'why', 'will', 'with', 'won', "won't", 'wouldn', "wouldn't", 'y', 'you', "you'd", "you'll", "you're", "you've", 'your', 'yours', 'yourself', 'yourselves'
]

stopwords = set(stopwords)

for i in reversed(range(len(frank))):
    # Iterate through words in text
    if frank[i] in stopwords:
        # Remove stopwords from text
        frank.pop(i)

word_dict = {}
words = list(word_dict.items())  # Returns list of tuples
# Iterate through list of words
# Add 1 to counter for each inference of word
for word in frank:
    if word in word_dict:
        word_dict[word] += 1
    else:
        word_dict[word] = 1

# Determine most commonly used words in text
count = Counter(word_dict)
high = count.most_common(10)

# Pass results to console

print("These are the most common words in my book, with their tally:")

for i in high:
    print(i[0], ":", i[1], " ")
