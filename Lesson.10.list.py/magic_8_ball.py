# =====================================================================
# PROJECT: The Magic 8-Ball Fortune Teller
# Create a program that gives random responses to yes/no questions
# =====================================================================

# TOOLS
# TODO: Import the 'random' module so we can pick a random index later.

# RESPONSES
# TODO: Create a list called 'responses' that contains at least 8 different 
#       8-ball answers (strings). There should be positive answers, negative answers and neutral answers.
#       Examples: "Yes, definitely!", "Ask again later.", "Outlook not so good."

# MAIN LOOP
# TODO Create an infinite loop
    
    # TODO: Ask the user to type in a Yes/No question about their future and save it in a variable.
    #       (Or tell them to type 'quit' to leave).
    
    # Check if the user wants to exit and break from the loop if they do.
        
    # RANDOM REPSONSE
    # TODO: Step A: Calculate the last valid index of your list.
    #       (Remember: If a list has 5 items, the indexes are 0, 1, 2, 3, 4).
    #       Use random.randint() to get a number between 0 and that last index.
    #       Save it in a variable called 'random_index'.
    
    
    # TODO: Step B: Use your 'random_index' to grab the matching answer 
    #       out of your 'responses' list.
    #       Save it in a variable called 'chosen_fortune'.

    # TODO Print the result

# TODO Say goodbye to let them know the program has ended.

# ==================================================
import random
responses = ["Absolutely!","Ooh, not too sure!","Sorry, what did you say?","Definitely not!"]
print(responses[4])

while True:
    question = input("Ask the magical 8-Ball a Yes/No question. Otherwise, type exit to leave")
    if question.lower().upper() == "exit":
        print("Alright then, have a nice day!")
        break
    