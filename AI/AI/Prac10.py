def ask_question(question, valid_answers):
    while True:
        answer = input(question + " ").strip().lower()
        if answer in valid_answers:
            return answer
        else:
            print(f"Invalid input. Please enter one of: {', '.join(valid_answers)}")

def evaluate(trend, fundamentals, indicators):
    if trend == "upwards" and fundamentals == "strong" and indicators == "positive":
        return True, "All indicators are positive: upward trend, strong fundamentals, and positive technicals."
    elif trend == "upwards" and fundamentals == "strong":
        return True, "Market trend and fundamentals are strong. Positive enough to consider buying."
    else:
        return False, "Market or company signals are not strong enough to recommend buying."

def print_result(should_buy, reason):
    print("\nEvaluation Result:")
    print(reason)
    if should_buy:
        print("✅ Recommendation: Buy the stock!")
    else:
        print("❌ Recommendation: Do not buy the stock.")

def main():
    print("📈 Welcome to the Stock Market Expert System!")
    print("This system will guide you on whether to buy a stock based on your answers.\n")

    while True:
        trend = ask_question("1. What is the current market trend? (upwards/downwards):", ["upwards", "downwards"])
        fundamentals = ask_question("2. How are the fundamentals of the company? (strong/weak):", ["strong", "weak"])
        indicators = ask_question("3. What do the technical indicators suggest? (positive/negative):", ["positive", "negative"])

        should_buy, reason = evaluate(trend, fundamentals, indicators)
        print_result(should_buy, reason)

        again = input("\nDo you want to evaluate another stock? (yes/no): ").strip().lower()
        if again != "yes":
            print("Thank you for using the Stock Market Expert System. Goodbye!")
            break

if __name__ == "__main__":
    main()