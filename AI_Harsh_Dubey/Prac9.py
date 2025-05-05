import random

# Responses for different customer inputs
greetings = ["Hello! How can I assist you today?", "Hi there! How can I help you?", "Greetings! How may I assist you today?"]
goodbye_responses = ["Goodbye! Have a great day!", "Bye! It was a pleasure assisting you.", "Take care! Feel free to come back anytime."]
product_info = {
    "laptop": "Our laptops are top-of-the-line, starting at $599.",
    "phone": "We offer a variety of smartphones, starting at $299.",
    "headphones": "High-quality noise-cancelling headphones, priced at $89."
}

def greet_customer():
    return random.choice(greetings)

def provide_product_info(product):
    # Check if the product exists in the dictionary
    return product_info.get(product.lower(), "Sorry, I couldn't find information about that product.")

def chatbot():
    print("Welcome to our Customer Support Chatbot!")
    print("Type 'help' for assistance, 'product' for details or 'exit' to end the conversation.")
    
    while True:
        user_input = input("You: ").lower()  # Take user input
        
        if user_input in ['hi', 'hello', 'hey', 'greetings']:
            print("Bot: " + greet_customer())
        elif user_input == 'help':
            print("Bot: You can ask about our products (e.g., laptop, phone, headphones), or just say 'exit' to leave.")
        elif user_input == 'exit':
            print("Bot: " + random.choice(goodbye_responses))
            break
        elif 'product' in user_input:
            product = input("Bot: Please specify the product you want to know about (e.g., laptop, phone, headphones): ").lower()
            print("Bot: " + provide_product_info(product))
        elif 'hours' in user_input:
            print("Bot: We are open from 9 AM to 6 PM, Monday to Friday.")
        else:
            print("Bot: Sorry, I didn't understand that. Type 'help' for assistance.")

if __name__ == "__main__":
    chatbot()
