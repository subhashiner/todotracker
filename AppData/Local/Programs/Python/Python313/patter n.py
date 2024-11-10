# Define responses based on keywords or phrases
responses = {
    "hello": "Hello! How can I help you today?",
    "hi": "Hi there! What would you like to talk about?",
    "how are you": "I'm just a program, but thanks for asking! How are you?",
    "name": "I'm a simple chatbot created to chat with you.",
    "what is your name": "I am Chatbot. What’s your name?",
    "goodbye": "Goodbye! It was nice chatting with you.",
    "quit": "Thank you for chatting with me! Have a great day!"
}

# Define a function to check for keywords in user input and respond
def get_response(user_input):
    user_input = user_input.lower()  # Convert input to lowercase for easy matching
    for key in responses:
        if key in user_input:  # Check if the keyword is in the user input
            return responses[key]
    return "I'm sorry, I don't understand. Could you rephrase that?"

# Chat loop
print("Chatbot: Hello! I'm here to chat with you. Type 'quit' to end the conversation.")
while True:
    user_input = input("You: ")
    if user_input.lower() == "quit":
        print("Chatbot:", responses["quit"])
        break
    response = get_response(user_input)
    print("Chatbot:", response)
