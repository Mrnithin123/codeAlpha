import nltk
from nltk.chat.util import Chat, reflections
nltk.download('punkt')
nltk.download('wordnet')
pairs = [
    (r'hi|hello|hey', ['Hello there! How can I help you today?']),
    (r'bye|exit|quit', ['Goodbye! Have a great day!']),
    (r'how are you?', ['I am just a bot, but I am doing fine! How about you?']),
    (r'I am (.*)', ['Oh, so you are %1. Tell me more about that.']),
    (r'what is your name?', ['I am CodeAlphaBot, your assistant.']),
    (r'where are you from?', ['I am from the digital world, here to assist you!']),
    (r'(.*) your (.*)', ['Sorry, I didn’t quite understand that. Can you rephrase?']),
    (r'(.*)', ['Interesting! Can you tell me more?'])
]
chatbot = Chat(pairs, reflections)
def chat():
    print("Hello! I am your chatbot. Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['bye', 'exit', 'quit']:
            print("Chatbot: Goodbye! Take care!")
            break
        else:
            response = chatbot.respond(user_input)
            print(f"Chatbot: {response}")
if __name__ == "__main__":
    chat()
