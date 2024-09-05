import re
import collections
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import os

nltk.download('stopwords')
nltk.download('punkt')
wordcloud = WordCloud()

def get_text(filename):
    with open(filename,'r',encoding='utf-8') as file:
        text=file.read()
    return text

# Function to preprocess the text
def preprocess_text(text):
    # Convert to lowercase
    text = text.lower()
    # Remove special characters and numbers
    text = re.sub(r'\W+', ' ', text)
    text = re.sub(r'\d+', '', text)
    return text

def remove_stopwords(tokens):
    stop_words = set(stopwords.words('english'))
    return [word for word in tokens if word not in stop_words]

# Function to get the top N keywords
def get_top_keywords(text, n=10):
    # Preprocess text
    cleaned_text = preprocess_text(text)
    # Tokenize text
    tokens = word_tokenize(cleaned_text)
    # Remove stop words
    filtered_tokens = remove_stopwords(tokens)
    # Count word frequencies
    word_counts = collections.Counter(filtered_tokens)
    # Get the top n keywords
    top_keywords = word_counts.most_common(n)
    return top_keywords


def generate(filename):
    corpus = get_text(f'data\{filename}')
    top_keywords = dict(get_top_keywords(corpus,30))
    plt.figure()
    Wordcloud=wordcloud.generate_from_frequencies(frequencies=top_keywords)    
    plt.imshow(Wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.savefig(f"{filename[:-4]}.png", format="png", bbox_inches="tight")
    #plt.show()

for file in os.listdir('data'):
    generate(file)
