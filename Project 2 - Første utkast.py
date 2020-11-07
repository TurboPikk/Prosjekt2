q1 = "Q1. What is the capital of Norway?"
q2 = "Q2.What is the currency of Norway?"
q3 = "Q3.What is the largest city in Norway?"
q4 = "Q4.When is constitution day (the national day) of Norway?"
q5 = "Q5.What color is the background of the Norwegian flag?"
q6 = "Q6.How many countries does Norway border?"
q7 = "Q7.What is the name of the university in Trondheim?"
q8 = "Q8.How long is the border between Norway and Russia?"
q9 = "Q9.Where in Norway is Stavanger?"
q10 = "Q10.From which Norwegian city did the world famous composer Edvard Grieg come?"

o1 = {
    "a" : "Bergen",
    "b" : "Oslo",
    "c" : "Stavanger",
    "d" : "Trondheim"
}

o2 = {
    "a" : "Euro",
    "b" : "Pound",
    "c" : "Krone",
    "d" : "Deutsche Mark"
}

o3 = {
    "a" : "Oslo",
    "b" : "Stavanger",
    "c" : "Bergen",
    "d" : "Trondheim"
}

o4 = {
    "a" : "27th of May",
    "b" : "17th of May",
    "c" : "17th of April",
    "d" : "27th of April"
}

o5 = {
    "a" : "Red",
    "b" : "White",
    "c" : "Blue",
    "d" : "Yellow"
}

o6 = {
    "a" : "1",
    "b" : "2",
    "c" : "3",
    "d" : "4"
}

o7 = {
    "a" : "UiS",
    "b" : "UiO",
    "c" : "NMBU",
    "d" : "NTNU"
}

o8 = {
    "a" : "96 km",
    "b" : "196 km",
    "c" : "296 km",
    "d" : "396 km"
}

o9 = {
    "a" : "North",
    "b" : "South",
    "c" : "South-west",
    "d" : "South-east"
}

o10 = {
    "a" : "Oslo",
    "b" : "Bergen",
    "c" : "Stavanger",
    "d" : "Tromsø"
}


alternatives = (o1, o2, o3, o4, o5, o6, o7, o8, o9, o10)
questions = (q1, q2, q3, q4, q5, q6, q7, q8, q9, q10)
answer_list = ("a", "b", "c", "d")
solution = ("b", "c", "a", "b", "a", "c", "d", "b", "c", "b")


validCredentials = { "MEK1300" : "Python" }



def login():
    while True:
        check = { input("Enter your username: ") : input("Enter your password: ") }
        if login_info(validCredentials, check) == True:
            break
        else:
            print("Invalid  username  and/or  password")

def login_info(stored, attempt):
    if stored == attempt:
        return True
    else:
        return False


def print_questions():
    answers = []
    for i in range(10):
        print(f"\n{questions[i]}")

        for key in alternatives[i]:
            print(f"{key}: {alternatives[i][key]}")

        while True:
            answer = input("Enter your choice: ")
            if answer in answer_list:
                break
        answers.append(answer)
    return answers


def results(questions, choices, reference, answer):
    score = 0
    for i in range(len(reference)):
        if answer[i] == reference[i]:
            score += 1
        else:
            pass

    print(f"""
--------
Results:
--------
Number of correct answers: {score}
Number of wrong answers:   {10 - score}

--------------
Wrong answers:
--------------""")

    for i in range(len(reference)):
        if answer[i] != reference[i]:
            print(f"""{questions[i]}
Your answer was:    {answer[i]}: {choices[i][answer[i]]}
Correct answer was: {reference[i]}: {choices[i][reference[i]]}
""")
        else:
            pass



def quiz():
    #login()
    outcome = print_questions()
    results(questions, alternatives, solution, outcome)



quiz()
    
