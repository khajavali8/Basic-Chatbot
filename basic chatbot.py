import nltk
import random
from nltk.chat.util import Chat, reflections

reflections = {
    "i am": "you are",
    "i was": "you were",
    "i": "you",
    "i'm": "you are",
    "i'd": "you would",
    "i've": "you have",
    "i'll": "you will",
    "my": "your",
    "mine": "yours",
    "you are": "I am",
    "you were": "I was",
    "you've": "I have",
    "you'll": "I will",
    "your": "my",
    "yours": "mine",
    "you": "me",
    "me": "you"
}
patterns = [
    (r"(.*)hello(.*)", ("Hello!", "Hi there!", "Hey! How can I help you?")),
    (r"(.*)how are you(.*)", ("I'm doing well, thank you!", "I'm fine, thank you! How about you?")),
    (r"(.*)your name(.*)", ("You can call me ChatBot.", "I'm just a chatbot!", "I'm ChatBot.")),
    (r"(.*)bye(.*)", ("Goodbye!", "Bye! Have a great day!", "See you later!")),
    (r"thank you|thanks", ("You're welcome!", "No problem!", "My pleasure!")),
    (r"(.*)", ("I'm sorry, I didn't understand that.", "Could you please repeat that?", "I'm not sure I follow."))
]

chatbot = Chat(patterns, reflections)

def main():
    print("Welcome to the ChatBot! (Type 'bye' to exit)")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print("ChatBot: " + chatbot.respond(user_input))
            break
        else:
            print("ChatBot: " + chatbot.respond(user_input))

if __name__ == "__main__":
    main()
