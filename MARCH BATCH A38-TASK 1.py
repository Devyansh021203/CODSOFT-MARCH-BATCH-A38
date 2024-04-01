def respond_to_user_input(user_input):

    user_input = user_input.lower()


    if "hello" in user_input:
        return "Hi there! How can I help you today?"
    elif "how are you" in user_input:
        return "I'm just a chatbot, but thanks for asking!"
    elif "weather" in user_input:
        return "I'm sorry, I'm not enough trained to provide weather information."
    elif "goodbye" in user_input:
        return "Goodbye Have a great day!"
    else:
        return "I'm sorry, I didn't understand that."

def main():
    print("Welcome! How can I assist you today?")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Goodbye! Have a great day!")
            break
        response = respond_to_user_input(user_input)
        print("Bot:", response)

if __name__ == "__main__":
    main()
