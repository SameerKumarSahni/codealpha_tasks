# TASK 4: BASIC CHATBOT

def chatbot_response(user_input):
    """
    This function takes the user's input
    and returns an appropriate response.
    """

    if user_input == "hello":
        return "Hi! Nice to meet you."

    elif user_input == "hi":
        return "Hello! How can I help you?"

    elif user_input == "how are you":
        return "I'm fine, thanks!"

    elif user_input == "what is your name":
        return "My name is CodeAlpha Bot."

    elif user_input == "what can you do":
        return "I can respond to some basic messages."

    elif user_input == "thank you":
        return "You're welcome!"

    elif user_input == "bye":
        return "Goodbye! Have a nice day."

    else:
        return "Sorry, I don't understand that."

# MAIN CHATBOT PROGRAM

print("====================================")
print("          BASIC CHATBOT")
print("====================================")
print("Type 'bye' to exit the chatbot.\n")


while True:

    user_input = input("You: ").lower().strip()

    response = chatbot_response(user_input)

    print("Bot:", response)

    if user_input == "bye":
        break


print("\nChatbot session ended.")
