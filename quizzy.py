print("!Welcome, this is a quiz about how well you know New Zealand!")
print("!Please answer each question down below by sayin a, b, c, or d!")
scores = 0
questions = 10
Quiz_set = True

# ques1
while True:
    print(" === Easy === ")
    ans1 = input("_ - No. 1 : What is the capital city of New Zealand? - _\n a - Wellington : \n b - Auckland : \n c - Christchurch : \n d - Hamilton : ")
    if ans1 == "a":
        print("Bravo, that is correct!\n You have earned 1 point!")
        scores += 1
        break
    else:
        print("Oops, wrong answer..\n Let's try again!")

# ques2
while True:
    ans2 = input(" _ - No . 2 : What bird is New Zealand famous for? - _\n a - Tui : \n b - Penguin : \n c - Kiwi : ")
    if ans2 == "c":
        print("Bravo, That's correct!\n You have earned an extra point!")
        scores += 1
        break
    else:
        print("Oops, wrong answer..\n Let's try again!")

#ques3
while True:
    ans3 = input(" _ - No. 3 : When living in New Zealand, is it true that people here are often called as *Kiwi's*? - _\n a - FALSE : \n b - TRUE : ")
    if ans3 == "b":
        print("Bravo, that is correct!\n You have earned an extra point!")
        scores += 1
        break
    else:
        print("Oops, wrong answer..\n Let's try again!")

#ques4
while True:
    ans4 = input(" _ - No. 4 :  - _\n")