def chatbot():
    print("Welcome to ShopEase Customer Support Chatbot!")
    print("How can I help you today? (Type 'exit' to quit)\n")

    while True:
        user_input = input("You: ").lower()

        if user_input == 'exit':
            print("Chatbot: Thank you for visiting ShopEase! Have a great day 😊")
            break

        elif "order" in user_input and "track" in user_input:
            print("Chatbot: You can track your order at: https://shopease.com/track-order")

        elif "return" in user_input:
            print("Chatbot: Our return policy allows returns within 30 days. Visit: https://shopease.com/returns")

        elif "refund" in user_input:
            print("Chatbot: Refunds are processed within 5-7 business days after item inspection.")

        elif "contact" in user_input or "customer care" in user_input:
            print("Chatbot: You can contact us at support@shopease.com or call 1800-123-456.")

        elif "product" in user_input:
            print("Chatbot: Please visit our product catalog here: https://shopease.com/products")

        elif "payment" in user_input:
            print("Chatbot: We accept credit/debit cards, UPI, net banking, and wallets like Paytm and PhonePe.")

        else:
            print("Chatbot: I'm sorry, I didn't understand that. Please try rephrasing your question.")

# Run chatbot
if __name__ == "__main__":
    chatbot()
