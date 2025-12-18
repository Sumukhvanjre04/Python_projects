import datetime
import time

name = input("Enter your name:")
current_time = datetime.datetime.now().hour
start_time = datetime.datetime.now()

if 5 <= current_time < 12:
    print("Good Morning!", name)
elif 12 <= current_time < 19:
    print("Good Evening!", name)
else:
    print("Good Night!", name)

print("Hello! Welcome to Rule based chat assistant")
print("You can ask me basic questions.")
print("Enter 1 to Chat with an assistant\nEnter 2 to view your chat history")
print("Type 'bye' to exit!")
print("\n\nHere are some questions you can ask")
print("Hello, How are you, Who are you, What is your name, What is python, Motivate me, What is the time, What is AI")

# create memory
responses = {
    "hello": "Hi, Welcome. How can I help you?",
    "how are you": "I am good. Thank you!",
    "who are you": "I am smart AI chatbot",
    "what is your name": "I am smart AI chatbot",
    "what is python": "Python is an high-level programming language used in AI, automation and Data Science.",
    "motivate me": "You don't need motivation. You just need action",
    "what is the time": lambda: f"The current time is:{datetime.datetime.now().strftime('%H:%M')}",
    "what is ai": "Artificial intelligence is a branch of computer science used to make machine smart"
}

# function to get responses
def getresponse(user_input):
    user_input = user_input.lower()
    for key in responses:
        if key in user_input:
            response = responses[key]
            time.sleep(2)
            return response() if callable(response) else response
    else:
        time.sleep(2)
        return "I am still in learning mode.Please try to ask another question"

# clearing a file
open("history.txt", "w").close()

# take user input
while True:
    try:
        choice = int(input("Enter your choice:"))
        if choice == 1:
            user_input = input("Enter your question\nYou:")
            if "bye" in user_input:
                break
            answer = getresponse(user_input)
            print("Bot answer:", answer)
            with open("history.txt", "a") as f:
                f.write(f"You:{user_input}\n")
                f.write(f"Bot answer:{answer}\n\n")
            print("\n")

        elif choice == 2:
            with open("history.txt", "r") as f:
                print("CHAT HISTORY")
                print(f"Session started at {start_time.strftime('%H:%M')}")
                lines = f.readlines()
                if not lines:
                    print("The chat history is empty")
                else:
                    for text in lines:
                        print(text, end="")

    except ValueError:
        print("Kindly choose 1 or 2 to interact with the chatbot")

end_time = datetime.datetime.now()
duration = end_time - start_time
total_seconds = int(duration.total_seconds())
minutes = total_seconds // 60
seconds = total_seconds % 60
print(f"You spent {minutes} minutes and {seconds} seconds using chatbot")
print("Thank you for using chatbot.")
