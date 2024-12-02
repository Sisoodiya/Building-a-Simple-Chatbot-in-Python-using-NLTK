# Meet cortana_ka_ex: your friend

# Import necessary libraries
import io
import random
import string  # to process standard Python strings
import warnings
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import nltk
from nltk.stem import WordNetLemmatizer

# Specify the path to NLTK data
nltk.data.path.append('/Users/abhaysinghsisoodiya/nltk_data')

# Download necessary NLTK data (uncomment the following lines if not already downloaded)
# nltk.download('punkt', download_dir='/Users/abhaysinghsisoodiya/nltk_data')
# nltk.download('wordnet', download_dir='/Users/abhaysinghsisoodiya/nltk_data')
# nltk.download('stopwords', download_dir='/Users/abhaysinghsisoodiya/nltk_data')

# Suppress warnings
warnings.filterwarnings('ignore')

# Reading in the corpus
with open('chatbot.txt', 'r', encoding='utf8', errors='ignore') as fin:
    raw = fin.read().lower()

# Tokenization
sent_tokens = nltk.sent_tokenize(raw)  # Converts to a list of sentences
word_tokens = nltk.word_tokenize(raw)  # Converts to a list of words

# Preprocessing
lemmer = WordNetLemmatizer()

def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]

remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)

def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))

# Keyword Matching
GREETING_INPUTS = ("hello", "hi", "greetings", "sup", "what's up", "hey",)
GREETING_RESPONSES = ["hi", "hey", "*nods*", "hi there", "hello", "I am glad! You are talking to me"]

def greeting(sentence):
    """If user's input is a greeting, return a greeting response"""
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)

# Generating a response
def response(user_response):
    cortana_ka_ex_response = ''
    sent_tokens.append(user_response)
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    tfidf = TfidfVec.fit_transform(sent_tokens)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx = vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    if req_tfidf == 0:
        cortana_ka_ex_response = cortana_ka_ex_response + "I am sorry! I don't understand you"
        return cortana_ka_ex_response
    else:
        cortana_ka_ex_response = cortana_ka_ex_response + sent_tokens[idx]
        return cortana_ka_ex_response

# Main chat loop
flag = True
print("cortana_ka_ex: My name is cortana_ka_ex. I will answer your queries about Chatbots. If you want to exit, type Bye!")
while flag:
    user_response = input()
    user_response = user_response.lower()
    if user_response != 'bye':
        if user_response in ('thanks', 'thank you'):
            flag = False
            print("cortana_ka_ex: You are welcome..")
        else:
            if greeting(user_response) is not None:
                print("cortana_ka_ex: " + greeting(user_response))
            else:
                print("cortana_ka_ex: ", end="")
                print(response(user_response))
                sent_tokens.remove(user_response)
    else:
        flag = False
        print("cortana_ka_ex: Bye! Take care..")