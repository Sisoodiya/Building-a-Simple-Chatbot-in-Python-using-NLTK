# Chatbot Project

This project implements a simple chatbot named cortana_ka_ex using Python. The chatbot can respond to user queries about chatbots and engage in basic conversation.

## Features

- **Greeting Responses**: cortana_ka_ex can recognize and respond to greetings.
- **Query Responses**: cortana_ka_ex uses TF-IDF vectorization and cosine similarity to generate responses to user queries based on a provided text corpus.
- **Interactive Chat Loop**: The chatbot runs in a loop, allowing continuous interaction until the user types "Bye".

## Libraries Used

- `io`
- `random`
- `string`
- `warnings`
- `numpy`
- `sklearn`
- `nltk`

## Setup

1.Ensure you have the necessary NLTK data downloaded:

```python
    nltk.download('punkt', download_dir='/Users/abhaysinghsisoodiya/nltk_data')
    nltk.download('wordnet', download_dir='/Users/abhaysinghsisoodiya/nltk_data')
    nltk.download('stopwords', download_dir='/Users/abhaysinghsisoodiya/nltk_data')
```

2.Place your text corpus in a file named `chatbot.txt` in the same directory as the script.

## How to Run

Execute the script to start the chatbot:

```bash
python3 chatbot.py
```

## Example Interaction

``` 
cortana_ka_ex: My name is cortana_ka_ex. I will answer your queries about Chatbots. If you want to exit, type Bye!
User: Hello
cortana_ka_ex: hi
User: What is a chatbot?
cortana_ka_ex: [Response based on the text corpus]
User: Bye
cortana_ka_ex: Bye! Take care..
```