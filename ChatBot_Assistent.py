import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    ['my name is (.*)', ['Hi %1, how can I help you?']],
    ['(hi|hello|hey|hola)', ['Hello, how can I assist you?']],
    ['how are you?', ['I am doing well, thank you!', 'I am fine, thank you for asking.']],
    ['who are you?', ['I am chatbot AI']],
    ['what is your name?', ['My name is Devin2.']],
    ['you know who i am?', ['Yes you are my onwer and you created me. thank you so much!']],
    ['can you help me', ['Sure, I can help you with that. What do you need assistance with?']],
    ['you live in which (location|city) ?', ['I am an AI and I exist in the virtual world.']],
    ['who created you?', ['I was created by a team of developers.']],
    ['how (age|old) are you ?', ['I am a computer program, so I don\'t have an age.']],
    ['how i can check (weather|temperature) ?', ['You can check the weather using various online services.']],
    ['(.*)', ['I apologize, but I am not sure how to respond to that.']]
]

chatbot = Chat(pairs, reflections)

def chat():
    print("Welcome! How can I assist you today?")
    print("press q for quit")
    while True:
        user_input = input("> ")
        if user_input.lower() == 'q':
            print("Thank you for using me!")
            print("Goodbye!")
            break
        else:
            response = chatbot.respond(user_input)
            print(response)

if __name__ == "__main__":
    nltk.download('punkt')
    chat()
