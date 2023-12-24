import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import matplotlib.pyplot as plt
from collections import Counter

with open('chesterton-ball.txt', 'r', encoding='utf-8') as file:
    text = file.read()

words = word_tokenize(text)

word_freq = Counter(words)
top_words = [(word, freq) for word, freq in word_freq.most_common(10) if word.isalnum()]

top_words, frequencies = zip(*top_words)

plt.bar(top_words, frequencies)
plt.title('10 найбільш вживаних слів у тексті')
plt.xlabel('Слова')
plt.ylabel('Частота вживання')
plt.show()

stop_words = set(stopwords.words('english'))
filtered_words = [word.lower() for word in words if word.isalnum() and word.lower() not in stop_words]

filtered_word_freq = Counter(filtered_words)
top_filtered_words = [(word, freq) for word, freq in filtered_word_freq.most_common(10)]

top_filtered_words, filtered_frequencies = zip(*top_filtered_words)

plt.bar(top_filtered_words, filtered_frequencies)
plt.title('10 найбільш вживаних слів у тексті після фільтрації')
plt.xlabel('Слова')
plt.ylabel('Частота вживання')
plt.show()