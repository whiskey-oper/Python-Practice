print("!Welcome, this is a quiz about how well you know New Zealand!")
print("!Please answer each question down below by sayin a, b, c, or d!")
scores = 0
questions = 10
Quiz_set = True

# Easy questions
# ques1
while True:
    print(" === ✨Easy✨ === ")
    ans1 = input("_ - No. 1 : What is the capital city of New Zealand? - _\n a - Wellington : \n b - Auckland : \n c - Christchurch : \n d - Hamilton : ")
    if ans1 .lower() == "a":
        print("🌟Bravo, that is correct!\n You have earned 1 point!🌟")
        scores += 1
        break
    else:
        print("Oops, wrong answer..\n Let's try again")

# ques2
while True:
    ans2 = input(" _ - No . 2 : What bird is New Zealand famous for? - _\n a - Tui : \n b - Penguin : \n c - Kiwi : ")
    if ans2 .lower() == "c":
        print("🌟Bravo, that is correct!\n You have earned 1 point!🌟")
        scores += 1
        break
    else:
        print("Oops, wrong answer..\n Let's try again")

#ques3
while True:
    ans3 = input(" _ - No. 3 : When living in New Zealand, is it true that people here are often called as *Kiwi's*? - _\n a - FALSE : \n b - TRUE : ")
    if ans3 .lower() == "b":
        print("🌟Bravo, that is correct!\n You have earned 1 point!🌟")
        scores += 1
        break
    else:
        print("Oops, wrong answer..\n Let's try again")

# Medium questions

# ques4
while True:
    print("\n Let's make this more interesting shall we? ;) \n === ✨Medium✨ === ")
    ans4 = input(" _ - No. 4 : Are indigenous people in New Zealand called Maori's? - _\n a - TRUE : \n b - FALSE : ")
    if ans4 .lower() == "a":
        print("🌟Bravo, that is correct!\n You have earned 1 point!🌟")
        scores += 1
        break
    else:
        print("Oops, wrong answer.. \n Let's try again")

# ques5
while True:
    ans5 = input(" _ - No. 5 : In which ocean is New Zealand located? - _\n a - Pacific Oceania : \n b - Atlantic Ocean : \n c - Southern Ocean : ")
    if ans5 .lower() == "a":
        print("🌟Bravo, that is correct!\n You have earned 1 point!🌟")
        scores += 1
        break
    else:
        print("Oops, wrong answer..\n Let's try again")

# ques6
while True:
    ans6 = input(" _ - No. 6 : What mountain is the highest? - _\n a - Aoraki/ Mount Cook : \n b - Tasman : \n c - Malte Brun : \n d - Mount Taranaki : ")
    if ans6 .lower() == "a":
        print("🌟Bravo, that is correct!\n You have earned 1 point!🌟")
        scores += 1
        break
    else:
        print("Oops, wrong answer..\n Let's try again")

# Hard questions

# ques7
while True:
    print(" === ✨Hard✨ === \n Nearly there!")
    ans = input(" _ - No. 7 : Which City is known as the 'Garden City'? - _\n a - Dunedin : \n b - Gisborne : \n c - Napier : \n d - Christchurch : ")
    if ans .lower() == "d":
        print("🌟Bravo, that is correct!\n You have earned 1 point!🌟")
        scores += 1
        break
    else:
        print("Oops, wrong answer..\n Let's try again")

# ques8
while True:
    ans8 = input(" _ - No. 8 : What is New Zealand's national sport? - _\n a - Volleyball : \n b - Tennis : \n c - Rugby : \n d - Badminton : ")
    if ans8 .lower() == "c":
        print("🌟Bravo, that is correct!\n You have earned 1 point!🌟")
        scores += 1
        break
    else:
        print("Oops, wrong answer..\n Let's try again")

# ques9
while True:
    ans9 = input(" _ - No. 9 : What sea separates both North and South Islands? - _\n a - Tasman : \n b - Cook Strait : \n c - Waikato :")
    if ans9 .lower() == "b":
        print("🌟Bravo, that is correct!\n You have earned 1 point!🌟")
        scores += 1
        break
    else:
        print("Oops, wrong answer..\n Let's try again\n")

# Bonus round for question 10

print("\n !✨Last but not least is all you have been currently waiting for!✨")
print("This is worth double points as well ;)")

while True:
    ans10 = input(" ! _ -- No. 10 : Do you love New Zealand?\n Yes , Maybe , No")
    if ans10 .lower() == ("Yes", "YES", "yes"):
        print("Aw! Then you are a superstar for that!")
        scores += 1
        
    elif ans10 .lower() == ("Maybe"):
        print("Well that's okay, not everyone doesn't like New Zealand! :,)")
        scores += 1
        
    else:
        ans10 .lower() == ("No", "Nope") or ans10 .lower() == ("Nah", "Nuh uh")
    print("Oh wow, why are you taking my quiz then HMMM??🤨 \n By the way, I've taken one point away from you- ")
    scores -= 1
    break

# Closing message
print("You have done so well answering the questions above - ")
print("\n But we will have to see the scores you have earned!")

# Results for the users amount of scores and questions they got correct
print(f"\n Your final result is..\n {scores}/10!")
if scores == 10:
    print("Way to go superstar! You are a New Zealander expert!🥳")

elif scores >= 5:
    print(f"Well done, but you still have {questions} to go! However, that proves that you know a fair bit of New Zealand.")

else:
    scores <= 5
    print(f"So.. if your score is {scores}/10- Get better.\n Or keep on learning to ace this quiz next time...")

print("\n🙌!That's all folks!🙌")