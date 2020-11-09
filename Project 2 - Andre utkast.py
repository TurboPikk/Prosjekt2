quiz = [
    {
        "question" : "Q1. What is the capital of Norway?",
        "alternatives" : {
            "a" : "Bergen",
            "b" : "Oslo",
            "c" : "Stavanger",
            "d" : "Trondheim"},
        "solution" : "b"
    },
    {
        "question" : "Q2.What is the currency of Norway?",
        "alternatives" : {
            "a" : "Euro",
            "b" : "Pound",
            "c" : "Krone",
            "d" : "Deutsche Mark"},
        "solution" : "c"
    },
    {
        "question" : "Q3.What is the largest city in Norway?",
        "alternatives" : {
            "a" : "Oslo",
            "b" : "Stavanger",
            "c" : "Bergen",
            "d" : "Trondheim"},
        "solution" : "a"
    },
    {
        "question" : "Q4.When is constitution day (the national day) of Norway?",
        "alternatives" : {
            "a" : "27th of May",
            "b" : "17th of May",
            "c" : "17th of April",
            "d" : "27th of April"},
        "solution" : "b"
    },
    {
        "question" : "Q5.What color is the background of the Norwegian flag?",
        "alternatives" : {
            "a" : "Red",
            "b" : "White",
            "c" : "Blue",
            "d" : "Yellow"},
        "solution" : "a"
    },
    {
        "question" : "Q6.How many countries does Norway border?",
        "alternatives" : {
            "a" : "1",
            "b" : "2",
            "c" : "3",
            "d" : "4"},
        "solution" : "c"
    },
    {
        "question" : "Q7.What is the name of the university in Trondheim?",
        "alternatives" : {
            "a" : "UiS",
            "b" : "UiO",
            "c" : "NMBU",
            "d" : "NTNU"},
        "solution" : "d"
    },
    {
        "question" : "Q8.How long is the border between Norway and Russia?",
        "alternatives" : {
            "a" : "96 km",
            "b" : "196 km",
            "c" : "296 km",
            "d" : "396 km"},
        "solution" : "b"
    },
    {
        "question" : "Q9.Where in Norway is Stavanger?",
        "alternatives" : {
            "a" : "North",
            "b" : "South",
            "c" : "South-west",
            "d" : "South-east"},
        "solution" : "c"
    },
    {
        "question" : "Q10.From which Norwegian city did the world famous composer Edvard Grieg come?",
        "alternatives" : {
            "a" : "Oslo",
            "b" : "Bergen",
            "c" : "Stavanger",
            "d" : "Tromsø"},
        "solution" : "b"
    },
]

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

def print_questions(quiz):
    answers = []
    for questions in quiz:
        print(f"\n{questions['question']}")
        for key in questions["alternatives"]:
            print(f"{key}: {questions['alternatives'][key]}")
        while True:
            answer = input("Enter your choice: ")
            if answer in questions['alternatives']:
                break
        answers.append(answer)
    return answers

def results(quiz, answers):
    score = 0
    failed_answers = []
    for i in range(len(quiz)):
        if answers[i] == quiz[i]["solution"]:
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

    for i in range(len(quiz)):
        if answers[i] != quiz[i]['solution']:
            print(f"""{quiz[i]['question']}
Your answer was:    {answers[i]}: {quiz[i]['alternatives'][answers[i]]}
Correct answer was: {quiz[i]['solution']}: {quiz[i]['alternatives'][quiz[i]['solution']]}
""")
        else:
            pass

def run_quiz():
    login()
    results(quiz, print_questions(quiz))



run_quiz()
    
