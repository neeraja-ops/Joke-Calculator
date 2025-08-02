import random
import time

def useless_calculator():
    print("Welcome to the Useless Calculator™")
    print("It calculates... something. Probably.")
    print("Select your operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Enlighten me")

    choice = input("Enter your choice (1-5): ")
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")

    print("\nCalculating result...")
    time.sleep(2)

    jokes = [
        "Why was the equal sign so humble? Because it knew it wasn't less than or greater than anyone else!",
        "Parallel lines have so much in common. It's a shame they'll never meet.",
        "Why do plants hate math? Because it gives them square roots.",
        "Why was the math book sad? Because it had too many problems.",
        "I'm reading a book on anti-gravity. It's impossible to put down!",
        "Why did seven eat nine? Because you're supposed to eat three squared meals a day!",
        "I tried to be a mathematician but I couldn't count on it.",
        "What's a math teacher's favorite place in NYC? Times Square.",
        "Why did the student do multiplication problems on the floor? The teacher told him not to use tables.",
        "What do you call a number that can't keep still? A roamin' numeral.",
        "Why was the fraction nervous about marrying the decimal? Because he would have to convert.",
        "Why did the obtuse angle go to the beach? Because it was over 90 degrees!",
        "What do you call an angle that's adorable? A-cute angle.",
        "Why is the number 6 afraid of 7? Because 7 8 9!",
        "How do you stay warm in a cold room? Stand in the corner—it's always 90 degrees.",
        "What did zero say to eight? Nice belt!",
        "Why do mathematicians like parks? Because of all the natural logs.",
        "Why can't your nose be 12 inches long? Because then it would be a foot.",
        "Why was the math lecture so long? The professor kept going off on a tangent.",
        "What did the triangle say to the circle? You're pointless.",
        "Why did the calculator break up with the pencil? It felt like it was being used.",
        "What do you get when you cross geometry with McDonald's? A plane cheeseburger.",
        "Why did the mathematician work at Starbucks? Because she loved dealing with large sums.",
        "Why did the student eat his math homework? Because the teacher said it was a piece of cake.",
        "What's the best tool to do math? Multi-pliers!",
        "Why did the number go to therapy? It couldn't find its roots.",
    ]

    print(random.choice(jokes))

# Correct entry point
if __name__ == "__main__":
    useless_calculator()
